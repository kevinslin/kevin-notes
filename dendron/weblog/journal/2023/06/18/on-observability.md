---
id: frxkty7tuvcy6m526krapk8
title: On Observability
desc: ''
updated: 1687877340204
created: 1687126805893
topic: devops
tags: []
notion: >-
  https://www.notion.so/dendronhq/On-Observability-b347504446344f25afbb1d9c0e05a9e8?pvs=4
---

## What is Observability 
Metrics, logs and traces

## Observability Basics
- [Monitoring 101](https://www.datadoghq.com/blog/monitoring-101-collecting-data/)

## Who uses observability 

### Developers

Generally, full stack developers. Mainly use logs to debug errors or verify new functionality

### DevOps

Use metrics to understand service health metrics. Use logs to triage operational issues. Sometimes uses traces to do performance (generally later stage companies)

### SREs

SREs are closely related to devops but they get paid more. Generally more involved with incident response and managing issues. 
Rely on logs and metrics to root cause issues. 

## What is being observed?

- monoliths on VMs
- container services
- serverless services
- infrastructure

### Monoliths on VMs
- eg. django/rails/nodejs

Relatively easy and well understood

### Container based services
- eg. kubernetes, ecs, nomad, etc

Challenges:
- explosion in logs and metrics
- kubernetes

### Serverless based services
- eg. lambda/api gateway

Challenges:
- explosion in logs and metrics

Vendors:
- sst.dev (easy to deploy and basic monitoring)
- AWS SAM (local debugging)

### Infrastructure
- eg. load balancer, database, etc

Challenges:
- logs need to be combined with application logs
- need to correlate infra metrics with application metrics


## Observability Providers
There are three primary ways that companies manage observability:

1. Rely on capabilities provided by the cloud vendor (eg. cloudwatc)
2. Build something in house using open source providers (eg. prometheus and grafana)
3. Use a vendor  (eg. datadog, new relic)

The common path for most companies is to start with the cloud provider and then transition to an observability vendor.
If the company is an infrastructure company or their observability bill gets high enough, they will go for maintaining an observability stack in house

### Cloud Based Observability (AWS)

- Cloudwatch: metrics
- Cloudwatch logs: logs
- Cloudwatch log insights: query over logs
- Opensearch: logs (faster and more scalable than log insight)
- AWS XRay: Traces

### Open Source Observability
For open source solutions, common setups include the following:
- for logs:
    - opensearch/elasticsearch (defacto standard for a long time, ELK stack)
    - loki (an easier to maintain elasticsearch by grafana)
    - clickhouse (faster aggregation, came from uber)
- for metrics:
    - prometheus
        - cortex/thanos (scale promethesus horizontally)
    - influxdb (smaller player)
- for traces
    - jaeger (standard open source tracing)
    - grafana tempo (new)

Prometheus by far is the most popular solution for metrics. Main challenge is horizontal scaling. This is where coretx/thanos come in (s3 backends for prometheus).

There are also open source data dog alterntaives that attepmt to be an end to end observability platform. 
- opstrace: metrics and logs. build on top of prometheus, cortex, and loki. acquired by gitlab
- signoz: metrics, logs and tracing. build on top of clickhouse.
- grafana: metrics frontend. have not build out an end to end suite for observability with cloud offering

### Vendor Based Observability

- incumbents for everything
    - datadog, splunk, new relic
- mid sized
    - betterstack
    - [papertrail](https://www.papertrail.com/)
- new comers
    - [middleware](https://www.ycombinator.com/launches/Hs9-middleware-a-unified-observability-platform-for-cloud-native-microservices-and-distributed-apps)
    - highlight.io
- one person bootstrapped
    - clouddash (serverless metrics)

## Observability Stack

### Features
Common features for an observability platform 

- metrics, logs, and traces
- alarms and dashboards
- ability to turn logs to metrics
- ability to live tail logs
- lifecycle management of data (active, archive, cold storage)

- advanced
    - build in integration to collect kubernetes data
    - build in integration to collect serverless data (eg. lambda/api gateway)

### Backend
To build an observability platform, you need the following elements:

- metrics backend
- logs backend
- tracing backend
- metrics frontend
- logs frontend
- tracing frontend

- metric client/agent
- logs client/agent
- tracing client/agent
- infrastructure metrics/logs collector 

> A client is language specific SDK that requires a code change to instrument. An agent is a daemon that runs and automatically collects metrics/logs/traces from the system

## Etc

Special purpose monitoring - may or may not be included in general observability platforms

### Breakpoints

Not exactly monitoring but often grouped together.
Putting remote breakpoints in remote services like lambdas and mobile devices.

Examples:
- appspector.com - Mission control, for remote iOS/Android/Flutter debugging
- sst.dev

### Synthetics

Using a remote machine to impersonate user. Meant to provide monitoring from endpoint external to the service that you're running

Examples
- checklyhq.com - Open source E2E / Synthetic monitoring and deep API monitoring for developers. Free plan with 5 users and 50k+ check runs.

### Insights

Using AI to automatically highlight issues. Usually built on top of existing metrics/logs vs a standalone service

Examples:
- datadog watchdog

### Logs/Errors

There's usually been a split between application logs, infrastructure logs, and error logs.
End2end observability platforms do all of it but most providers only provide one of the three. 

Error logs are generally associated with frontend applications. There's some sort of client side error and the stack trace is captured and logged.

Examples:
- [sentry](sentry.io/) (incumbent)
- Logrocket 
- Airbrake.io 

Recently theres been new open source contenders like [highlight](https://github.com/highlight/highlight) (YC).

Error logging is also different from session replay/capture. This is when not just the logs but a screen recording of the session is captured for later analysis.
Incumbent in this space is [fullstory](https://www.fullstory.com/)

### Logs/Audit

There's an entire industry that does logs for compliance (soc2, fedramp, etc)
In AWS, the service that does this is cloudtrail though cloudtrail by itself is not sufficient (you'll also need application level logs).

### Metrics/Uptime

Check if a system is up. 

Use cases:
- cron jobs
- servers
- containers
- apis

Examples:
- deadmanssnitch.com — Monitoring for cron jobs. 1 free snitch (monitor), more if you refer others to sign up
- Pingmeter.com - 5 uptime monitors with 10 minutes interval. Monitor SSH, HTTP, HTTPS, and any custom TCP ports.

### Metrics/Cost

There's an entire industry on monitoring cloud costs. Observability providers like grafana even dedicate specific dashboards for this

## Concepts

### Application Performance Monitoring (APM)

## Further Reading
- [Google SRE Handbook](https://sre.google/sre-book/table-of-contents/): Combines observability with the context of incident response. Industry standard reference
- Opentelemetry: CNCF accepted standard for collecting metrics
- Free monitoring tools for devs: https://github.com/ripienaar/free-for-dev#monitoring

## Communities
- hangops.slack.com
    - #monitoring_love
    - #aws
    - #sre
- coffeeops.slack.com
    - #monitoring
    - #aws
- rands-leadership.slack.com
    - #aws
    - #devops
- cloud-native.slack.com
    - #devops
    - #monitoring
    - #aws 

- Reddit
    - https://www.reddit.com/r/devops/
    - https://www.reddit.com/r/Monitoring/
    - https://www.reddit.com/r/grafana/
    - https://www.reddit.com/r/aws/

## FAQ


## Related
* [[task.2023.06.18.read-up-on-opstrace]]
* [[seeds.talks.20230518-datadog-inside-of-aws]]
- [[scratch.2023.06.25.150715.monitoring-101-collecting-the-right-data]]
- [[ext.google-sre-handbook]]
