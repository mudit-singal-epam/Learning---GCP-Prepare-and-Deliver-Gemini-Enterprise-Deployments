# Module introduction

---

Who is the agent: agent identity versus service accounts

In this module, you'll analyze how to establish robust machine identities for AI agents.

You'll explore the structural weaknesses of traditional service accounts in autonomous workloads and transition to using Agent Identity, which leverages short-lived, certificate-bound credentials.

You'll also examine how to enforce the principle of least privilege by binding specific IAM roles to individual agent identities rather than shared service accounts.

Finally, you'll implement Principal Access Boundaries to create a secondary layer of protection that limits the resources an agent can access even if IAM configurations are overly permissive.

![Image](CSS Graphic Crop (5).png)

By the end of this module, you'll be able to:

* Analyze the security limitations of traditional service accounts within the context of autonomous agentic workloads.
* Evaluate the security benefits of certificate-bound Agent Identity and SPIFFE-based authentication over static long-lived credentials.
* Apply least-privilege principles by binding precise IAM roles directly to unique agent identities.
* Implement Principal Access Boundary policies to establish deterministic enforcement ceilings that contain potential configuration errors.
