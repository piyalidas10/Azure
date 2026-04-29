from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.textanalytics import TextAnalyticsClient

endpoint="https://document200020.cognitiveservices.azure.com/"
key=""

language_endpoint="https://language3000030.cognitiveservices.azure.com/"
language_key=""

document_url="https://documentstore4000.blob.core.windows.net/documents/sample_sentiment_sentences.pdf"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))
language_client=TextAnalyticsClient(endpoint=language_endpoint,credential=AzureKeyCredential(language_key))

response=client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult =response.result()
documents = []

for each_page in result.pages:
    for index,line in enumerate(each_page.lines):
        documents.append(line.content)

language_response=language_client.analyze_sentiment(documents=documents)

for result in language_response:
        print(f"Sentiment: {result.sentences[0].sentiment} - Sentence: {result.sentences[0].text}")