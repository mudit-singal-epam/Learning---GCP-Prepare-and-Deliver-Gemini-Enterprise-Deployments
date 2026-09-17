# VPC Service Controls and Principal Access Boundary

## Lesson introduction

Identity establishes who an agent is and on whose behalf it acts. Network controls establish where it can send traffic and who can reach it.

These are independent layers: an agent with a perfectly scoped identity can still exfiltrate data if outbound traffic isn't controlled, and a well-isolated network doesn't protect against a compromised agent making authorized calls with a malicious payload.

This lesson starts with the outermost, policy-based perimeter.

## VPC Service Controls (VPC-SC): Macro Security Perimeter

VPC Service Controls (VPC-SC) encapsulates an entire project within a macro security perimeter.

Even if an agent's credentials are stolen and replayed from outside the perimeter, Google API calls that attempt to read BigQuery data, Cloud Storage objects, or any other protected resource are rejected by the perimeter policy, regardless of whether the credential itself is valid.

Because it's policy-based, VPC-SC requires no application code change and blocks exfiltration at the network level, covering gaps that application logic might miss.

---
> This is a fundamentally different guarantee from IAM: IAM asks **"is this identity allowed?"** while VPC-SC asks **"is this request coming from inside the perimeter?"**
---

VPC-SC pairs naturally with the Principal Access Boundary (PAB) mentioned earlier to give you two enforced ceilings above your IAM bindings.

PAB limits which resources an identity may name; VPC-SC limits where data may move. Because Agent Identity is a first-class principal in VPC-SC ingress and egress rules, you can write perimeter policy directly against a specific agent.

The combined effect is that a single misconfiguration, like a too-broad IAM binding, doesn't open the organization: even with a valid, over-scoped credential, an attacker still can't move data across the perimeter or reach a resource outside the boundary.
