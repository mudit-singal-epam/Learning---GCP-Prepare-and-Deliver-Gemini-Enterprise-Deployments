# The identity challenge

## Learning objectives

By the end of this lesson, you will be able to:

- Articulate the specific use case for Workforce Identity Federation (WIF).
- Distinguish between Cloud Identity, Workload Identity, and Workforce Identity.

## The Scenario: The "GlobalTech" Merger

Welcome to your new role. You are a Cloud Architect at GlobalTech.

It is 9:00 AM on a Tuesday. Your CTO walks in with news: GlobalTech is partnering with PartnerCorp to build a new application.

- **The Requirement:** 500 PartnerCorp developers need immediate access to your Google Cloud projects to view logs and upload code.
- **The Constraint:** PartnerCorp uses **Okta** for their login. They do not have, and do not want, Google/Gmail accounts.
- **The Timeline:** They need access by Thursday.

### Your challenge: How do you grant the PartnerCorp developers access?

#### **The "old way" (the anti-pattern)**

In the past, you might have solved this by using **Google Cloud Identity (GCI)**.

- You create 500 new Google accounts (such as, `dev1@globaltech.com`) or use Google Cloud Directory Sync (GCDS) to keep the accounts in sync.
- If you create 500 new Google accounts then you would need to email the credentials to 500 people.

#### **Why this fails**

- **Security Risk**: If a developer leaves PartnerCorp, their Okta account is disabled, but their GlobalTech Google account might remain active (a "Zombie Account").
- **Overhead**: You are now managing the lifecycle of 500 extra users.
- **Cost**: Depending on your license, you might pay for these identities.
- **User Friction**: The developers hate it. They have to manage a second set of credentials and 2FA tokens.

#### **The Solution: Workforce Identity Federation**

To grant 500 new, external users from PartnerCorp access, Workforce Identity Federation is the preferred solution because it shifts from **Synchronization** (copying users) to **Federation** (borrowing trust).

Instead of creating a user in Google Cloud, you tell Google Cloud:

*"I trust PartnerCorp’s Okta for these 500 PartnerCorp developers. If PartnerCorp’s Okta says this developer is 'Jamie' and they are allowed to be here, let them in."*

##### **How it works (High Level)**

- The user logs in to their system (Okta, Microsoft Entra ID, Ping, and others).
- Their system gives them a "pass" (a token).
- They show that "pass" to Google Cloud.
- Google Cloud grants them temporary access to the console or API.

> Key Takeaway
>
> The identity remains external. Google only manages the permissions, not the user.

### Concept Distinction: Which "Identity" Solution?

Google Cloud has several similarly named services. Choosing the wrong one is a common architectural mistake.

You can use this table to provide clarity:

| Feature | Cloud Identity | Workload Identity Federation | Workforce Identity Federation |
| :--- | :--- | :--- | :--- |
| **Who is it for?** | **Internal Employees** | **Machines and Software** | **External Personnel** |
| **Primary Use Case** | Full-time staff who need G-Suite, Gmail, Drive, and Google Cloud. | AWS Lambda, GitHub Actions, On-premises servers needing Google Cloud access. | Employees without Google Workspace Identities, Partners, Contractors, Vendors using their own IdP. |
| **Mechanism** | Synchronization (Users exist in Google). | Token Exchange (No user creation). | Token Exchange (No user creation). |
| **User Experience** | Login with Google. | No UI (API and CLI only). | Login using "Federated" Console or CLI. |

## Analogy

Let's take an example of the potential services that would be used for a hospital:

- **Cloud Identity** is an employee badge.
- **Workforce Identity** is a visitor badge given because you showed your Driver's License (your external ID).

## Summary

Now that you understand why you need Workforce Identity Federation to solve the GlobalTech challenge, you need to understand the mechanics.

In the next lesson you will explore the **Token Exchange Flow**. You will trace exactly what happens to the data packets when an external user clicks "Login."
