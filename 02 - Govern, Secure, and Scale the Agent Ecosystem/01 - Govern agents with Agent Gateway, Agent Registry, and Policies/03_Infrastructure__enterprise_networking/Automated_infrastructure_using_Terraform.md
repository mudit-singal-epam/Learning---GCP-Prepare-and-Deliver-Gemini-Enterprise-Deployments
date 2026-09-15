# Automated infrastructure using Terraform

### Heading

In this lesson, you'll learn how to automate the provisioning of the core infrastructure stack using Terraform.

Manual configuration of virtual private networks, subnets, firewall rules, and service attachments is highly error-prone and difficult to replicate across environments.

By deploying your agent security infrastructure as code (IaC), you ensure that every development, staging, and production environment maintains an identical, secure posture.

You'll write and apply declarations that configure the VPC, subnets, Artifact Registry, and the [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) automatically.

The foundation network VPC

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

The automated infrastructure starts with a dedicated virtual private cloud (VPC) network (e.g., gateway-vpc) that isolates the agent ecosystem. In this network, we provision several specialized subnets:

* **Primary Subnet:** Standard regional subnet where standard internal services run.
* **Proxy-Only Subnet:** A /24 active range required by Google Cloud's regional Application Load Balancer.
* **Agent Gateway Subnet:** A dedicated /28 or larger range (using RFC 1918 addresses like 10.0.0.0/24) reserved exclusively for [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) egress. It must not overlap with standard VPC routing.
* **Cloud NAT:** Configured on a Cloud Router to allow resources in private subnets to retrieve software updates without exposing them to inbound internet traffic.

Declaring the agent gateway resource

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

### Heading

In your Terraform configuration, you define the [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) using the google\_network\_services\_agent\_gateway resource. This resource specifies that the gateway operates in AGENT\_TO\_ANYWHERE mode, binds to the project's regional [Agent Registry](https://docs.cloud.google.com/agent-registry/overview), and references a **Network Attachment** for physical egress.

### Heading

**Google Cloud Best Practice**  
When applying authz policies to a newly created [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) in Terraform, always introduce a **time\_sleep** resource of at least 30 seconds between the gateway creation and policy attachments. The gateway's underlying tenant project requires a brief period to stabilize, and attempting to attach policies immediately will cause transient "resource can not be updated" API errors.
