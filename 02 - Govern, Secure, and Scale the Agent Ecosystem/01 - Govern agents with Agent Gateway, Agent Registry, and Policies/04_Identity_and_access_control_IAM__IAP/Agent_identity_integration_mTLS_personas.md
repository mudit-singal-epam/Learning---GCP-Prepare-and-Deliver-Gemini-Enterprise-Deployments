# Agent identity integration (mTLS personas)

### Heading

In this lesson, you'll learn how to transition from shared, high-privilege service accounts to per-agent [**Agent Identity**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity).

Letting multiple agents share a single identity makes auditing impossible and leaves your system vulnerable if one agent is compromised using prompt injection.

By deploying agents with unique mTLS personas, you will ensure that every model instance operates inside its own cryptographic boundary.

You'll learn how to provision these identities, assign them minimum required roles, and trace their actions in audit logs.

### Understanding the agent identity structure

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

### Heading

An [**Agent Identity**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) is a unique, Google-managed service principal that is auto-provisioned and tied to the lifecycle of a specific reasoning engine deployment.

* **Credential Management:** You do not manage private keys! The platform automatically provisions and rotates unique credentials for the agent, securing its outgoing traffic with end-to-end mutual TLS (mTLS).
* **Principal Format:** The identity surfaces in IAM in the following format: service-[PROJECT\_NUMBER]@[gcp-sa-aiplatform-re.iam.gserviceaccount.com](http://gcp-sa-aiplatform-re.iam.gserviceaccount.com)

**Effective Identity:** If an agent is deployed without an identity, it defaults to using the broad caller identity, which violates the security principle of least privilege.

### Assigning IAM boundaries

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

### Heading

Once an agent has a unique identity, you can grant it permissions to specific resources rather than the entire project.

* **Google Cloud APIs:** If the agent needs to read from a Cloud Storage bucket or run queries in BigQuery, you grant those specific roles (e.g., roles/storage.objectViewer) directly to the agent identity principal.
* **Enterprise Tools:** For internal tools hosted behind the [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview), the gateway's authorization layer verifies this principal against tool-specific policies.

### Heading

**Google Cloud Best Practice**   
Always configure your deployment scripts to enable [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) explicitly during the deployment phase. In python, instantiate your client with the v1beta1 API and set enable\_agent\_identity=True when building the deployment payload.
