from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

endpoint="https://vision40000.cognitiveservices.azure.com/"
key=""

client=ComputerVisionClient(endpoint,CognitiveServicesCredentials(key))
features = [VisualFeatureTypes.brands]

with open("brand.png","rb") as image_file:
    response=client.analyze_image_in_stream(image_file,visual_features=features)

for brand in response.brands:
   print(f"- {brand.name} (confidence: {brand.confidence:.2f}) at {brand.rectangle}")