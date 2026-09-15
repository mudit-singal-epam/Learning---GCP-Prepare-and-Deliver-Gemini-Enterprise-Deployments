# CLI and API access

## Learning objectives

By the end of this lesson, you will be able to:

- Explain how the `gcloud` CLI authenticates using Workforce Identity Federation (WIF) without a browser.
- Generate the `configuration.json` file required for headless authentication.
- Execute a login command that utilizes external credentials instead of a standard Google user account.

## Scenario: The Headless Runner

Alice (your PartnerCorp Lead) is happy with the Console access. But now she asks:

> *"I have a Python script that uploads huge datasets to Cloud Storage. I run it from my laptop terminal. How do I authenticate? I don't have a Service Account key."*

If Alice tries `gcloud auth login`, it pops up a browser asking for a Gmail address. She doesn't have one.

You need to teach the `gcloud` tool how to speak **Workforce Identity**.

## The Key Component: The Configuration File

Unlike a standard user who just types their email, a WIF user needs a "map" that tells the CLI where to go (the Issuer URL, the Client ID, the Pool ID).

This map is a JSON file.

**You (The Admin) must generate this file for your users.**

### Step 1: Generate the Config

You can create this file using the CLI:

```bash
gcloud iam workforce-pools create-login-config \
    locations/global/workforcePools/partnercorp-engs/providers/partnercorp-engs-oidc \
    --output-file=login_config.json
```

The created file will be used to give gcloud the information it needs to use this Workforce Pool and Provider. It looks like this:

```bash
{
  "universe_domain": "googleapis.com",
  "universe_cloud_web_domain": "cloud.google",
  "type": "external_account_authorized_user_login_config",
  "audience": "//iam.googleapis.com/locations/global/workforcePools/partnercorp-engs/providers/partnercorp-engs-oidc",
  "auth_url": "https://auth.cloud.google/authorize",
  "token_url": "https://sts.googleapis.com/v1/oauthtoken",
  "token_info_url": "https://sts.googleapis.com/v1/introspect"
}
```

#### Breakdown of the command

- `create-login-config`: The magic command.
- The Long String: The full resource path to the **Provider** (not just the Pool).
- `--output-file`: Where to save the JSON "map".

### Step 2: Distribute the File

You email this `login-config.json` file to Alice. It contains no secrets—only configuration data (URLs and IDs). It is safe to share internally.

## The User Experience: Logging In

Now, switching roles to **Alice** on her laptop.

She saves the file to her home directory. To log in, she runs:

```bash
gcloud auth login --login-file=~/login-config.json
```

### What happens next?

1. The CLI reads the file.
2. It identifies that this is an OIDC provider.
3. It opens a browser window to **Okta** (not Google).
4. Alice logs in to Okta.
5. Okta passes the token back to the local CLI.
6. `gcloud` exchanges it for a Google Access Token.

### Result

Alice receives:

```bash
Authenticated with external account authorized user credentials for: [principal://iam.googleapis.com/locations/global/workforcePools/partnercorp-engs/subject/00uxtl72q9F6xbe1o697].

Your current project is [current-project-id].  You can change this setting by running:

 $ gcloud config set project PROJECT_ID
```

She can now set a project and then run commands like `gsutil cp huge-file.dat gs://my-bucket` successfully.

## Advanced: Headless / CI/CD Mode

What if Alice wants to run this on a Jenkins server or GitHub Action where there is **no browser** to pop up?

Workforce Identity supports **Headless** flows, but it requires the environment to have a recent file-based OIDC credential (like a generic OIDC token saved to disk). You can read more about this in the Documentation for a given provider, for example the documentation covering [sign-in methods for Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#sign_in).

**Note**: This is an advanced topic, but it's important to know that **Workload**Identity Federation (not **Workforce**Identity Federation) is the standard way to auth GitHub Actions to Google Cloud (via Workload Identity).

## Summary

- You have Alice using the Console and the CLI.
- But suddenly, at 3:00 PM, she gets an "Access Denied" error.
- She calls you. "I didn't change anything!"

How do you investigate? In the next lesson, you become Detectives. You will dive into **Cloud Logging** to trace the failures in the authentication handshake.
