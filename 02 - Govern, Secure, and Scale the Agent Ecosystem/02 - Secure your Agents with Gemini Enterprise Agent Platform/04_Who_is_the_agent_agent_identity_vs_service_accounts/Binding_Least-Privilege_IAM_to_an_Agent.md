# Binding Least-Privilege IAM to an Agent

---

This lesson covers how to grant each agent exactly what its role requires, which is the credential-layer expression of the goal-bounding control (mentioned previously), and how a Principal Access Boundary (PAB) limits an identity even when an IAM policy is misconfigured.

A precise identity is only valuable if you bind precise permissions to it.

Permissions Per Identity

Bind roles directly to each Agent Identity rather than to a shared service account.

In the Warranty Claim System, the Data Agent’s Identity holds **roles/bigquery.dataViewer** on the specific warranty and sales datasets, no additional permissions.

No other agent has that permission, so if the Data Agent is compromised, the attacker can read warranty data but can't write to any table, call any external API, or reach any resource outside that binding.

Per-identity binding is what makes a compromise bounded: the potential impact area equals exactly the one role on the one resource.  

The DevOps Assistant explores the same principle for a different capability. Its identity is granted only the narrow right to retrieve the signed-in user's credentials from its OAuth connector:

That one role lets the agent participate in the delegated-identity flow (Module 4) and nothing more.

Principal Access Boundary

Principal Access Boundary (PAB) policies declare the maximum set of projects and resources an identity may reach, regardless of its IAM grants.

Even if an IAM policy is accidentally too broad, PAB restricts the agent to its declared boundary, so an attacker who finds a misconfigured binding still can't reach anything outside it.

This layering is deliberate defense in depth at the identity level: IAM expresses intended access, and PAB limits the potential impact of inevitable IAM configuration errors.

**Note:** Google Cloud Best Practice. Grant the narrowest role on the narrowest resource, bound to the agent's own identity, never a shared account. Treat PAB as the safeguard that contains misconfiguration, so a single wrong binding never opens the whole organization.
