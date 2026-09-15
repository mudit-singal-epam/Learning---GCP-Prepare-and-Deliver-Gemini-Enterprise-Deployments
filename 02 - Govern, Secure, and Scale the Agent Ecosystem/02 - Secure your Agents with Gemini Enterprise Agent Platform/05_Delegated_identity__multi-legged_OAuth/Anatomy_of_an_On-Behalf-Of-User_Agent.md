# Anatomy of an On-Behalf-Of-User Agent

---

You now have the full conceptual stack: delegated identity, the three-legged flow that grants it, and the Auth Manager and connector that broker it safely.

In this lesson you'll examine how those concepts assemble into a real agent by reading the key pieces of the DevOps Assistant you'll build in the codelab.

In this course and in the codelab, you use [**Google’s Agent Development Kit**](https://cloud.google.com/agent-development-kit) to build our multi-agent system.

Wiring Delegation Into the Agent

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

ADK separates *what the agent does* from *how its credentials are obtained*. Delegation is enabled by registering a credential provider once, so the framework knows to resolve user credentials through the Auth Manager rather than expecting the agent to supply them:

This single registration is what connects the abstract Auth Manager from the previous lesson to the running agent. From here on, when a tool says it needs authorization, the framework drives the consent flow and retrieves the bound token automatically; the agent author writes no OAuth code.

Declaring a Tool’s Authority Requirement

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

The tool itself only has to declare that it requires user authority via a particular connector. It does this with an auth scheme that names the connector and the URI the flow should return to after consent:

Read this declaratively. The toolset says: **"I connect to GitHub's MCP endpoint, and reaching it requires the user's authority obtained through the github-oauth-provider connector."**

Notice what is absent: there is no **Authorization** header and no token.

That omission is the security property; the framework injects the user's credential at call time and the code never holds it. This is the concrete realization of **"the agent never sees the token"** from the previous lesson.

Reading the Consent Round-Trip

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

The first time a user asks the agent to do something that needs GitHub, there's no consent yet, so the framework emits a special event, a function call named **adk\_request\_credential**, instead of calling the tool.

That event carries a one-time nonce that ties the upcoming consent to this exact session.

A thin client surface (a web page in the demo) catches the nonce, sends the user through the provider's consent screen, and when the provider redirects back, finalizes the grant:

The important idea is the round-trip, not the API surface: the agent requests a credential (nonce out), the user consents at the provider, and the client finalizes the grant (state + nonce back).

After finalization, the token lives in the vault, bound to the agent's identity, and subsequent tool calls resolve it silently.  

A detail worth noticing: the nonce is single-use and session-scoped, so a consent captured for one session can't be replayed to authorize another.

Least Privilege as a Design Choice

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

Least Privilege as a Design Choice

Security isn't only about who the credential represents; it's also about how much it can do. Two choices in the configuration above narrow the blast radius even when acting as a fully authorized user.

The header **X-MCP-Readonly: "true"** requests a read-only surface, so the delegated access can list and inspect but never write, update, or delete.

And the agent's system instruction reinforces the same boundary in natural language:

This is defense in depth at the tool boundary: the model is *instructed* to stay read-only, and the connection is *configured* to be read-only, so a prompt injection that talks the model into attempting a write still hits a surface that can't perform one.

The same principle you saw in the Warranty Claim System, to make the dangerous action structurally impossible, not merely discouraged, applies here to delegated access.

**Note: Google Cloud Best Practice:** Even with correctly delegated identity, apply least privilege to the *scope* of access. Request the narrowest OAuth scopes the task needs, prefer read-only tool surfaces when the agent's job is to read, and reinforce the boundary in the system instruction. Delegated identity controls *whose* authority is used; scope and read-only controls limit *what that authority can do* through your agent.
