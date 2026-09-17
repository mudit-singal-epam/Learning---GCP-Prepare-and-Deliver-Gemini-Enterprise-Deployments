# Flexible tool ingress (Public vs. private architecture)

In this lesson, you'll learn about the two primary networking topologies for hosting your internal tools (MCP servers) on Cloud Run: Default (Public Ingress) and Secure (Private Ingress).

Choosing the wrong ingress model can either expose sensitive database APIs to the internet or create insurmountable infrastructure bottlenecks for your developers.

By analyzing the trade-offs of both architectures, you will design a deployment plan that fits your company's security standards.

You'll learn how to build and deploy tools in both modes, ensuring you can support rapid development cycles while maintaining absolute production security.

## Default path: Cloud run with public ingress

In the **Default Ingress Pattern**, internal tools (MCP servers) are deployed to Cloud Run with the ingress configuration set to all.

* **Topology:** The service receives a public \*.[run.app](http://run.app) URL. Traffic is routed from the [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) over standard HTTPS.
* **Security:** Access is still secured! Although the URL is public, every request is intercepted by IAP and the [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)'s service extensions. Unauthenticated internet requests return immediate errors.

**Pros/Cons:** Extremely simple to set up, requires no custom domains, and is ideal for sandbox development or rapid proof-of-concept deployments. However, it does not satisfy strict corporate compliance rules that forbid public endpoints entirely.

## Secure path: Cloud run with private networking

In the **Private Ingress Pattern**, Cloud Run ingress is restricted to internal-and-cloud-load-balancing.

* **Topology:** The public \*.[run.app](http://run.app) URL is disabled. The services are placed behind an internal regional Application Load Balancer (ALB) configured with a Serverless Network Endpoint Group (NEG).
* **Infrastructure Setup:** You provision a regional Google-managed certificate, set up DNS authorizations, and configure Cloud DNS to route all internal queries for \*.mcp. directly to the internal ALB's frontend IP.

**Pros/Cons:** Provides absolute network isolation—the tools are completely unreachable from outside the VPC. However, it requires owning a public DNS domain delegated to Cloud DNS to validate the SSL certificate.

| Ingress feature | Public ingress (Default) | Private ingress (Secure) |
| --- | --- | --- |
| **Cloud Run ingress setting** | ingress = "all" | ingress = "internal-and-cloud-load-balancing" |
| **Hostname type** | Public \*.run.app | Private \*.mcp.your-domain.com |
| **SSL certificate** | Automatic (Google-managed) | Regional Google-managed (Requires DNS validation) |
| **External visibility** | URL is public (secured using IAM) | Completely hidden (No public routing exists) |
