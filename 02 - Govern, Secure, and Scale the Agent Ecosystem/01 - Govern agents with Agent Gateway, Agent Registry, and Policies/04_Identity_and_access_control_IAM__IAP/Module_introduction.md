# Module introduction

Identity and access control (IAM and IAP)

In this module, you'll explore the identity and access control (IAM) layers that define zero-trust governance in the AI era. In a legacy system, applications often run under over-privileged service accounts, which makes tracing anomalous actions difficult.

You'll learn how to configure unique, cryptographically verifiable mTLS personas for each agent runtime, and implement per-tool authorization using Identity-Aware Proxy (IAP) and the REQUEST\_AUTHZ gateway service extension.

Finally, you'll learn to write advanced Common Expression Language (CEL) conditions to restrict agents to specific actions based on metadata, guaranteeing strict adherence to the principle of least privilege.

![Image](CSS Graphic Crop (5).png)

By the end of this module, you'll be able to:

* Configure and deploy unique [Agent Identities](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) using mTLS.
* Implement per-tool authorization policies using the REQUEST\_AUTHZ extension.
* Author Common Expression Language (CEL) policies to enforce granular, condition-based access boundaries.
