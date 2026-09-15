# Model Armor and Semantic Governance

---

Model Armor & Semantic Governance

Callbacks validate the format or structure of fields. But many threats hide in valid-looking natural language that no structural check would catch.

Two more guardrails inspect the meaning of payloads, layering on top of the access and shape checks you've already seen.

### Model Armor: Inspecting Full Natural-Language Payloads

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

Model Armor: Inspecting Full Natural-Language Payloads

Model Armor performs inline scanning of full natural-language payloads for prompt injection, jailbreak patterns, PII, credentials, and unsafe URLs, redacting or blocking the payload before the model processes it.

A common misconception is that it only protects the human-facing interface. In fact, when integrated with Agent Gateway, it inspects every egress payload sent from one agent to another, not just the final response.

In the Warranty Claim System, it inspects the response the Data Agent sends back to the Case Manager.

If the Data Agent’s model accidentally included the customer’s full address or payment data in what should be a simple **"Covered"** reply, Model Armor redacts those fields before they reach the Case Manager’s context.

### Semantic Governance Policies: Enforcing Intent

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

Some attacks are authorized, well-shaped, and still malicious.

Semantic Governance Policies (SGP) are custom classifiers that operate at the semantic layer: they understand meaning, not just structure.

![Image](ldap-compliant directory - secure.png)

Even if network controls authorize the connection between the Case Manager and the Logistics Agent, and even if the payload passes the structural validation callbacks, an SGP acts as an intent-aware firewall.

It can block a plausibly worded request that tries to instruct the Logistics Agent to generate an unauthorized 100% discount code. A network control cannot catch that because the connection itself is legitimate.

1. **Three Checks for Content Controls and Layers**
Putting the content controls together with the layers from earlier modules gives you three checks, each asking a different question of the same request.
2. **Summary of Content Control Checks**
Each request is evaluated for access, shape, and intent, ensuring security and compliance at multiple levels.
3. **Access**
Can this agent reach this endpoint? Enforced by IAM, perimeters, and Agent Gateway.
4. **Shape**
Is the payload the correct structure for the tool contract? Enforced by ADK before/after callbacks.
5. **Intent**
Does the payload’s meaning comply with business policy? Enforced by Model Armor and Semantic Governance Policies.
A request must pass all three to proceed.

The two content guardrails, structural (callbacks) and semantic (Model Armor/SGP), are implemented in addition to the access controls; therefore, an authorized, well-formed message is still inspected to determine its intent.
