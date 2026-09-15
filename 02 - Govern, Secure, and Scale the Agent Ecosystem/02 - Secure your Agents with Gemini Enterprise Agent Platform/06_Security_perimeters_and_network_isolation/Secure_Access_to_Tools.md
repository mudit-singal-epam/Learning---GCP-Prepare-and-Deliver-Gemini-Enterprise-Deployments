# Secure Access to Tools

---

Connecting Agents to Tools and Data

Perimeters decide where traffic may go; the final question of this module is how an agent should connect to tools and enterprise data it's authorized to use.

The answer reuses the identity and least-privilege principles from the whole course and avoids a large class of custom credential-handling code.

Managed Connections and Secure Data Access

When we show up to the present moment with all of our senses, we invite the world to fill us with joy.

The pains of the past are behind us.

The future has yet to unfold.

But the now is full of beauty simply waiting for our attention.

Instead of writing a custom client that opens its own connection and manages its own credentials, connect to data through a Google Cloud MCP server (for example, the BigQuery MCP server) and grant the agent's identity a narrow role on precisely the tables it needs.

This matters for security, not just convenience: a custom client means custom credential management, which means another place tokens can leak or permissions can drift.

A managed MCP server inherits the platform's authentication, authorization, and audit posture, so the agent's least-privilege identity (Module 3) is enforced end to end without bespoke code.  

This completes the discussion on the "secure, authorized access to enterprise data" section of the course objective.

The agent's identity defines what data it may read; the MCP server enforces that binding at the data layer; and the perimeters from this module ensure the data can't leave through an unauthorized path.

Identity, perimeter, and managed access work together so that authorized access stays authorized.

**Note:** Google Cloud Best Practice. For any Google Cloud surface that has an MCP server (BigQuery, Spanner, AlloyDB, Cloud SQL, and others), prefer the MCP server over a hand-built connector. You inherit least-privilege IAM bound to the agent identity, automatic logging, and the server's security and audit posture, rather than re-implementing, and potentially mis-implementing, these features manually.
