# Module introduction

## Delegated identity and multi-legged OAuth

In this module, you'll explore the critical distinction between an agent's native identity and user-delegated authority.

You'll analyze how to implement delegated identity using multi-legged OAuth flows to ensure agents act strictly within the permissions of the signed-in user rather than relying on broad, static credentials.

You'll examine the mechanics of the Agent Platform Auth Manager and connectors, which broker these secure consent flows to keep sensitive tokens out of agent application code.

By the end of the module, you'll integrate these concepts to build agents that safely borrow user authority, ensuring that every tool call remains fully attributable, audit-compliant, and scoped to the user's explicit access levels.

By the end of this module, you'll be able to:

* Distinguish between an agent's native machine identity and user-delegated authority to determine the appropriate authentication model for specific tool operations.
* Evaluate the security trade-offs between two-legged and three-legged OAuth flows to ensure robust, user-consented access to protected resources.
* Implement delegated identity patterns using connectors and the Auth Manager to isolate sensitive credentials from agent application code.
* Apply least-privilege principles to tool configurations by specifying narrow access scopes and read-only requirements for on-behalf-of-user operations.
