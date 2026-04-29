from openai import AzureOpenAI
import base64

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://cloud-metks4fx-eastus2.cognitiveservices.azure.com/",
    api_key="",
)

with open("img1.png","rb") as image_file:
    image_details=base64.b64encode(image_file.read()).decode("utf-8")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant who helps to describe images.",
        },
        {
            "role": "user",
            "content": 
            [
                {
            "type":"text",
            "text":"Give me a description of the what the image is trying to explain"
                },
                {
                    "type":"image_url",
                     "image_url" :{
                        "url":f"data:image/png;base64,{image_details}"
                    }
                }
            ]
        }
    ],
    max_tokens=16384,
    temperature=0.7,
    top_p=1.0,
    model="gpt-5-chat"
)

print(response.choices[0].message.content)
