
from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://language4000.cognitiveservices.azure.com/"
key=""

client=ConversationAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

utterance="I need a double room for me and my family for the weekend"
project_name="TrainingProject"
deployment_name="TrainedDeployment"

response=client.analyze_conversation(
    task={
        "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": utterance 
                },
                "isLoggingEnabled": False
            },
            "parameters": {
                "projectName": project_name,
                "deploymentName": deployment_name
            }
    }
)

print(response)