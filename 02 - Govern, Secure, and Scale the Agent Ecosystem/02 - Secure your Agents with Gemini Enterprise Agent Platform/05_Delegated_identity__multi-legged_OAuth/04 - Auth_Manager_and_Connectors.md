# Auth Manager and Connectors

The three-legged flow you just traced has a high-risk step: somewhere, an access token that grants access to a user's data has to be stored and reused across the conversation.

If that token lives in your agent's code, environment variables, or logs, you've recreated the exact static-secret problem you eliminated by adopting Agent Identity described previously.

This lesson introduces the platform component that runs the OAuth flow for the agent and keeps the credential out of the agent's hands entirely: the **Agent Identity Auth Manager**, configured through a connector.

## Agent Platform Auth Manager

The Auth Manager is a managed broker that owns the complex, security-sensitive parts of OAuth on the agent's behalf. When a tool needs delegated access, the Auth Manager drives the consent flow, exchanges the authorization code for a token, and stores that token in a managed vault keyed to the user.  

The agent's code never reads the token. When combined with Agent Gateway, the token is decrypted and injected into the outbound request *at the gateway*, so it never even transits the agent's process.

This is a structural improvement over custom-developed OAuth implementations.

The most common way real systems leak tokens is by handling them in application code: caching them carelessly, logging a request that includes the **Authorization** header, or embedding them into a container.

If the agent never possesses the raw credential, none of those failure modes are reachable. The agent expresses *intent* ("call this tool as the user"); the platform supplies the *credential*.

## IAM Connector

A connector is the configuration object that tells the Auth Manager how to perform the three-legged flow for one external system. It captures exactly the values you met in the previous lesson: the authorization URL, the token URL, and, after you register the application with the provider, the client ID and client secret.  

To create a Connector for a third party provider (Github in this example) in the Agent Platform Auth Manager, run the following gcloud command. The authorization and token url varies depending on the provider you are connecting to.

```bash
gcloud alpha agent-identity connectors create github-oauth-provider \
    --project="project-id" \
    --location="us-central1" \
    --three-legged-oauth-authorization-url="https://github.com/login/oauth/authorize" \
    --three-legged-oauth-token-url="https://github.com/login/oauth/access_token"
```

After creating the connector, run the **describe** command to retrieve its **redirect URI**. Then register a new OAuth app in GitHub, setting this value as the app's redirect URI; it tells GitHub where to send the user back once they've authenticated.

```bash
gcloud alpha agent-identity connectors describe github-oauth-provider \
    --project="project-id" --location="us-central1"
```

Finally, registering the OAuth app gives you a client ID and secret, which you supply back to the connector. With that, the connector holds everything the three-legged flow needs.

```bash
gcloud alpha agent-identity connectors update github-oauth-provider \
    --project="project-id" \
    --location="us-central1" \
    --three-legged-oauth-client-id="YOUR_CLIENT_ID" \
    --three-legged-oauth-client-secret="YOUR_CLIENT_SECRET"
```

A connector is just the OAuth flow's parameters turned into managed configuration: the authorization URL, token URL, redirect URI, and client credentials each map onto a connector field. You can try these commands hands-on in the lab section.

> ## Google Cloud Best Practice
>
> Prefer Auth Manager and connectors over implementing custom-built OAuth in your agent. You inherit the credential vault, automatic token refresh, mTLS/DPoP token binding, and audit logging "for free," and you remove the single largest source of token leaks: application code that touches raw credentials.
