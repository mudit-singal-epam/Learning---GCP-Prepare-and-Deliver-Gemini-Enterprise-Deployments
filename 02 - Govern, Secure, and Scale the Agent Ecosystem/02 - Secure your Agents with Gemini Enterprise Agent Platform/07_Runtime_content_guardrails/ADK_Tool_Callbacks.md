# ADK Tool Callbacks

---

Network controls prevent unauthorized connections and identity controls prevent unauthorized callers.

Content controls, which are the third runtime layer, filter malicious or malformed payloads traveling inside authorized connections from authorized callers.

These are different attack vectors that require different defenses because a payload can be perfectly authorized to travel and still be hostile. The first content tool is deterministic validation at the tool boundary, provided by the ADK's callback hooks.

BeforeToolCallback: A Deterministic Input Firewall

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

A **BeforeToolCallback** runs before the model's tool request reaches the external system.

This is the right place for a check that doesn't depend on model reasoning, such as pure code or an LLM that either passes or raises an exception.

It doesn't matter how cleverly the model was manipulated, because the validation is independent of what the model produced.

In the Warranty Claim System, the Data Agent validates every serial number before it reaches BigQuery:

A prompt injection that tricks the Data Vault’s model into passing a SQL fragment, like **'; DROP TABLE entitlements; --**, as the serial number is caught here before any query fires.

This is a small amount of code defending against a large class of injection attacks, which is why it is one of the most effective controls you can implement.

AfterToolCallback: Validating What Comes Back

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

An AfterToolCallback applies the same deterministic discipline to tool outputs before they reach the next agent. It ensures the Data Agent can only ever return one of a few known-good status values ("Covered," "Expired," or "Suspicious") and never raw model output or a prompt-injected instruction disguised as a status.  

Together, before-callbacks and after-callbacks form a bidirectional integrity fence around every tool call: the before-callback validates inputs going out to external systems, and the after-callback validates outputs coming back before they re-enter the agent's reasoning context.

Neither half is optional; an unvalidated output is just an injection waiting for the next agent.
