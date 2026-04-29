from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult

endpoint="https://document200020.cognitiveservices.azure.com/"
key=""
document_url="https://documentstore4000.blob.core.windows.net/documents/Sample Invoice.pdf"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-invoice",AnalyzeDocumentRequest(url_source=document_url))

result = response.result()

for index,invoice in enumerate(result.documents):
    print(f"Customer Name {invoice.fields.get("CustomerName").get("valueString")}")
    print(f"Invoice ID {invoice.fields.get("InvoiceId").get("valueString")}")
    print(f"SubTotal{invoice.fields.get("SubTotal").get("content")}")