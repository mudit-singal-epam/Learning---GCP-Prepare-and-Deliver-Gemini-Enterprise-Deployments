# Attribute conditions (the guardrails)

## Learning objectives

By the end of this lesson, you will be able to:

- Construct Boolean CEL expressions to enforce specific entry criteria for external users.
- Analyze the security benefits of filtering users at the "Pool Entry" level versus the "IAM Policy" level.
- Troubleshoot common logic errors involving case sensitivity and missing claims.

## The Concept: The Bouncer

Imagine your Workforce Pool is a construction job site.

- **Authentication (IdP)**: Checking the ID card to make sure it's real.
- **Attribute Mapping**: Writing a name tag for the guest.
- **Attribute Condition**: The Gatekeeper.

Even if the ID is real, and you can write a name tag, the Gatekeeper might say: *"Sorry, you don’t have the safety certification to enter this job site."*

In technical terms, an **Attribute Condition** is a logic check that runs after the token is verified but **before** access is granted. If the condition evaluates to **False**, the login fails immediately.

## The Syntax: Boolean logic

Unlike Attribute Mapping (which was `Left = Right`), Attribute Conditions must result in a **True/False** answer.

You continue to use [CEL (Common Expression Language)](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel#string-manipulation-operators), which includes:

| Logical operators | Description | String manipulation operators | Description |
| :--- | :--- | :--- | :--- |
| **==** | Equals | **.contains()** | For lists or substrings |
| **!=** | Does not equal | **.matches() or ==** | For equality |
| **&&** | AND | **.startsWith()** | For matching the start of the string |
| **\|\|** | OR | **.endsWith()** | For matching the end of the string |
| | | **.lowerAscii()** | To lowercase a string |
| | | **.upperAscii()** | To uppercase a string |

## The GlobalTech Scenario: Tightening the Perimeter

Let's review the PartnerCorp requirements again.

**Risk**: PartnerCorp has 10,000 employees. You only want the **500 developers** to access your pool. You don't want their Sales or HR teams cluttering your logs or potentially finding accidental access.

### The Policy Requirements

1. User must be from `partnercorp.com` (No personal Gmails).
2. User must be in the `Engineering` department.
3. User's email must be **verified** (A security best practice).

```bash
assertion.email.endsWith('@partnercorp.com') &&
assertion.department.lowerAscii() == 'engineering' &&
assertion.email_verified == true
```

### How it executes

- **Alice (Dev)**: `True && True && True` results in **ACCESS GRANTED**.
- **Bob (Sales)**: `True && False && True` results in **ACCESS DENIED**.
- **Eve (Hacker with fake email)**: `True && True && False` results in **ACCESS DENIED**.

## Critical Thinking: Why filter here?

You might ask: *"Why not just let everyone in, but only give IAM permissions to the Engineering group?"*

This is the principle of **Defense in Depth**.

### Reduced Blast Radius

If someone else later grants **Viewer** access to all users of the Pool (it happens), having a Condition prevents Bob from Sales from seeing your data. He never becomes an "Authenticated User" in your pool.

### Cleaner Audit Logs

Your Cloud Logging isn't filled with noise from irrelevant users.

### Cost Management

You prevent unnecessary token exchanges.

## Common Pitfalls

### The Case Sensitivity Trap

CEL is strictly case-sensitive.

- Condition: `assertion.department == 'engineering'`
- Incoming Claim: `Engineering` (Capital E)
- Result: `False`. Access Denied.
- The Fix: Normalize the string.
`assertion.department.lowerAscii() == 'engineering'`

### The Missing Claim

What if PartnerCorp's IdP forgets to send the `department` field for a specific user?

- The expression tries to read `assertion.department`.
- It finds `null`.
- The logic crashes.
- **Result**: Access Denied (Fail Closed).
  - **Note**: This is good for security, but confusing for debugging.
- **The Fix**: Ask the Identity Provider Admin to ensure expected values are present.

### The List Or String

If `assertion.groups` is a list (array) `['admin', 'dev']`:

- **Wrong**: `assertion.groups == 'dev'` (A list is not equal to a string).
- **Right**: `assertion.groups.contains('dev')`

## Summary

You have successfully mapped Alice's attributes and verified she is allowed to enter the pool.

But right now, she is standing in the lobby. She has no keys to the server room. If she tries to list a Storage Bucket, Google responds with "403 Forbidden."

In the next lesson, you will perform the final step: **IAM Policy Binding**. You will connect your mapped attributes to actual Google Cloud Roles.
