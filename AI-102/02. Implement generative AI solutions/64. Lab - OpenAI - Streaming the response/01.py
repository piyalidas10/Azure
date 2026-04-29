from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2025-03-01-preview",
    azure_endpoint="https://cloud-metks4fx-eastus2.cognitiveservices.azure.com/",
    api_key="",
)


response = client.responses.create(
    input=[        
        {"role": "system", "content": "You are an assistant who helps teach how to code"},
        {"role": "user", "content": "How can I write a simple Python program that interacts with an OpenAI Model"}
    ],
    max_output_tokens=10000,
    temperature=0.7,
    model="gpt-5-chat",
    stream=True
)

for event in response:
    if event.type=="response.output_text.delta":
        print(event.delta,end="", flush=True)
    elif event.type=="response.output_text.done":
        print()
