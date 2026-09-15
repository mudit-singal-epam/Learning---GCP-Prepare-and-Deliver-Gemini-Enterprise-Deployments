# Course summary

---

Congratulations! You have completed the course **Secure your Agents with Gemini Enterprise Agent Platform**.

In this course, you learned how to move from agents secured as an afterthought to agents secured by design, layer by layer, with identity and access as the foundation for reaching enterprise data safely.

You discovered the threats unique to multi-agent systems — prompt injection, lateral movement, data exfiltration, and excessive agency — and learned to contain them through role-based decomposition, separating model controls from agent controls, and mapping each agent's worst-case failure to a specific control.

You learned to establish a strong machine identity for every agent with Agent Identity (SPIFFE) instead of static-key service accounts, and bind least-privilege IAM backstopped by a Principal Access Boundary.

At the core, you learned to make an agent act on behalf of a signed-in user through delegated identity and a multi-legged (3-legged) OAuth consent flow, brokered by the Auth Manager and a connector so the agent never holds the raw token, and saw it implemented in the DevOps Assistant reading GitHub as the authorized user.

Finally, you then learned to confine that access with security perimeters: VPC Service Controls, network egress allowlists, and runtime content guardrails (ADK callbacks and Model Armor). The result is secure, authorized, and fully auditable access to enterprise data that scales across an entire fleet of agents.

![Image](complete.png)

Congratulations on completing this course!

![Image](confetti2.png)
