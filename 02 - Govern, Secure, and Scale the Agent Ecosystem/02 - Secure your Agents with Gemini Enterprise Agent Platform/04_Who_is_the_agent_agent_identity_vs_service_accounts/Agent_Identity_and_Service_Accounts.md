# Agent Identity and Service Accounts

---

Every request an agent sends to a Google Cloud service carries a credential. That credential determines what the service allows the agent to do and what an attacker can do if they obtain it.  

Choosing the wrong credential model undermines every other security control because identity is the layer all the others depend on.  

The traditional approach is to attach a service account to the compute resource that runs the agent. Service accounts are familiar and well-supported, but they have three structural problems that become serious at an agentic scale, which we will discuss in this lesson.

Why service accounts are not the best choice for agents

Service accounts are essential for managing application identities and permissions within cloud environments. However, service accounts are not the best choice for agents.

- **Susceptibility to Excess Permissions**  
Least privilege is recommended but not enforced, so scope tends to become broader than needed. For an agent controlled by untrusted input, every excess permission grants additional power that an injection can exploit.
- **Lifecycle Decoupled From the Workload**  
A service account is not removed when the workload it serves is terminated. Without deliberate cleanup, unused identities remain: extra credentials to govern and audit, difficult to track.
- **Long-Lived Keys When Exported**  
Service accounts can use downloaded keys: long-lived static secrets that stay valid until manually rotated, so a leak into an image, environment variable, or log line is usable until then. (Google recommends short-lived tokens instead.) The pattern: service accounts permit insecure setups; the next lesson's Agent Identity makes the secure posture the default.

Agent Identity (SPIFFE)

Agent Identity resolves the three weaknesses with a fundamentally different model: instead of borrowing a service account, the agent in Agent Platform is a **first-class identity**, issued a cryptographic credential tied to its lifecycle.

This lesson explains what that identity is, the properties that make it secure, and how you enable it.

![Image](confidential.png)

Agent Identity Properties

When you deploy an agent to Agent Runtime with an Agent Identity, the platform issues a SPIFFE ID, which is a unique machine identity backed by a short-lived X.509 certificate (an SVID) and authenticated with mutual TLS.

The identity is provisioned automatically as part of deployment, so there's no key to generate, store, or rotate.

Each of the following properties maps directly to a service-account weakness mentioned earlier.

Click the items to learn more.

### Certificate-bound

The identity is tied to a short-lived certificate, so a credential extracted from a compromised container is useless outside the agent's authorized runtime context; this defeats the static-key problem.

### Lifecycle-tied

The identity is created when the agent is deployed and automatically revoked when the agent is deleted, so there are no residual credentials to audit; this defeats the lifecycle-drift problem.

### Unique and non-impersonable

Each deployment gets its own SPIFFE ID, so IAM policies can be precise, and no developer or workload can mint a key to impersonate the agent; this is the foundation for the least-privilege bindings in the next lesson.

When you deploy an agent to Agent Runtime, add the **identity\_type** parameter in the config to automatically create a SPIFFE based Agent Identity.
