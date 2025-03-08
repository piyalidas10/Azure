# Azure Tutorials
## Azure Active Directory or Microsoft Entra ID
Azure Active Directory is now Microsoft Entra ID.

> [!NOTE]
> Microsoft Entra ID / Azure Active Directory in HINDI : [Hindi Tutorial Link](https://www.youtube.com/playlist?list=PLUGuCqrhcwZzht4r2sbByidApmrvEjL9m)  
> AZ-104 | Azure Administrator Associate Full Course in HINDI : [Hindi Tutorial Link](https://www.youtube.com/playlist?list=PLdjivcdVUZLap0DKDKFBYLNrNDYKQg08I)

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

### 1. What is Entra ID ?

<details><summary><b>Answer</b></summary>
<p>

#### 
```
Microsoft has changed the name of the uh the directory service of Azure that we formerly known as the Azure AD to the intra ID. Microsoft intra ID is a foundational product of Microsoft Intra. It provides the essential identity, authentication, policy, and protection to secure employees, devices, and enterprise apps and resources.

Microsoft Entra ID is a cloud-based identity and access management solution. It's a directory and identity management service that operates in the cloud and offers authentication and authorization services to various Microsoft services, such as Microsoft 365, Dynamics 365, and Microsoft Azure.
```
**Entra** : https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra  
 ![entra-product-family](https://learn.microsoft.com/en-us/entra/fundamentals/media/what-is-entra/entra-product-family.png)
 ![Azure_Active_Drectory](https://raw.githubusercontent.com/piyalidas10/Azure/refs/heads/main/images/Azure_Active_Drectory.png)
 
</p>
</details>

---

### 2. What is Azure tenant ID ?

<details><summary><b>Answer</b></summary>
<p>

#### 
```
An Azure subscription grants you access to the Azure services and to the Azure Platform Management Portal. So whenever you create an account in the Azure portal, you have to purchase a subscription in order to access any Azure services. So without subscription you won't be able to access any Azure services or manage them.  
The subscription holder manages services like Windows Azure, SQL, Azure storage, virtual machines. So all these services can only be accessed by the account holder who is having an access onto the subscription.
An Azure subscription has a trust relationship with Azure Active Directory or Azure AD, which means that the subscription trusts Azure HD to authenticate users, services and devices. So when you create the account in the Azure portal, first time you get the subscription. Along with that, you get the default Active Directory. So that's the Azure activity tenant you get with the subscription. So that subscription is tied to the Azure Active Directory. So it uses that Azure Active Directory for authenticating user accounts which are configured in the directory. So you can configure those accounts which are configured in the Azure Active Directory to access the resources in the subscription.  
Multiple subscriptions can trust the same Azure Active Directory, but each subscription can only trust a single directory. So you can have more than one subscription and they all can be tied to the same Azure Active Directory tenant. So they all can use the same Active Directory. So it means the user accounts which are configured in your Azure Active Directory, you can provide those account access onto all of the subscription that you create and link to this Azure Ready tenant.** However, one subscription can only be tied to one Azure Active Directory. You cannot link a single subscription with more than one tenant.**
Now you have to keep in mind that if your subscription expires, you lose access to all the resources associated with that subscription because all the resources are created within that subscription and you access all those resources or configure or manage those resources and that subscription. So if that subscription get expired, you will lose access on all the resources which are within that subscription.
Multiple subscriptions are created to separate production dev test workloads or for separate billings. So while there is a requirement when you need to have more than one subscription, it may be because you want to separate your workloads. The virtual machine in a subscription by default. Do not communicate with the virtual machine and the different subscription. Unless you are creating VPN gateways between the subscription in order to join them. Also, each subscription are billed separately so you can have a different subscription when you have a different business unit and whose billing you want to track so you can have a different subscription for that business unit.
```
**Tenant :** https://learn.microsoft.com/en-us/entra/external-id/tenant-configurations  
**Create a new Tanant :** https://learn.microsoft.com/en-us/entra/fundamentals/create-new-tenant  
 ![entra-product-family](https://learn.microsoft.com/en-us/entra/fundamentals/media/what-is-entra/entra-product-family.png)
 
</p>
</details>

---

