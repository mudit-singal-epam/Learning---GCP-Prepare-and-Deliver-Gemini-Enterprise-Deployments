# SCIM support for Gemini Enterprise

## Learning objectives

By the end of this lesson, you will be able to:

- Enable SCIM for Gemini Enterprise deployments

## The Scenario: Sharing NotebookLM notebooks

If your IdP supports [System for Cross-domain Identity Management (SCIM)](https://en.wikipedia.org/wiki/System_for_Cross-domain_Identity_Management), adding a SCIM tenant in your IdP application allows Gemini Enterprise users to share NotebookLM notebooks with a group using the group's name instead of its object ID (UUID). To learn more about sharing notebooks with groups, visit: [Share a notebooks with a group](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/share-notebooks#share-notebook-group).

Before creating a SCIM tenant, be sure to familiarize yourself with the limitations documented in the [SCIM support](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#scim) documentation.

> One important fact to understand is that you can only have one SCIM tenant in an organization, and if you delete a tenant without using the --hard-delete flag, you will initiate a 30-day soft-delete period.
>
> During this time, the tenant is hidden and cannot be used, and you cannot create a new SCIM tenant in the same workforce identity pool.

Specific instructions for enabling SCIM with Microsoft Entra ID are provided in the documentation [Configure SCIM for Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id#configure-scim). For other providers, refer to [Configure SCIM for Other OIDC / SAML providers](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#configure-scim).
