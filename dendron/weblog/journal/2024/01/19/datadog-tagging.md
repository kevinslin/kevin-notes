---
id: x3ez5zufcdkzg6rfiymtojv
title: Datadog Tagging Best Practices
desc: ''
updated: 1705690416580
created: 1705690416580
topic: datadog
tags: []
---

Datadog has [unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) where you can define a set of standard tags for your org.

The datadog defaults are pretty good (`service/env/version`) and enough if all you need is correlation between metrics, traces and logs. That said, it does require that you at least configure the agent to emit the correct tags.

To go further and set a standard, I recommend the [AWS tagging guidelines](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) which for the most part maps on to datadog as well.

> NOTE: Where I disagree with the AWS guidelines is that more tags are always better. Too much and it just becomes noise. It's better to have a small set of well understood and standardized tags vs a hot mess of garbage. For datadog, each additional tag incurs extra costs in terms of ingest and storage.

## What to Tag
Before tagging, make sure you have an end goal in mind. Examples include:

- better incident response
- cost tracking 
- security

### Incident Response

During an incident, you want to easily query for impacted or related services and figure out root cause. An `app` tag can be used to track related services.

If you're using k8, this maps on to the `part-of` tag that can be autodiscovered by datadog (though in that case, you should consider remapping it to the `app` tag or standardizing on `part-of` as your application tag).

### Cost Tracking

Ownership tags are a must have if you care about cost tracking. You can accomplish this using a `team` tag. You can then create a dashboard as well as alarms on datadog [usage metrics](https://docs.datadoghq.com/account_management/billing/usage_metrics/) filtered by ownership tags to get a cost breakdown on a per team basis. 

### Security

Security tags are used to restrict access of data to privileged parties. The standard tags for security are `confidentiality` and `compliance` 

Confidentially should be a numeric tag that maps to your organizations data classification levels.

Compliance should be used to enforce specific compliance requirements (eg. `ITAR` tagged assets can only be operated on by US citizens)

For datadog, you can use the built-in [rbac access control](https://docs.datadoghq.com/logs/guide/logs-rbac/?tab=api) to then limit access based on a combination of `confidentiality` and `compliance` (and `team` also depending on your needs). 

## How to Tag

TBD

## Enforcing Tags

TBD
