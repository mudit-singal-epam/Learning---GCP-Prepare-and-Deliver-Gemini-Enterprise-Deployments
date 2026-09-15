# Compare OIDC and SAML Protocols

## Learning objectives

By the end of this lesson, you will be able to:

- Compare the two primary protocols supported by Workforce Identity Federation: SAML 2.0 and OpenID Connect (OIDC).
- Identify the data formats associated with each (XML and JSON).
- Select the appropriate protocol based on the capabilities of the external Identity Provider (IdP).

## The Concept: Choosing the Language

In the previous lesson, you learned that the IdP sends a "Subject Token" to Google. But what format is that token in?

To make Federation work, Google and the Partner must agree on a common language. Workforce Identity Federation is bilingual. It speaks:

- **SAML 2.0** (The Enterprise Veteran)
- **OIDC** (The Modern Standard)

In general OIDC is recommended as the modern standard, if the identity provider supports it.

OIDC is generally preferred today because it eases key rotation and provides other convenient features.

For example, if an Okta application rotates its signing keys, Google WIF can pick up the new public key automatically. With SAML, you might have an outage until you upload the new certificate.

Additionally, suppose a user has a field updated within Okta, WIF integration using OIDC can provide these updated fields to Google IAM the next time the user logs in. If WIF integration uses SAML, the user may need to be removed and re-added to the Okta application for user field updates to be shared downstream to Google IAM during authentication.

### **Comparison**

| Feature | SAML 2.0 | OpenID Connect (OIDC) |
| :--- | :--- | :--- |
| **Data Structure** | XML (older format) | JSON (newer standard) |
| **Trust Setup** | Uploading a Static XML Metadata file which contains a public key. | Built on top of OAuth 2.0. Dynamically fetches keys from a dynamic "Discovery URL" (.well-known). |
| **How User Updates are Handled** | Users may need to be deleted and recreated in the Identity Provider application for updates on users (like a department change) to transfer. | Updates to users should automatically transfer. |
| **Key Rotation** | Hard: If the Partner changes their certificate, you must manually upload the new one to Google. | Easy: Google automatically checks the URL for new keys. |
| **Debugging** | You can debug in the browser directly using Chrome Developer Tools or a plugin. | You need to intercept the token and paste it into a debugger (like jwt.io) to read it. |
| **Industry Trend** | Stable / Declining | Growing / Standard |

### **The GlobalTech Decision**

Back to the scenario. You are setting up the pool for PartnerCorp.

**Partner**: "We use Okta."

**You**: "Great. We prefer OIDC because it automates certificate rotation, meaning less maintenance for us later. Here is our Redirect URI. Please provide your Issuer URL, Application (Client) ID, and Client Secret."

*Note: You will configure this specifically in Module 2.*

## Summary

Congratulations! You have completed this module on Foundations and Architecture.

- You learned that WIF allows you to trust external identities without creating Google accounts.
- You learned that WIF is essentially a Currency Exchange (STS) converting Subject Tokens to Access Tokens.
- You learned the difference between the XML-based SAML and the JSON-based OIDC.

In the next module you open the Google Cloud Console. You will act as the administrator and build the infrastructure you have just learned about. You will start by creating the Workforce Identity Pool.
