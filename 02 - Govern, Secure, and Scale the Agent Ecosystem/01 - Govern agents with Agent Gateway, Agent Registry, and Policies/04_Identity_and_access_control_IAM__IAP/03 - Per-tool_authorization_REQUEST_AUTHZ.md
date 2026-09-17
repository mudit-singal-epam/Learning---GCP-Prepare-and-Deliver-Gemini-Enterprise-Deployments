# Per-tool authorization (REQUEST_AUTHZ)

In this lesson, you'll learn how to restrict what tools an agent can execute by implementing the REQUEST\_AUTHZ service extension.

An agent that has unlimited access to write, update, or delete records across every database creates a major operational risk.

By configuring Identity-Aware Proxy (IAP) checkouts at the network layer, you will ensure that every single tool call is examined against strict permissions.

You'll also learn how to write smart, conditional policies using the Common Expression Language (CEL) to restrict critical write tools while allowing safe read tools.

## The REQUEST\_AUTHZ execution flow

The **REQUEST\_AUTHZ** extension acts as a gatekeeper at the very beginning of the request cycle.

1. **Invocation:** The agent attempts to call an internal tool (e.g., corporate-email).
2. **Intercept:** The [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) captures the request and invokes the REQUEST\_AUTHZ extension, which delegates evaluation to Identity-Aware Proxy (IAP).
3. **Verification:** IAP checks the incoming request headers to extract the [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) OIDC token. It verifies if the agent has been granted the roles/iap.egressor role on that *specific target server*. If the role is missing, IAP returns a 403 Forbidden response before the request is ever routed to the destination.

## Granular access policies using CEL conditions

To prevent over-privilege, you can attach **Common Expression Language (CEL)** conditions to the agent's IAM policy bindings. The [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) exposes several attributes that are evaluated instantly:

* iap.googleapis.com/mcp.toolName - The name of the tool being requested.
* iap.googleapis.com/mcp.tool.isReadOnly - A boolean indicating if the tool performs a read-only operation.

For example, to restrict a mortgage assistant agent so it can only run read-only operations on the corporate email server, you write the following CEL condition.

```text
api.getAttribute('iap.googleapis.com/mcp.tool.isReadOnly', false) == true
```

To apply this restriction, you define an IAM allow policy in a JSON-formatted file (e.g., agents-iap-policy.json).

```json
{
  "policy": {
    "bindings": [
      {
        "role": "roles/iap.egressor",
        "members": [
          "principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/REGION/reasoningEngines/AGENT_ID"
        ],
        "condition": {
          "title": "ReadOnlyToolsOnly",
          "description": "Restrict agent to read-only tools on corporate-email",
          "expression": "api.getAttribute('iap.googleapis.com/mcp.tool.isReadOnly', false) == true"
        }
      }
    ]
  }
}
```

Then, run the official Google Cloud gcloud CLI command to bind the policy directly to IAP for that specific MCP server resource:

```bash
gcloud beta iap web set-iam-policy agents-iap-policy.json \
    --project=PROJECT_ID \
    --mcpServer=MCP_SERVER_ID \
    --region=REGION
```

> [!Warning]
>
> Remember that the `reasoningEngines/<id>` changes every time you redeploy your agent code, changing your Agent Identity's principal name. You must re-apply the IAP policy containing the new principal ID after *every* redeploy, or tool calls will fail with immediate `403 PermissionDenied` errors.
