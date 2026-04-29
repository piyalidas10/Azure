from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeImageOptions,ImageData

endpoint="https://contentsafety4000.cognitiveservices.azure.com/"
key=""

client=ContentSafetyClient(endpoint,AzureKeyCredential(key))
with open("img1.jpg","rb") as image_file:
    request=AnalyzeImageOptions(image=ImageData(content=image_file.read()))

response=client.analyze_image(request)

print(response)