# Pools and Providers

## Learning objectives

By the end of this lesson, you will be able to:

- Construct the logical hierarchy of Workforce Identity: Organization to Pool to Provider.
- Create a Workforce Identity Pool using the Google Cloud Console.
- Apply naming conventions and session duration settings that balance security with user experience.

## The Workforce Pool: the container

Before you click any buttons, you need to understand where these resources live.

### Required Roles

You will require the IAM role of **IAM Workforce Pool Admin**, assigned at the organization level.

### The Structure

- **Google Cloud Organization**: The top-level resource for Google Cloud, where Workforce Pools are created.
- **Workforce Pool**: A group of users who may log in from one or multiple external groups. Think of this as a "User Directory" for external people.
- **Provider**: The specific connection inside the Pool (such as the Okta connection, or the Entra ID connection).

### The metaphor

If Google Cloud is a university campus consisting of many secured buildings:

- Each **Pool** is a building on campus (buildings with classrooms, the teaching hospital, the research labs, the dorms).
- Each **Provider** is a door into this pool. (Students have Student IDs, security officers have Security credentials, healthcare workers have their own credentials, and so on).
- Once they are in the building (Pool) people with certain attributes (for example, staff) can access the staff lounge regardless of which type of Badge (Provider) they used.

### A Globally Unique ID

Workforce Pools are global resources, and therefore must have globally unique names across all customer organizations. The ID must be 4-32 characters, and may contain letters, numbers, and hyphens. The prefix gcp- is reserved for use by Google.

## Step-by-Step: Creating the Pool

Let's apply this to the GlobalTech scenario. You need a place for your PartnerCorp developers to land.

In this walkthrough, you learn how to navigate to IAM & Admin in the Google Cloud console to configure organization-level Workforce Identity Pools and create Workforce Identity Providers.

1. **Navigate to Workforce Identity Federation:** In Google Cloud Console, select your organization node and navigate to **IAM & Admin** > **Workforce Identity Federation**.
2. **Create a Workforce Pool:** Click **Create Pool**. Enter a Pool ID (e.g., `partner-pool`), Display name, and optional description. Configure session duration limits.
3. **Add a Provider:** Open the pool details and click **Add Provider**. Choose your protocol (**OpenID Connect (OIDC)** or **SAML 2.0**).
4. **Configure IdP Details:** Enter the Provider ID, Issuer URL or Metadata XML, Client ID, and relevant secret keys.
5. **Configure Attribute Mapping:** Map IdP assertion claims to Google Cloud attributes (such as `google.subject` and `google.groups`).
6. **Review and Save:** Verify the configuration and click **Submit** to activate the pool and provider.

You now have an empty Pool. It has no "Doors" (Providers) yet, so nobody can enter, but the structure exists.

## Critical Concept: Multi-Provider Pools

You might ask: Why not just make a new pool for every partner?

You can, but the power of the **Pool** is **Aggregation**.

Imagine GlobalTech hires three different design agencies. They all use different IdPs (One uses Okta, one uses Ping, one uses Entra ID).

- You create **one** pool called creative-agencies.
- You add **three** providers inside it.
- You write **one** IAM Policy: "Allow members of creative-agencies to view the Design Storage Bucket."

If you had three different pools, you would have to write and maintain three different IAM policies. **Group by function, not just by source**.

## Summary

You have built the "Lobby" (`partner-pool`). Now you need to unlock the door.

In the next lesson, you will configure the **Identity Provider (IdP)**. Since you decided in Module 1 to use **OIDC** for Okta, you will focus on that integration. After that, you will touch on **SAML** for completeness.
