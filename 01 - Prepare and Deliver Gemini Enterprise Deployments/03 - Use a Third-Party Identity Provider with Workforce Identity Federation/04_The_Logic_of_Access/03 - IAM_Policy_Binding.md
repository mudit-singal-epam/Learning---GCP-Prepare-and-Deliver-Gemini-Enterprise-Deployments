# IAM policy binding

## Learning objectives

By the end of this lesson, you will be able to:

- Construct the specialized `principalSet` IAM string required to grant access to Federated users.
- Differentiate between binding a policy to a specific **Subject** (one person) versus an **Attribute** (a group/category).
- Apply the Principle of Least Privilege by creating granular bindings based on custom attributes.

## The Concept: The Visitor Badge

Alice has passed the IdP check. She passed the Attribute Condition check. She is now inside the Google Cloud ecosystem.

However, by default, she has **0 permissions**. She cannot access projects, list VMs, or read logs.

In standard IAM, you grant roles to an email: `roles/storage.viewer` is granted to `user:alice@gmail.com`

In Workforce Identity, you don't have an email address in the traditional sense. You have a **Federated Principal**. You need a new way to point to Alice.

## The Syntax: The `principal` Protocols

Workforce Identity introduces two new types of IAM Members. You will paste these strings into the "Add Principal" box in the IAM console.

### Targeting a Specific User (Principal)

Use this when you want to give permissions to exactly one person.

- Syntax:

    `principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ID`
- Example:

    `principal://iam.googleapis.com/.../partnercorp-engs/subject/alice@partnercorp.com`

### Targeting a Group (PrincipalSet)

Use this when you want to give permissions to **everyone who shares a trait**. This is the scalable approach.

To give access to everyone in a Workforce Pool:

- Syntax:

  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*`
- Example:

  `principal://iam.googleapis.com/locations/global/workforcePools/partnercorp-engs/*`

To grant access to only those that match a specific attribute value:

- Syntax:

  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`

- Example (The Engineering Department):

  `principalSet://iam.googleapis.com/.../partnercorp-engs/attribute.department/engineering`

**Warning**: You can only use `principalSet` on attributes you explicitly mapped with attribute mapping. If you didn't map `department`, you can't target it here.

## Step-by-step: Security Policy Implementation

Let's implement the security policy for your **PartnerCorp Developers**.

These steps demonstrates how to grant IAM permissions to federated users, groups, or custom attribute sets using the principalSet identifier syntax.

### Step-by-Step Walkthrough

1. **Locate Target Resource:** Select the target GCP Project, Cloud Storage bucket, or BigQuery dataset.
2. **Capture WIF PrincipalSet:**  Go to **IAM & Admin** > **Workforce identity pools** > [**Pool Name**] and copy the WIF PrincipalSet.
3. **Open IAM Permissions:** Go to **IAM & Admin** > **IAM** and click **Grant Access**.
4. **Enter Principal Identifier:** Enter the WIF principal set string:
   - Entire Pool: `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*`
   - Specific Group: `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_NAME`
   - Specific Attribute: `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/attribute.department/dev`
5. **Select Role:** Assign the necessary IAM roles (e.g., `roles/storage.objectViewer` or `roles/discoveryengine.user`).
6. **Save Binding:** Save the IAM policy. Federated users now have immediate access upon authentication.
7. Go back to the WIF Pool and get the identity provider signin URL.

> Note: Specific Groups and Specific Attributes needs configuratins at the Ockta side for attribute mapping for it to translate those values to GCP.

## Best Practice: Abstract vs. Concrete

Why use **principalSet** (Attributes) instead of **principal** (Subjects)?

**Scalability**.

- **Scenario**: PartnerCorp hires 50 new engineers next week.
- **If using Subjects**: You must manually edit the IAM policy 50 times to add every new ID.
- **If using Attributes**: You do **nothing**. As long as their IdP sends **department: engineering**, they automatically inherit the **Log Viewer** role.

**The Golden Rule**: Use **Attributes** for Roles (RBAC). Use **Subjects** only when exceptions are required.

## Troubleshooting

### The Mapped Attribute Check

Before you try to bind a policy, verify your mapping from Lesson 3.1.

- **Mapping**: `attribute.dept = assertion.job_role`
- **IAM Binding**: `.../attribute.dept/developer`

Notice the name change?

- The IdP sends `job_role`.
- But Google's internal name is `dept`.
- Therefore, your IAM binding must use `dept`.
- **Common Mistake**: trying to bind to `.../attribute.job_role/developer`. It will fail because `job_role` is the source, not the destination.

### Delayed validation

**Scenario**:

You paste a **principalSet** string into the IAM console, and it turns red with an error: "Email address or domain not valid."

**Diagnosis**:

The IAM Console's "Add Principal" box validates emails by default. When pasting these long federation strings, the validation sometimes lags or requires you to press "Enter" to confirm the complex string. Ensure you haven't introduced any spaces or line breaks, then give it a bit more time.

## Summary

Congratulations! You have completed **The Logic of Access** module.

- You used **Attribute Mapping** to translate "Foreign Claims" into "Google Attributes."
- You used **Attribute Conditions** to act as a bouncer, rejecting invalid users.
- You used **IAM Policy Binding** to link attributes to permissions.

The system is now fully functional. But what happens when things break?

In the next module, you will explore **Access and Troubleshooting**, focusing on usage for developers and debugging logs for administrators.
