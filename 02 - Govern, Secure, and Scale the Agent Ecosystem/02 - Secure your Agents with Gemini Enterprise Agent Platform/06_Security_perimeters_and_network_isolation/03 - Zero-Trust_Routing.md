# Zero-Trust Routing

## Lesson introduction

The macro perimeter guards the project's edge.

Inside it, you still need to govern traffic between agents and traffic going out to legitimate external systems. Two controls cover those distinct segments of the traffic surface.

## Network Isolation: Inspecting Internal Traffic at Layer 7

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

Cloud Next Generation Firewall performs Layer-7 inspection on agent-to-agent (A2A) and MCP communications inside the perimeter.

Layer-7 means it parses payload content, not just source and destination IP and port, so it can recognize patterns like a SQL-injection fragment embedded in what otherwise looks like a legitimate A2A call.

A compromised Case Manager that attempts to send a malicious query to the Data Agent through a side channel can be caught here, below the application layer, before the destination agent ever processes it.

## Secure Web Proxy and Outbound Traffic Control

Secure Web Proxy governs egress for agents that legitimately call external systems.

The Logistics Agent calls third-party shipping carriers and email providers, which are legitimate destinations, so it is not possible to simply block outbound traffic.

Instead, the proxy restricts its outbound connections to an explicit allowlist of vendor URLs. Any outbound call to a destination not on the list, including attacker-controlled command-and-control infrastructure used for exfiltration, is dropped before it leaves the VPC.

This is the network-level complement to data minimization: even if a model is tricked into trying to send data somewhere it shouldn't, there's nowhere unapproved for it to go.
