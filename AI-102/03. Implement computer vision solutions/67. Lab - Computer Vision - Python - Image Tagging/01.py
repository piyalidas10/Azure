from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json

endpoint="https://vision40000.cognitiveservices.azure.com/"
key=""

client=ImageAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

with open("AzureAIVision-ImageTagging.png","rb") as image_file:
    image_details=image_file.read()

response=client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.TAGS]
)

print(json.dumps(response.as_dict(), indent=4))