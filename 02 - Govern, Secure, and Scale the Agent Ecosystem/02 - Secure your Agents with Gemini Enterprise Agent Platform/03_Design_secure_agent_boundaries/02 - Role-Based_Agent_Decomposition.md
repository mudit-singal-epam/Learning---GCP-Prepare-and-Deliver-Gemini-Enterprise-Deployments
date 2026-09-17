# Role-Based Agent Decomposition

## Introduction to structural defense

Understanding the threats described previously is the first step; the next is structural defense.

The most effective way to contain those threats is to divide a complex workflow across agents that each own one specific role, and to direct all communication through a gateway rather than allowing direct communication between agents.

This lesson explores how role-based decomposition turns a potential breach into a recoverable error, using the Warranty Claim System as the case study.

## The Design Question: What's the Worst Case?

----
> For every agent you design, ask one question: "What is the worst outcome a hallucination or injection can cause, given this agent's tools and data access?"
----

Then narrow the role until that worst case is a recoverable error rather than an irreversible action.

This reframes security from **"how do I stop every attack"** to **"how do I ensure no single failure is catastrophic,"** a question you can actually answer for each agent.

An agent whose worst case is **"routes to the wrong specialist"** is fundamentally safer than one whose worst case is **"ships a free product,"** regardless of how clever the model is.

## Three Narrow Roles in the Warranty Claim System

The Warranty Claim System applies this principle across three agents, each with a deliberately constrained boundary.

**The Case Manager (orchestrator)** receives the sanitized claim, extracts the appliance model, fault, and serial number, and delegates it to specialists. Its boundary is strict: no database tools, no fulfillment tools, and no direct network path to any backend. If it's successfully injected, the worst outcome is a misclassification or an incorrect routing call, which the gateway can validate and block. A hallucination here produces a routing error, not a fraudulent shipment.

**The Data Vault (data specialist)** does exactly one job: look up warranty status and return only the specific fields fulfillment needs. It accepts only a serial number (never raw customer text) and returns a simplified status ("Covered," "Expired," or "Suspicious") plus the name and address required downstream. It is the only agent with database permissions, and it never returns full rows.

**The Logistics Liaison (fulfillment executor)** receives the minimum data (name, address, and status) and initiates shipping, email, and discount processes. It cannot query the database, its outbound access is restricted to approved vendors, and its branching logic is deterministic code, not model reasoning.

Because each role is narrow, a single injection occurs within a context that lacks the tools to cause real harm. Decomposition is the structural foundation that the identity, perimeter, and content layers later enforce.

## The Two-Question Audit

This lesson gives you a repeatable method to produce threat mapping, turning security from an undefined goal into a reviewable artifact that the later layers are built to enforce.

For each agent, ask two questions: **"what is its most dangerous failure mode?"**, and **"what control makes that failure recoverable rather than catastrophic?"**.

Let us examine the Warranty Claim System:

1. Case Manager: worst case: misclassification or routing to the wrong agent → control: it holds no execution tools, so the damage is bounded to a routing error the gateway can catch.
2. Data Vault: worst case: mass exfiltration of customer data → controls: a network perimeter around the data, an input-validation callback that rejects malformed serial numbers, and an instruction to return only the status.
3. Logistics Liaison: worst case: automated financial fraud → control: mandatory human-in-the-loop (HITL) approval before any financial API fires.

The mapping doubles as a design test and a build plan.

### Testing

Evaluate whether an agent's capabilities align with its stated role.

If a capability cannot be justified, it should be removed to prevent unnecessary complexity or vulnerabilities.

### Planning

Each control identified in the mapping process should be treated as a requirement to be addressed during implementation.

The Data Vault's "scoped data access" becomes least-privilege IAM bound to its Agent Identity (and a VPC perimeter; its "reject malformed input" becomes a tool callback. You will learn more about this later.

Designing the mapping first means the identity, perimeter, and content layers have a clear specification to satisfy rather than being applied without a formal plan.
