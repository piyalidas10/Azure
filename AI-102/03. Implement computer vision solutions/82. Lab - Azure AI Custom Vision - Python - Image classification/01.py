
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

endpoint="https://customvision2000-prediction.cognitiveservices.azure.com/"
key=""

credentials = ApiKeyCredentials(in_headers={"Prediction-key": key})
prediction_client = CustomVisionPredictionClient(endpoint=endpoint,
                                                 credentials=credentials)

image_data=open("img1.jpeg",mode="rb").read()
projectid="d6de4719-8433-4936-8a4a-e25b9a0c21a2"
model_name="PetModel"

response=prediction_client.classify_image(projectid,model_name,image_data)

for prediction in response.predictions:
    print(prediction)