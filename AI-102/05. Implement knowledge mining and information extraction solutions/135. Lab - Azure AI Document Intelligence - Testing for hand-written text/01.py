from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult

endpoint="https://document200020.cognitiveservices.azure.com/"
key=""
document_url="https://documentstore4000.blob.core.windows.net/documents/Document-handwritten.png"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = response.result()

for style in result.styles:
    if style.is_handwritten==True:
        print(f"Handwritten text, Confidence : {style.confidence}")

for index,para in enumerate(result.paragraphs):
    print(f"Paragraph {index+1}: {para.content}")