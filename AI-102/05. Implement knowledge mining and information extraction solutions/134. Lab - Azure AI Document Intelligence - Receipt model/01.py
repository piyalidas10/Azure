from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult

endpoint="https://document200020.cognitiveservices.azure.com/"
key=""
document_url="https://documentstore4000.blob.core.windows.net/documents/Sample Receipt.pdf"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-receipt",AnalyzeDocumentRequest(url_source=document_url))

result = response.result()

for index,receipt in enumerate(result.documents):
    print(f"Merchant Name {receipt.fields.get("MerchantName").get("valueString")}")
    print(f"Total {receipt.fields.get("Total").get("content")}")
    print(f"Transaction Date {receipt.fields.get("TransactionDate").get("valueDate")}")