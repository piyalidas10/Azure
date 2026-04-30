from openai import AzureOpenAI
from typing import Dict, Any, List

GPT5_ENDPOINT = ""
GPT5_KEY = ""
GPT5_DEPLOYMENT = ""
GPT5_API_VERSION=""

GPT4_ENDPOINT = ""
GPT4_KEY = ""
GPT4_DEPLOYMENT = ""
GPT4_API_VERSION=""

MAX_TOKENS=5000

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

def ask_models(user_prompt: str,system_prompt: str = "You are a helpful assistant.",history: List[Dict[str, str]] = None)-> Dict[str, Any]:
    if history is None:
        history = []

    results = {}

    response5 = client_gpt5.chat.completions.create(
        model=GPT5_DEPLOYMENT,
        messages=[
            {"role": "system", "content": system_prompt},
            *history,
            {"role": "user", "content": user_prompt}
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
            {"role": "system", "content": system_prompt},
            *history,
            {"role": "user", "content": user_prompt}
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

if __name__ == "__main__":
    history = []
    user_input = "Explain the difference between supervised and unsupervised learning with examples."
    result = ask_models(user_input, history=history)
    for model, output in result.items():
        print(f"\n=== {model} ===")
        print("Response:", output["response"])
        print(f"Tokens Used → Prompt: {output['prompt_tokens']} | Completion: {output['completion_tokens']} | Total: {output['total_tokens']}")