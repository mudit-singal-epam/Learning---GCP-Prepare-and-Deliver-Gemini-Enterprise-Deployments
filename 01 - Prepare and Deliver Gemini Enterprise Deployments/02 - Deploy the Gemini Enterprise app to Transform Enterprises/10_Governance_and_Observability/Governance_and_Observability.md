# Governance and Observability

As Gemini Enterprise scales across an organization, **maintaining visibility** and **continuous control** is paramount. Governance and observability ensure that your AI deployment remains **secure**, **compliant**, and **performant** while delivering measurable business value.

## Observability

Under the **Configuration tab** of your **Gemini App**, you will find the **Observability tab**. You can turn the following settings on or off.

### Enable Instrumentation of OpenTelemetry Traces and Logs

View **traces**, **spans**, **span** **logs**, and **metrics** associated with your logs in Cloud Logging.

### Enable Logging of Prompt Inputs and Response Outputs

**Cloud Logging**logs the full content of user prompts and responses, including **sensitive data or Personally Identifiable Information** (PII).

To enable this setting, you must first enable **Enable instrumentation of OpenTelemetry traces and logs**.

> ### Google Cloud Logging
>
> Within your Google Cloud project, you can view logs, traces, spans, span logs, and metrics associated with your logs under:
> **Observability/Monitoring -> Logs explorer**

Enabling the **logging of prompt inputs and response outputs** ensures Cloud Logging captures the full content of both user prompts and model responses.

It's important to take note of the following:

* Enabling this setting logs potentially **sensitive data or Personally Identifiable Information** (PII).
* Please ensure you have the necessary **user consents and data handling policies** in place.
* You can **restrict log access** to authorized users only.

> **Enable instrumentation of OpenTelemetry traces and logs** setting.

To learn more about the specific information logged visit the following link in the official Google Cloud documentation: [Access Gemini Enterprise usage audit logs with Cloud Logging](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs).

### Summary

Governance and Observability are vital for secure Gemini Enterprise scaling. Observability features enable two key logging settings: OpenTelemetry instrumentation (traces, logs, and metrics) and full prompt and response logging (including PII). The latter requires the former and necessitates user consent and restricted log access due to sensitive data. Logs are viewed in Google Cloud's Logs Explorer.
