# Runtime tool discovery (Agent registry)

### Heading

In this lesson, you'll learn how to configure runtime tool discovery using the [**Agent Registry**](https://docs.cloud.google.com/agent-registry/overview).

Hardcoding service URLs or database connection strings in your agent source code forces developers to redeploy the entire agent code every time an endpoint moves or scales.

By utilizing the [Agent Registry](https://docs.cloud.google.com/agent-registry/overview), you'll decouple agent code from system infrastructure.

You'll learn how to register tools and APIs as central registry services, allowing your agents to search, locate, and bind to approved tools dynamically on startup.

The Agent Registry architecture

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

The [**Agent Registry**](https://docs.cloud.google.com/agent-registry/overview) is a centralized, regional catalog of approved services (including Google APIs and third-party Model Context Protocol servers) deployed within your project.

* **Dynamic Binding:** Instead of hardcoding a URL like , the developer simply instructs the agent to look up legacy-dms in the registry.
* **Egress Decoupling:** Because the [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) reads this registry, it automatically knows which external hostnames are registered and configures routing and security policies for them dynamically. Unregistered hostnames are blocked by default at the network boundary.

Registering services in the registry

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

### Heading

You register services in the [Agent Registry](https://docs.cloud.google.com/agent-registry/overview) using the gcloud alpha agent-registry CLI or Terraform. For example, to register an MCP server hosted on Cloud Run:

### Heading

The registry stores the display name, the path to the tool specification JSON schema (which describes the tool's functions to the LLM), and the target interface URL.

**Google Cloud Best Practice**   
Always use the [Agent Registry](https://docs.cloud.google.com/agent-registry/overview) for all tool integrations rather than manually configuring local environment variables with tool URLs inside your agent runtime container.

This keeps your agent deployments clean, portable, and centrally auditable by security teams.
