# Data connectors

## **Get started with Gemini data connectors**

On day one, it is highly recommended to stick to Generally Available (GA) data connectors. Non-GA connectors can be identified in the documentation here: [Connect a third-party data source](https://cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source?hl=en)

If working with non-GA data connectors, be prepared to encounter technical issues that may require waiting for connector development or alternative data access patterns to overcome.

Some roadmap features may not yet be available for some connectors. Ensure that you have tested a connector for its current capabilities before guaranteeing that certain features of that data connector are available.

Contact your Partner Development Manager (PDM) or Partner Advisor (PA) for an up-to-date list of data connectors and their statuses.

When configuring data access to connectors, remember that search and summarization in Gemini Enterprise requires only read access to the data sources.

## **Consider ingesting data if a connector is not ready**

If certain data must be part of a customer’s solution, and a connector is not yet ready, consider ingesting the data into an appropriate database on Google Cloud and using a first-party data connector to access the data through Gemini Enterprise.

## **Custom data connectors**

Customers can now develop [custom data connectors](https://docs.cloud.google.com/gemini/enterprise/docs/custom-connector). Custom connectors work by using an automated data pipeline to perform three key actions: Fetch, Transform, and Sync. This process ensures external data is correctly prepared and uploaded to Gemini Enterprise.

- **Fetch**: The connector pulls data, including documents, metadata, and permissions, from external system using its APIs, databases, or file formats.

- **Transform**: The connector converts raw data into the document format of the Discovery Engine, structures the content and metadata, and assigns a globally unique ID to each document. For access controls, you can use either Google-recognized identities directly or identity mapping for external users or custom groups.

- **Sync**: The connector uploads the documents to Gemini Enterprise data stores and keeps them updated through scheduled jobs. The data sync is performed using a data store created for an entity. You can find more information about creating data stores by following the [Data store creation process](https://docs.cloud.google.com/gemini/enterprise/docs/custom-connector#data-store-creation-process). Choose a sync mode based on your needs: *Incremental* adds and updates data, while *Full* replaces the entire dataset.

## **Identity management options**

A new Google Cloud domain will need to be established for Gemini Enterprise, configuring core identity and access management within Google Cloud Identity. It also may require Workforce Identity Federation setup, if applicable, to integrate with existing identity providers. The goal is to provide a solid identity and access foundation.

- Cloud Identity
  - Google’s first-party Identity solution
  - Customers sync identity from their third-party IdP to create Cloud Identities through GCDS
- Workforce Identity Federation
  - Google’s support for third-party Identity solution.
  - Customers federate identity from third-party IdP to access any Google Cloud service.
  - No sync required.

## **Pro tips for data connectors**

- **Validate everything first:**

  - Don’t assume data connectors can do everything you can imagine.

- **De-risk with a technical pre-flight check:**

  - Confirm IAM permissions and access policies *before* the engagement starts.

- **Start small with connectors:**

  - Master one connector before adding more to avoid unnecessary complexity during the crucial learning phase.

- **Make sure your testers, including execs, have permissions:**

  - Sometimes testers won’t have permission to data in a data source and may think it’s not working.

- **What does 'good' look like?:**

  - Be transparent about connector limitations.

  - Clearly delineate what Gemini Enterprise does and what NotebookLM is for.

- **Leverage your Google resources:**

  - Having a Partner Engineer or Specialist who understands how Gemini Enterprise connectors work under the hood and can provide workarounds and can explain the product roadmap is essential.

- **Work with Partner Engineers, Google contacts to file bugs:**

  - Know who you will contact and report bugs to if a connector does not work as advertised.

- **Don’t assume that adding third-party data connectors will be easy:**

  - Don’t assume that adding third-party data connectors will be easy or seamless.

  - Lean on your Google reps and refer to the documentation here: [Documentation](https://cloud.google.com/agentspace/docs/connect-third-party-data-source?hl=en).

## **Networking**

Beware of gotchas like timeouts.

Some networking components have default configurations -- for example 30-second timeouts -- that may be non-issues for typical network traffic but may pose issues when awaiting responses from a thinking model.

## **Security**

### Timeline

For a proof-of-concept, if **Personally Identifiable Information (PII)** or **confidential company data** is being used, it's recommended to set up Gemini Enterprise in a **hardened Google Cloud project**. They can harden the project by using the Security Foundation toolkit here: [Security Foundation toolkit](https://cloud.google.com/security/solutions/security-foundation?hl=en)

Following the proof of concept (PoC), it's recommended to implement a Gemini Enterprise instance within the customer's Google Cloud organization. This instance should be configured using the Security Foundation toolkit, along with Google Cloud's best practices and guidelines.

Google Cloud Storage and Google BigQuery data connectors do not come with user-specific access enabled by default. All users who can use the app can access all data connected by these data sources, unless ACLs are enabled, which is covered in the documentation here: [Configure Access Control Lists](https://cloud.google.com/agentspace/docs/identity)

For data access controls to be respected, one-time ingestion must be used. As of this course’s publication, periodic ingestion does not support data access controls. You can find information about one-time ingestion and periodic ingestion here: [Sync from Google Cloud](https://cloud.google.com/agentspace/docs/connect-cloud-storage#:~:text=Data%20source%20access%20control%20is%20not%20supported.%20The%20imported%20data%20can%20contain%20access%20controls%20but%20these%20controls%20won%27t%20be%20respected.)

To guide the secure enablement of data connectors, use the provided data stores checklists in the documentation here: [Checklist for data sources](https://cloud.google.com/agentspace/docs/introduction-to-connectors-and-data-stores#google_data_sources)
