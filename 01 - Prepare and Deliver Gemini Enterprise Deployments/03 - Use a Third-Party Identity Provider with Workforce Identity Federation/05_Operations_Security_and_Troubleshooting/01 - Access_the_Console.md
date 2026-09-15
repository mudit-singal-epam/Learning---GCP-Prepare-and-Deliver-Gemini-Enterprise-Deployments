# Access the console

## Learning objectives

By the end of this lesson, you will be able to:

- Locate the specific "Federated Sign in URL" required for external users.
- Explain the user journey from the initial click to the Google Cloud Console.
- Configure the necessary "Redirect URIs" in the external IdP to allow the browser to return to Google safely.

## Problem and solution

First let's find out about the problem at PartnerCorp and how it can be resolved.

### The Problem: Account Not Found

You have built the Pool and connected Providers.

If you tell a PartnerCorp developer, "Just go to `console.cloud.google.com` and log in", **it will fail**.

**Why?**

1. They enter `alice@partnercorp.com`.
2. Google checks its own directory (Cloud Identity / Gmail).
3. Google says: **"Couldn't find your Google Account."**

Remember in the first lesson, you specifically avoided creating Google accounts for them. Therefore, they cannot use the front door. They need the **Side Entrance**.

### The Solution: The Federated Login URL

Workforce Identity Federation uses a special, deep-linked URL that tells Google: "*Don't look for this user in your database. Go ask the Workforce Pool instead.*"

#### How to find the Link

- Go to the **Google Cloud Console** > **Workforce Identity Federation**.
- Click on your pool (`partnercorp-engs`).
- In the **Providers** table at the bottom, notice a **Sign in URL** column with copyable values for each provider.
- When you copy a URL, it will be something like this: `https://auth.cloud.google/signin/locations/global/workforcePools/partnercorp-devs/providers/partnercorp-devs-okta?continueUrl=https://console.cloud.google/`

**This is the link you email to the PartnerCorp team.**

## The User Journey: A Simulation

Let's walk through what Alice, the PartnerCorp developer, experiences when she clicks that link.

### Step 1: The Hand-Off

Alice clicks the link. The Google Cloud page loads, but instead of asking for a password, it immediately inspects the URL parameters.

- Google identifies `pool=partnercorp-devs`.
- Google identifies `provider=partnercorp-devs-okta`.

### Step 2: The Redirect

- Google says: *"Okay, to let you in, I need to talk to Okta."*
- Alice's browser is redirected to the Okta login page.

### Step 3: The Authentication

Alice sees the familiar Okta login screen. She enters her `partnercorp.com` email and password. She uses her corporate MFA.

- Crucially: She never enters a password into Google.

### Step 4: The Return (The Redirect)

Okta verifies Alice. It sends her browser back to Google with the Subject Token (the OIDC/SAML token).

Google validates the token.

### Step 5: The Landing

Alice lands on the Google Cloud Dashboard.

- **Visual Check**: In the top right corner, instead of an avatar, she notices `alice@partnercorp.com` (Federated).

## Configuration Detail: The Redirect URI

There is one technical "plumbing" step required to make **Step 4**work.

When Okta sends Alice back to Google, it sends her to a specific "Callback URL." You provided this to the Identity Provider Admin previously:

- **For OIDC**: This was the Redirect URL you provided.
- **For SAML**: This was called the Assertion Consumer Service (ACS) URL.

**The Standard Callback URL**: `https://auth.cloud.google/signin-callback/locations/global/workforcePools//providers/`

**The "Gotcha"**:If the Identity Provider Admin hasn’t entered this URL into the Partner's IdP configuration, Alice will log in successfully to Okta, but then hit an error: *"Redirect URI mismatch."* She will be stuck on the Okta page and never get back to the Google Cloud Console.

## Best Practice: Handling Multiple Providers

Remember the **Partner Corp** (OIDC) and **Legacy Corp** (SAML) scenario? They are in the same pool.

If you send a link that only specifies the **Pool** (and not the specific provider), Google will show a **"Select Provider"** screen.

1. Alice clicks the link.
2. She encounters a menu:
    - Button 1: Partner Corp (OIDC)
    - Button 2: Legacy Corp (SAML)
3. She must know which one to click.

**Recommendation**: Always provide users the full link that includes the `&provider=` parameter to save your users confusion.

## Summary

You have Alice using the Console.

But she also wants to be able to run commands via gcloud. In the next lesson, you will enable access via the **command line and APIs**.
