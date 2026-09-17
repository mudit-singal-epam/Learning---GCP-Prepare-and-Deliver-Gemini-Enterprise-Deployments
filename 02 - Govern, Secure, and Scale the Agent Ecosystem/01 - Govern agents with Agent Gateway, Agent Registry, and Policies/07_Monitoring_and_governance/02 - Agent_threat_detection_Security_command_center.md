# Agent threat detection (Security command center)

In this lesson, you'll learn how to use [**Security Command Center**](https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview) to proactively detect security threats targeting your AI agent workforce.

Adversaries continuously attempt to find weaknesses in deployed models, hoping to exploit prompt injections or bypass network boundaries to access internal databases.

By enabling Agent Platform Threat Detection in SCC, you'll receive real-time alerts when malicious activity is detected.

You'll learn how to interpret these findings, configure alerts, and establish automated response playbooks to isolate compromised runtimes before threats can spread.

## Understanding Agent Platform threat detection

[**Security Command Center**](https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview) includes specialized threat detection engines tailored specifically for generative AI workloads:

* **Semantic Attack Detection:** Identifies sustained prompt injection attempts, jailbreak payloads, or jailbreak-style probing patterns across agent runtimes.
* **Egress Violations:** Triggers critical alerts if an agent runtime attempts to bypass the [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) or connect to unapproved IP addresses.

**Credential Misuse:** Flags anomalous usage of auto-provisioned [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) tokens (e.g., an agent identity token being used from a workstation IP outside the designated Google Cloud VPC).

## Responding to SCC security alerts

When SCC detects a threat, it generates a structured finding with details including the Agent ID, the project scope, the source IP, and the exact threat category (e.g., Adversarial Prompt Probing).

* **Automated Response:** You can configure Pub/Sub and Cloud Functions to trigger automated defense actions, such as immediately disabling the reasoning engine's runtime service account or pausing the session.

**Audit Logging:** Every finding is permanently archived in your [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview) log database for forensic review.

> [!Warning]
>
>Ensure that your organization has active organization-level SCC permissions.
>
> If SCC is only enabled at the project level, you'll miss critical organization-wide threat signals, such as an adversary attempting to orchestrate a distributed prompt attack across separate projects hosting different agents.
