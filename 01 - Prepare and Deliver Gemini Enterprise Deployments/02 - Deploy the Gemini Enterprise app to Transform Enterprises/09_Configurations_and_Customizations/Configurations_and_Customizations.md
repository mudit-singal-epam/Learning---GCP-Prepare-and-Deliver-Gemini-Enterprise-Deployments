# Configurations and Customizations

Once the core architecture, identity boundaries, and security perimeters are established, administrators can **fine-tune the end-user experience**.

Gemini Enterprise provides a robust suite of configuration options to **customize the interface**, modify search behavior, **govern feature access**, and **monitor adoption**.

Let's explore a few notable settings.

## Search UI tab

You can white-label the web application with a custom corporate**Logo Image URL**.

## Control tab

### Serving Controls

Service controls change the default behavior of how a request is served when results are returned. Serving controls act at a data-store level. They act as the steering mechanism for search relevance by modifying how the AI retrieves results.

For example, administrators can explicitly boost results from highly authoritative data stores (such as official HR policy documents) to ensure they appear first.

Conversely, they can bury or completely filter out less relevant sources (like legacy archives) so the AI only grounds its answers in verified, up-to-date information.

### Custom Synonyms

Custom synonyms align the AI's understanding with your organization's unique language.

By grouping terms that mean the same thing in your company (e.g., 'PTO,' 'Leave,' and 'Vacation,' or mapping an internal project codename to a public product title), administrators guarantee that users receive comprehensive results regardless of the specific corporate jargon they type into the prompt.

## Assistant settings tab

### Custom LLM Instructions

Administrators can govern the assistant's baseline personality, tone, and formatting behavior across all interactions.

For example, they can instruct the assistant to act as a 'Senior Compliance Officer,' requiring it to maintain a strictly formal tone, automatically include legal disclaimers on specific topics, and always format financial figures in a standardized regional format.

### Enable Google Search Grounding

This feature allows the assistant to supplement your internal enterprise data with real-time public web context, ensuring answers are enriched with the latest external facts.

For instance, if a sales representative asks Gemini to prepare a brief for a client meeting, the assistant can pull account history from your internal CRM Data Store, while simultaneously using Google Search grounding to pull the client's latest news announcements or stock performance from that very morning.

### Disable Grounding for Internal Agents

In scenarios involving strictly internal agents, such as HR policy bots or internal IT support, grounding can be disabled.

Pulling in generic internet data in these cases can dilute the accuracy of the response, causing the AI to surface a standard internet answer instead of your company's specific, mandated internal policies.

## Knowledge graph

A knowledge graph is a structured network that maps out the **underlying relationships between different data points** (like people, documents, and concepts) to provide deeper contextual understanding.

Rather than just matching keywords, it **connects entities like nodes on a web**, allowing the AI to understand the **meaning and context behind a query**.

### Public Knowledge Graph

A public knowledge graph enriches search responses by incorporating publicly available world knowledge and facts.

If a user searches for a competitor, the Public Knowledge Graph can instantly connect that company's name to its current CEO, subsidiary brands, and global headquarters, pulling in broad factual context without needing that data stored internally.

### Private Knowledge Graph

Public knowledge graphs synthesize specialized, confidential insights and relationships relying strictly on internal data. It relies on your organization's people data.

You’ll need to connect your people data in the data stores page.

A good example is when an employee searches for 'Jane's Q3 projects.'

The Private Knowledge Graph understands the relationship that 'Jane' manages the 'Engineering Team,"'which owns 'Project Apollo,' scheduled for 'Q3.'

It will surface the Project Apollo documentation even if the document never explicitly mentions Jane's name.

### Feature management

* **Enable Agent Designer**
  * Empower non-technical users to construct custom, specialized agents using only natural language prompts instead of complex code.
* **Session Sharing**
  * Allow employees to generate a secure link to forward useful AI conversations to colleagues, preserving the full context of the interaction.
* **Enable Image Generation**
  * Enable Image Generation and explicitly restrict or govern which foundational models are available for organizational use.

## Summary

Configurations and Customizations provides administrators with a suite of options to fine-tune the Gemini Enterprise experience, including customizing the interface, controlling search relevance, defining the assistant's tone and behavior, and managing feature access.
