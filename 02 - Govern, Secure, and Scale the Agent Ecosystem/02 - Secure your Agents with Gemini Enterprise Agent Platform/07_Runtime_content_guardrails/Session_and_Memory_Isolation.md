# Session and Memory Isolation

---

The final content concern is preventing different users' data and context from mixing, both within a live conversation and across long-term memory.

This lesson covers isolation at the session and memory layers, completing the content safety framework.

### Session Isolation

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

The ADK uses **session\_id** and **user\_id** primitives to ensure that data and operations for different users remain separated even within the same deployed agent.

Two concurrent warranty-claim sessions cannot share state with each other, so one customer's data can never surface in another's interaction.  

This matters because a single deployed agent typically serves many users at once; without strict session scoping, the shared deployment itself would become a cross-user leakage path.

### Memory Isolation and Poisoning Prevention

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

For long-term memory, the Agent Platform Memory Bank enforces isolation using IAM conditions and **memoryScope** attributes, so stored memories are bound to the right user and never readable by another.  

Just as importantly, it routes all unstructured inputs through Model Armor before they're written to disk.

This prevents a poisoned memory entry, an injection planted in one session, from being persisted and silently influencing future sessions. Memory is a long-lived context surface, so an unvalidated write is a long-term risk of injection.

**Note:** Content controls augment rather than replace the identity and perimeter layers; each layer is designed assuming the others can fail. A compromised identity is still bounded by the perimeter; a payload that bypasses the perimeter is still inspected for shape and intent.
