Invoke-WebRequest -Uri "https://contentsaefty600909.cognitiveservices.azure.com/contentsafety/text:analyze?api-version=2024-09-01" `
  -Method POST `
  -Headers @{
    "Ocp-Apim-Subscription-Key" = "EQ7DgvOVKjzQrQ3Ht73lVeLQ6lVik8JZCBvL4MibPAnLlekNnSV7JQQJ99BGACYeBjFXJ3w3AAAHACOGjkf2";
    "Content-Type" = "application/json"
  } `
  -Body '{"text":"Think of inducing drugs into the person","categories":["Hate","Sexual","SelfHarm","Violence"]}'
