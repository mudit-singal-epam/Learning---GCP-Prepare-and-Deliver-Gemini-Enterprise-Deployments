# Multi-Legged OAuth Explained

Previously, you explored the concept of acting on a user's behalf, now let's examine the technical protocol that makes it possible: OAuth 2.0.

The security of your agent’s delegated access depends entirely on the structure of this handshake, specifically, how many "legs" or parties participate in the exchange.

This lesson explores the difference between two-legged and three-legged OAuth, tracing the consent flow step-by-step so you can implement delegated identity without ever exposing user credentials.

---
> Delegated identity raises an important question: how does an agent come to hold a user's authority without ever knowing the user's password?
---

The answer is OAuth 2.0, the protocol that lets a user grant a third party limited, revocable access to their data without sharing credentials.

For agents, the distinction that matters most is how many parties participate in the exchange, or what practitioners call the number of steps in the exchange.

## Two-Legged OAuth: The Agent's Own Authority

A two-legged flow involves two parties: the client (the agent) and the authorization server. There is no Human-in-the-loop (HITL).

The agent presents its own credentials, proof of its machine identity, and receives a token representing *its* authority.

This is the OAuth shape behind the agent's-own-authority model from the previous lesson.

It's appropriate for background tasks and business-owned resources; the Data Vault Agent acquiring a token to call a Google Cloud API on its own behalf is, conceptually, a two-legged exchange.

There's no consent screen because there's no user whose permission is being borrowed.

## Three-Legged OAuth: Borrowing the User's Authority

A three-legged flow adds the critical third party: the resource owner, the human user whose data is at stake. The three legs are the user, the client (the agent), and the authorization server.  

The flow proceeds as follows:

1. **Authorization request**
The agent needs to act for the user, so it redirects the user's browser to the authorization server's URL, including which scopes it's requesting (for example, read-only access to issues).
2. **User consent**
The authorization server authenticates the user and displays a consent screen: "DevOps Assistant wants to read your issues and pull requests." The user approves or denies. Crucially, this happens between the user and the authorization server, the agent is not involved in the authentication process and never sees the user's password.
3. **Authorization code returned**
On approval, the authorization server redirects the user's browser back to a pre-registered redirect URI belonging to the application, carrying a short-lived, single-use authorization code.
4. **Token exchange**
The application presents that code, plus its client credentials, to the authorization server's token URL, and receives an access token (and usually a refresh token). The token represents the user's granted authority.
5. **Authorized call**
The agent now calls the protected API with the access token and receives only what the user is allowed to see.
Understanding the flow

### Understanding the flow

A three-legged flow is defined by two distinct endpoints: an **authorization URL** (where the human consents) and a **token URL** (where the code is exchanged for a token).

Configuring these two values is required when setting up an IAM Connector. The separation is deliberate: the authorization step is interactive and human-facing, while the token exchange is a server-to-server call that proves the application's identity.  

The intermediate redirect with a single-use code is what keeps the access token off the user's browser and out of URL history, as the token is only ever delivered over the back-channel token exchange.
