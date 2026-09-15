# Accountability and governance (Access transparency & dashboard)

### Heading

In this lesson, you'll learn how to configure [Access Transparency](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-transparency) and build custom **Authorization Debugging Dashboards** to maintain complete administrative control over your agent ecosystem. Compliance-heavy environments require strict tracking of every single entity that accesses their data, including cloud support personnel.

By implementing [Access Transparency](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-transparency), you'll log every manual action taken by Google Cloud engineers on your agent tenant projects. You'll also learn how to build a unified monitoring dashboard to track policy denials and resolve connectivity errors instantly.

Access transparency (AxT)

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

[**Access Transparency**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-transparency) provides cryptographic, auditable logs showing when and why Google personnel access your configurations or agent databases (e.g., during a support ticket troubleshooting call).

* **Compliance:** Helps meet strict regulatory frameworks (like HIPAA, FedRAMP, or GDPR) requiring audit trails for vendor support actions.
* **Scope:**[Access Transparency](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-transparency) covers the entire agent ecosystem, logging accesses to your VPCs, reasoning engines, gateways, and [Model Armor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor) configurations.

The authorization debugging dashboard

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

### Heading

To troubleshoot and manage agent egress traffic, you configure a custom dashboard in Cloud Monitoring. This dashboard consolidates signals into four critical widgets:

1. **Unregistered outbound blocks:** Tracks traffic blocked by the [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) because the destination hostname does not exist in the [Agent Registry](https://docs.cloud.google.com/agent-registry/overview). (These are blocked before reaching IAP, meaning no IAP audit logs are generated).
2. **Agent ➔ MCP server (403 Denials):** Counts request failures where the agent reached the tool, but IAP denied access because the [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) lacked appropriate roles.
3. **Traffic overview & IAP enforcement mode:** Displays all traffic patterns, highlighting if IAP is operating in DRY\_RUN mode (observing and auditing) or null/active mode (actively blocking traffic).
4. **Google Cloud API IAM denials:** Scans standard Cloud Audit Logs to catch underlying Google Cloud API permission errors when the agent tries to read from standard services like BigQuery or Cloud Storage.

![Image](Govern Agents - RISE Graphics (3).png)

### Google Cloud Best Practice

Always deploy your [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) with IAP Enforcement set to DRY\_RUN during the initial testing phase.

This allows you to validate that your agent discovers and successfully calls its tools while the Authorization Debugging Dashboard verifies that all IAM policies are constructed correctly without causing operational disruptions.

Once you confirm zero false positives in the logs, update the mode to null to enforce policies.
