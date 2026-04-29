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

invoice_schema = {
    "name": "invoice_fields",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "invoice_number": {"type": "string"},
            "invoice_date": {  
                "type": "string",
                "format":"date",
                "description": "Invoice date"
            },
            "company_name": {"type": "string"},
            "total_due": {
                "type": "number",
                "description": "Total due"
            }
        },
        "required": ["invoice_number", "invoice_date", "company_name", "total_due"]
    },
    "strict": True
}

response = client.responses.create(
    input=[        
        {
            "role": "user", 
            "content": 
         [
         {
                  "type": "input_text",
                  "text": "Read the invoice and return ONLY the requested fields."
          },
          {
                  "type": "input_file",
                  "file_id": f.id,
              }
         ]}
    ],
    response_format={
        "type": "json_schema",
        "json_schema": invoice_schema
    },
    max_output_tokens=10000,
    temperature=0.7,
    model="gpt-5-chat"
)

print(response.output_text)
