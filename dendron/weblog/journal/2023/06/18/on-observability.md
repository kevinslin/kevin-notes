---
id: frxkty7tuvcy6m526krapk8
title: On Observability
desc: ''
updated: 1687133946114
created: 1687126805893
topic: devops
---

For observability, I'm talking about metrics, logs and traces

In the cloud, there are three primary ways that companies manage observability:
1. Rely on capabilities provided by the cloud vendor (eg. cloudwatch, xray)
2. Build something in house using open source providers (eg. prometheus)
3. Use a vendor  (eg. datadog, splunk)

The common path for most companies is to start with the cloud provider and then transition to an observability vendor.

If the company is an infrastructure company or their observability bill gets high enough, they will go for maintaining an observability stack in house

## On Open Source
For open source solutions, common setups include the following:
- for logs:
    - opensearch/elasticsearch
    - loki (an easier to maintain elasticsearch by grafana)
- for metrics:
    - prometheus, cortex/thanos 
    - clickhouse
- for traces
    - grafana tempo, jaeger

Prometheus by far is the most popular solution for metrics. Main challenge is horizontal scaling. This is where coretx/thanos come in (s3 backends for prometheus).

There are also open source data dog alterntaives. Two YC companies that fall into this batch:
- opstrace: metrics and logs. build on top of prometheus, cortex, and loki. acquired by gitlab.
- signoz: metrics, logs and tracing. build on top of clickhouse.

## Related
* [[task.2023.06.18.read-up-on-opstrace]]
* [[seeds.talks.20230518-datadog-inside-of-aws]]
