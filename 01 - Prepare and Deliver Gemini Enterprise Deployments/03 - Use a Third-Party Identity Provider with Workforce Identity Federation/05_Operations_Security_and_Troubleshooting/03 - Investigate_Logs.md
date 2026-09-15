# Investigate Logs

## Learning objectives

By the end of this lesson, you will be able to:

- Construct Cloud Logging queries to isolate Workforce Identity events.
- Distinguish between a Token Exchange Failure (STS) and an IAM Authorization Failure (Permission).
- Locate the specific logic error when an Attribute Condition denies access.

## The Concept: The Black Box Recorder

Alice calls you: *"I tried to log in, and it just says 'Error: Authentication Failed'. Help!"*

The UI error message is intentionally vague for security reasons. To fix it, you need to view the Cloud Audit Logs.

There are two distinct systems you must audit, depending on when the error occurred:

1. **STS (Security Token Service)**: The "Front Door." Errors here mean the login failed.
2. **IAM (Identity & Access Management)**: The "Room Key." Errors here mean the login worked, but the user touched something they shouldn't.

## Step-by-step: Fixing the Token Exchange

If the user cannot get to the Console at all, the issue is in the Token Exchange.

### Auditing and Troubleshooting Workforce Identity Federation Logs

This shows how to enable Cloud Audit Logs for STS and investigate authentication and authorization events in Cloud Logging.

#### Step-by-Step Walkthrough

1. **Enable STS Audit Logs:** Go to **IAM & Admin** > **Audit Logs**. Search for **Security Token Service (STS)** and enable **Admin Read** and **Data Read** logs.
2. **Open Cloud Logging:** Navigate to **Logging** > **Logs Explorer**.
3. **Filter by Service:** Enter the query `protoPayload.serviceName="iam.googleapis.com" OR protoPayload.serviceName="sts.googleapis.com"`.
4. **Inspect Authentication Info:** Expand log entries to examine `protoPayload.authenticationInfo` and view the mapped subject, attributes, and STS token exchange response.
5. **Troubleshoot Errors:** Check for error codes such as `INVALID_ARGUMENT` (attribute condition failed) or `UNAUTHENTICATED` (signature or issuer mismatch).

## Troubleshooting

### WIF Attribute Condition Failure

This is a common error in WIF.

The user provides valid credentials, but your **Attribute Condition** rejects them.

- **The Query**: `protoPayload.serviceName="sts.googleapis.com"`
- **The Detail**: Check inside `protoPayload.status.message`.
  - It will explicitly state: `The given credential is rejected by the attribute condition.`

**Debugging Tip**: The log will not tell you which part of your condition failed (for example, it won't say "Department was wrong"). You must inspect the mapped attributes in the log entry to deduce what happened.

## The "Mapped Attributes" View

A hidden gem in Cloud Logging is viewing what attributes were actually mapped during the login.

In the STS logs of a successful login `(protoPayload.methodName: "SignIn")`, check for `protoPayload.metadata.mappedAttributes`.

It contains a JSON dump of the data the IdP sent.

```bash
"thirdPartyPrincipal": {
  "payload": {
    "sub": "alice-123",
    "job_role": "Intern",  <-- AHA!
    "email": "alice@partner.com"
  }
}
```

- **Scenario**: Alice swore she was an "Engineer."
- **The Log**: The log proves Okta sent her role as "Intern."
- **Resolution**: The problem isn't in Google. Alice needs to talk to her HR/IT department to update her Okta profile.

## Summary

You have fixed the errors. Alice is logged in, her attributes are correct, and she can access the bucket.

In the next lesson, you will cover **SCIM support for Gemini Enterprise**.
