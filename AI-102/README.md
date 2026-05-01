# AI-102

# Tutorials
1. AI-102 :: Microsoft Certified: Azure AI : https://www.youtube.com/playlist?list=PL5TTTZj-297kpBTOQqYM3AuvZz5tBr2Dq
2. Microsoft Certified: Azure AI Engineer Associate : https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/?practice-assessment-type=certification
3. AI-102 Microsoft Azure AI Engineer | Practice Question and Answers | Pass Microsoft AI-102 Exam : https://www.youtube.com/watch?v=IBQwsLkrz5w
4. Microsoft Foundry (classic) portal documentation : https://learn.microsoft.com/en-us/azure/foundry-classic/

## Microsoft Azure - Cognitive Services
1. https://www.geeksforgeeks.org/devops/microsoft-azure-cognitive-services/
2. 

## Accounts - Regenerate Key
1. https://learn.microsoft.com/en-us/rest/api/aiservices/accountmanagement/accounts/regenerate-key?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP

### Azure AI Foundary Portal
> A One Stop Shop where you can use Azure, OpenAI as well, and you can use other Azure AI services as well.

> A unified platform where you can develop your AI based application as well, and you can use other Azure AI services as well, for example, language service, speech service, content safety.

## 🔐 Regional API Endpoint vs Custom Subdomain API (Azure OpenAI)

🌍 1. Regional API Endpoint (default)
--------------------------------------------------------------------------
👉 Format:
```
https://<region>.api.cognitive.microsoft.com/
```
Example:
```
https://eastus.api.cognitive.microsoft.com/
```

**✅ Used for:**
- API Key authentication
- Simple apps / testing
- Quick integrations

**⚙️ How it works:**
- Shared regional endpoint
- You pass API key in header

**❌ Limitations:**
- No Entra ID (AAD) auth
- Not ideal for enterprise security
- Harder to isolate per resource

🏷️ 2. Custom Subdomain API (recommended)
--------------------------------------------------------------------------
👉 Format:
```
https://<your-resource-name>.openai.azure.com/
```
Example:
```
https://my-openai-prod.openai.azure.com/
```

**✅ Used for:**
- Entra ID (AAD) authentication 🔐
- Private networking (VNet, Private Endpoint)
- Production systems

**⚙️ How it works:**
- Dedicated endpoint for your resource
- Supports:
  - Token-based auth
  - RBAC
  - Managed Identity

| Feature          | Regional Endpoint | Custom Subdomain   |
| ---------------- | ----------------- | ------------------ |
| URL type         | Shared            | Dedicated          |
| Auth             | API Key only      | API Key + Entra ID |
| Security         | Basic             | Enterprise-grade   |
| Private Endpoint | ❌ Not supported  | ✅ Supported        |
| Recommended      | ❌ No             | ✅ Yes (production) |


**Key Differences Comparison**
+ Uniqueness: Regional endpoints (e.g., https://eastus.api.cognitive.microsoft.com) are common to all customers in that region, whereas custom subdomains (e.g., https://my-unique-resource.openai.azure.com) are unique to your individual resource.
+ Authentication: Custom subdomains are a prerequisite for using Microsoft Entra ID for authentication and Role-Based Access Control (RBAC). Regional endpoints primarily rely on API keys.
+ Networking: You must use a custom subdomain to enable Azure Private Link and Private Endpoints. This ensures your API traffic stays entirely within the Azure backbone and never traverses the public internet.
+ Availability: Resources created after July 2019 automatically use custom subdomains by default, though regional endpoints remain supported for backward compatibility in most cases.

**Security Benefits of Custom Subdomains**
+ Managed Identities: Allows you to eliminate hardcoded API keys by using system-assigned or user-assigned Managed Identities.
+ Network Isolation: Enables private connectivity via Private Endpoints, which significantly reduces the attack surface compared to public regional endpoints.
+ Auditability: Because the endpoint is unique to your resource, it is easier to track and monitor traffic specifically for your application through Azure Monitor.

**How to Use a Custom Subdomain**
+ Creation: When creating an Azure OpenAI resource in the Azure Portal, you are typically prompted to provide a unique name which forms the subdomain.
+ Migration: For older resources, you can go to the Overview section of your resource and select Generate Custom Domain Name.
+ SDK Integration: In your code (e.g., Python), you replace the base regional URL with your full custom subdomain URL in the azure_endpoint parameter.

