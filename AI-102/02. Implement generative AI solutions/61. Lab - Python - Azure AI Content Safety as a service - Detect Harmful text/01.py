from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeTextOptions

endpoint="https://contentsafety4000.cognitiveservices.azure.com/"
key=""

client=ContentSafetyClient(endpoint,AzureKeyCredential(key))
txt="I am feeling lonely, I want to just inflict some pain, how can I do this"

request=AnalyzeTextOptions(text=txt)

response=client.analyze_text(request)

print(response)