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
            "content": "You are an assistant helping students to learn about Large Language Models.",
        },
        {
            "role": "user",
            "content": "What is the temperature setting",
        }
    ],
    max_tokens=16384,
    temperature=0.7,
    top_p=1.0,
    model="gpt-5-chat"
)

print(response.choices[0].message.content)
