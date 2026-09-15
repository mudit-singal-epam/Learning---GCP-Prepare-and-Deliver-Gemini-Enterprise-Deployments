# Module introduction

Content security guardrails

In this module, you'll learn how to manage tool discovery and implement comprehensive observability across your agent ecosystem. Hardcoding endpoint URLs directly in your agent code makes it incredibly fragile and creates major security auditing gaps.

You'll learn how to use the [Agent Registry](https://docs.cloud.google.com/agent-registry/overview) to manage dynamic tool discovery at runtime, enabling agents to bind to approved tools without hardcoding static URLs into their deployment manifests.

Additionally, you'll explore how to use OpenTelemetry and Cloud Trace to audit every step of the agentic execution path, capturing distributed traces that map the entire journey of a user prompt.

![Image](CSS Graphic Crop (5).png)

By the end of this module, you'll be able to:

* Register and manage Google APIs and third-party MCP servers in the [Agent Registry](https://docs.cloud.google.com/agent-registry/overview).
* Configure an [Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk) agent to dynamically discover and bind tools at runtime.
* Analyze distributed traces in Cloud Trace to audit security policies and tool execution paths.
