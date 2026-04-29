from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2025-03-01-preview",
    azure_endpoint="https://cloud-metks4fx-eastus2.cognitiveservices.azure.com/",
    api_key="",
)

f=client.files.create(
    file=open("Invoice.pdf","rb"),
    purpose="assistants"
)

response = client.responses.create(
    input=[        
        {
            "role": "user", 
            "content": 
         [
         {
                  "type": "input_text",
                  "text": "Extract the details from the invoice"
          },
          {
                  "type": "input_file",
                  "file_id": f.id,
              }
         ]}
    ],
    max_output_tokens=10000,
    temperature=0.7,
    model="gpt-5-chat"
)

print(response.output_text)
