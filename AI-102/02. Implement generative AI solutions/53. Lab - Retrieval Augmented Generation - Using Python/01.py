from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://foundry3000.cognitiveservices.azure.com/",
    api_key="",
)

rag_params = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": "https://search4000.search.windows.net",
                "index_name": "dataindex",
                "authentication": {
                    "type": "api_key",
                    "key": "rFjpsL8Y0EIMRpYV6ZK2AxupM3GqYwhod770FsGLYtAzSeBaJ7wL",
                }
            }
        }
    ],
}

response = client.chat.completions.create(
    messages=[        
        {
            "role": "user",
            "content": "What are Decision trees",
        }
    ],
    max_tokens=16384,
    temperature=0.7,
    top_p=1.0,
    model="gpt-4.1",
    extra_body=rag_params
)

print(response.choices[0].message.content)
