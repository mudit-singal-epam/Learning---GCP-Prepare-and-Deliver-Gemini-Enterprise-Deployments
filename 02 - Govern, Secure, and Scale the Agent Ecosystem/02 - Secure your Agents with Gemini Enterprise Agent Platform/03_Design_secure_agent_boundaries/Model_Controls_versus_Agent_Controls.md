# Model Controls versus Agent Controls

---

Model controls: Protecting LLMs from manipulation

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

Model controls protect the underlying LLM from manipulation. They answer the question: What can an attacker make this model say or do through its inputs?

*Click each tab to learn more.*

### Input sanitization

Routes untrusted input through an inspection layer that scans for injection and sensitive data before it reaches the model.

### Data minimization

Prevents the model from holding data it could misuse. In the Warranty Claim system, the Data Agent is prompted to return only the status and required PII. This ensures the full record, including purchase price, payment method, service history, never reaches the Case Manager or Logistics Agent. Consequently, this data cannot be hallucinated into an outbound call.

### Scope isolation

Narrows what a model can be tricked into doing: The Data Agent’s prompt never mentions shipping APIs or discount codes. If a model does not have access to a tool, it cannot be instructed to use it.

Agent controls: Constraining capability

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

Agent controls protect the autonomous actions an agent can take. They answer: Even if the model misbehaves, how do you contain the damage?

*Click each tab to learn more.*

### Goal bounding

Limits each agent to the tools its role requires; the Case Manager holds no execution tools at all.

### IAM least privilege

Binds permissions to each agent's unique identity rather than a shared account, so a compromise of one agent cannot reach another's resources.

### Human-in-the-loop (manual approval process)

Capabilities can help suspend any high-stakes action for explicit approval before it fires; in the Logistics Liaison, the shipping-label call pauses for a human regardless of what the model decided or said.

**Note:** Standard IAM prevents unauthorized API calls but cannot prevent a model from hallucinating a bad action through an *authorized* one. Model controls constrain intent; agent controls constrain capability. Both are necessary, and the most robust designs make them complementary; each layer covers gaps left by the other.
