from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://cloud-metks4fx-eastus2.cognitiveservices.azure.com/",
    api_key="",
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Please give me an introduction onto Large Language Models",
        }
    ],
    max_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model="gpt-5-chat"
)

print(response.choices[0].message.content)