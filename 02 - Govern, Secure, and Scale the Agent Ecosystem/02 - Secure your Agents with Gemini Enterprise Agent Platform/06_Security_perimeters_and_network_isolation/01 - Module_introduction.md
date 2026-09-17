# Module introduction

## Security perimeters and network isolation

In this module, you'll analyze how to implement network-level security perimeters to contain agent activity.

You'll explore how VPC Service Controls act as a macro perimeter to block data exfiltration regardless of the agent's identity or credentials.

You'll also examine Layer-7 inspection of internal traffic to detect malicious payloads within authorized connections and implement Secure Web Proxy egress allowlists to prevent unauthorized external communication.

By integrating these network-level controls with your existing identity and access layers, you'll build a zero-trust architecture that prevents an agent from reaching destinations or moving data outside its authorized scope.

By the end of this module, you'll be able to:

* Analyze the protective role of VPC Service Controls in establishing a macro-perimeter against data exfiltration.
* Evaluate the interaction between Principal Access Boundaries and network-level perimeters to create redundant security ceilings.
* Assess the effectiveness of Layer-7 traffic inspection in identifying malicious patterns within agent-to-agent communications.
* Construct secure egress policies using web proxies to enforce strict network-level control over outbound agent connections.
