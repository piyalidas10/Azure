from openai import AzureOpenAI
from typing import Dict, Any, List
from fastapi import FastAPI, Body,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field
import os

from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeTextOptions, TextCategory

GPT5_ENDPOINT = os.getenv("AZURE_GPT5_ENDPOINT")
GPT5_KEY = os.getenv("AZURE_GPT5_KEY")
GPT5_DEPLOYMENT = os.getenv("AZURE_GPT5_DEPLOYMENT")
GPT5_API_VERSION=os.getenv("AZURE_GPT5_VERSION")

GPT4_ENDPOINT = os.getenv("AZURE_GPT4_ENDPOINT")
GPT4_KEY = os.getenv("AZURE_GPT4_KEY")
GPT4_DEPLOYMENT = os.getenv("AZURE_GPT4_DEPLOYMENT")
GPT4_API_VERSION=os.getenv("AZURE_GPT4_VERSION")

MAX_TOKENS=5000

CS_ENDPOINT = os.getenv("CONTENT_SAFETY_ENDPOINT")
CS_KEY = os.getenv("CONTENT_SAFETY_KEY")

client_gpt5 = AzureOpenAI(
    api_key=GPT5_KEY,
    api_version=GPT5_API_VERSION,
    azure_endpoint=GPT5_ENDPOINT
)

client_gpt4 = AzureOpenAI(
    api_key=GPT4_KEY,
    api_version=GPT4_API_VERSION,
    azure_endpoint=GPT4_ENDPOINT
)

cs_client = ContentSafetyClient(CS_ENDPOINT, AzureKeyCredential(CS_KEY))

app = FastAPI(title="Chat API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],  # your React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_prompt: str
    system_prompt: str = "You are a helpful assistant."
    history: List[Dict[str, str]] = Field(default_factory=list)

def ensure_prompt_is_allowed(text: str) -> List[Dict[str, Any]]:
    res=cs_client.analyze_text(AnalyzeTextOptions(text=text))
    # Now we can build a findings list that contain the category like harm etc and their severity
    findings = []
    for item in res.categories_analysis:
        cat = item.category.name if hasattr(item.category, "name") else str(item.category)
        sev = int(item.severity or 0)
        findings.append({"category": cat, "severity": sev})

    print(findings)
# We can raise an HTTP Exception if any severity is greater than 4
    if any(f["severity"] >= 4 for f in findings):
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Prompt blocked by Azure Content Safety.",
                "findings": findings
            }
        )
    
    return findings

@app.post("/ask")   
def ask_models(req: ChatRequest)-> Dict[str, Any]:
    moderation = ensure_prompt_is_allowed(req.user_prompt)
    history = req.history or []

    results = {"moderation": moderation}

    response5 = client_gpt5.chat.completions.create(
        model=GPT5_DEPLOYMENT,
        messages=[
            {"role": "system", "content": req.system_prompt},
            *req.history,
            {"role": "user", "content": req.user_prompt}
        ],
        max_tokens=MAX_TOKENS
    )

    results["gpt-5"] = {
        "response": response5.choices[0].message.content,
        "prompt_tokens": response5.usage.prompt_tokens,
        "completion_tokens": response5.usage.completion_tokens,
        "total_tokens": response5.usage.total_tokens
    }

    response4 = client_gpt4.chat.completions.create(
        model=GPT4_DEPLOYMENT,
        messages=[
            {"role": "system", "content": req.system_prompt},
            *req.history,
            {"role": "user", "content": req.user_prompt}
        ],
        max_tokens=MAX_TOKENS
    )

    results["gpt-4"] = {
        "response": response4.choices[0].message.content,
        "prompt_tokens": response4.usage.prompt_tokens,
        "completion_tokens": response4.usage.completion_tokens,
        "total_tokens": response4.usage.total_tokens
    }

    return results
