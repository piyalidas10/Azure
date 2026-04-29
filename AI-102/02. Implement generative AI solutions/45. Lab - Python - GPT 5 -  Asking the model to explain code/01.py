from openai import AzureOpenAI
import base64

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://cloud-metks4fx-eastus2.cognitiveservices.azure.com/",
    api_key="",
)

with open("code.py","r",encoding="utf-8") as code_file:
    code_content=code_file.read()

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant who helps teach how to code.",
        },
        {
            "role": "user",
            "content":f"Explain clearly what the following Python code does:\n\n{code_content}"     
        }
    ],
    max_tokens=16384,
    temperature=0.7,
    top_p=1.0,
    model="gpt-5-chat"
)

print(response.choices[0].message.content)
