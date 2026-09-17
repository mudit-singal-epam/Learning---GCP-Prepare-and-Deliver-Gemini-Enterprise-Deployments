# Delegated Identity: Acting on Behalf of the User

Previously, you gave each agent its own cryptographic Agent Identity, a machine identity that answers the question **"who is this agent?"**.

That identity is exactly right when an agent calls platform infrastructure on its own authority: writing an audit summary to a bucket, querying a dataset it owns, or routing a message through the gateway.

But many enterprise tasks aren't the agent's to perform. When a DevOps Assistant lists your private GitHub issues, it must not act as itself; it must **act as “you”**.

If it used its own identity, it would either examine nothing (no access to your private repos) or, far worse, it would need standing access to every user's data, turning a single compromised agent into an organization-wide breach.

The secure answer is delegated identity: the agent borrows the user's authority for the duration of a task, bounded by exactly the permissions that user already has.

## Agent Identity versus User Delegation

Every call an agent makes carries a credential, and that credential answers one of two questions.

1. The first is "what is this agent allowed to do as itself?"
2. The second is "what is this specific user allowed to do, and is the agent permitted to act on their behalf right now?"

These are different security questions with different blast radii, and conflating them is one of the most common ways agentic systems leak data.

### The agent's own authority

**The agent's own authority** is the preferred model for platform-level work that belongs to the agent regardless of who is chatting with it.

In the Warranty Claim System, the Data Vault Agent queries BigQuery under its own Agent Identity, because warranty records belong to the business, not to the customer who filed the claim.

The agent's identity holds a narrowly scoped role, read access to two datasets, and nothing about that access changes from one user session to the next.  

An important point to note is that, even though the Agent itself *can access any rows of the dataset*, the specific rows to which it has access for a specific query are *constrained* based on the current user making the request.

### User-delegated authority

**User-delegated authority** is the preferred model whenever the downstream system enforces *per-user* access controls.

The DevOps Assistant reads GitHub issues, but GitHub doesn't know or care about your agent; it knows about *the users* and the repositories each one can see.

For the assistant to return the correct, authorized results, it must present a credential that represents the signed-in user. The agent becomes a conduit for the user's existing permissions rather than a new permission boundary of its own.

### Why a Machine Identity Can't Substitute for the User?

It is common to consider "solving" GitHub access by granting the agent's own identity broad access to all repositories.

This is an anti-pattern for two reasons.

1. First, it collapses every user's access into one identity: if the agent is injected or compromised, the attacker inherits access to *everyone's* data at once, not just the current user's.
2. Second, it breaks the audit trail; GitHub would record every action as "the agent," making it impossible to attribute who actually requested what.

## Choosing a Model Per Tool

The decision to choose an authentication model isn't made once for the whole agent; it's made per tool. A single agent often needs both models at the same time.

The DevOps Assistant uses its **own** Agent Identity to authenticate to the platform (creating sessions, emitting telemetry, routing through the gateway), and *delegated* user authority to call GitHub.

---
> Ask one question of every tool: does the target system enforce access at the level of the individual end user?
---

If yes, the call needs **delegated** identity. If the resource belongs to the business and access is the same for every user, the agent's own identity is preferred and simpler.

> ## Google Cloud Best Practice
>
> Use the agent's own identity for platform and business-owned resources; use user-delegated identity for any tool that must honor per-user ACLs. Mixing the two within one agent is normal and expected. The goal is that each call carries the minimum authority required.
