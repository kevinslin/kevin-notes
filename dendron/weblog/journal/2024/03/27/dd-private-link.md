---
id: f3vunj91wnnqh5b3wiq0duq
title: Save 90% on Datadog Egress
desc: ''
updated: 1711594545489
created: 1711594313403
topic: datadog
---

If you use Datadog with AWS, here is a simple change you can do to save 90% of your egress fees immediately.

AWS Private Link is a service that lets you send data between two private networks without ever exposing data to the internet.
Private links are region specific - datadog has [private link endpoints](https://docs.datadoghq.com/agent/guide/private-link/?tab=connectfromsameregion) in the us-east-1 and ap-northeast-1 region.
This corresponds to datadog regions us1 and ap1.

Egress on EC2 is normally $0.09/gb on AWS. With private link, this becomes $0.01/gb!

To put this in perspective, ten terabyte of egress would normally cost you $900 from AWS (plus another $1000 of ingress in datadog).
With private link, you will be charged $90 from AWS (your ingress in datadog will still be the same)


