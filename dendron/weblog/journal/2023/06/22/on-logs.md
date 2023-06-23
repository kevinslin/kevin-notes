---
id: 9nf0hva0ezg3q0le4tq5skr
title: On Logs
desc: ''
updated: 1687527915594
created: 1687494535155
---

## What are logs
- logs are one of the pillars of the modern observability stack (the other two being metrics and traces)
- get fine grained visibility into the system
- arguably, logging most important, you can work backwards to traces and metrics from logging
- this is especially true for microservices - more services, more logs

## Why log
Main use cases:
- detect errors
- test features
- diagnose customer issues
- incident response

Other use cases:
- derive operational metrics 
- derive business metrics (this one is fun if you don't realize its happening)
- performance analysis
- request tracing

## Challenges with Logs
- storing
- transport
- archival 
- access
- stability

## Logging on AWS

### Pre 2014
- infrastructure logs go to S3
- application logs had no native solution

### 2014
- Jul 10, 2014: [Launch](https://aws.amazon.com/about-aws/whats-new/2014/07/10/introducing-amazon-cloudwatch-logs/) of Cloudwatch Logs - an AWS native application logging solution
    - No real filtering capabilities, to query logs, you still need to use another service (eg. elasticsearch)

### 2018
- Nov 27, 2018: [Launch](https://aws.amazon.com/about-aws/whats-new/2018/11/announcing-amazon-cloudwatch-logs-insights-fast-interactive-log-analytics/) CloudWatch Logs Insights
    - allows exploration and analysis of logs

### 2023
- Jun 6, 2023: [Launch](https://aws.amazon.com/about-aws/whats-new/2023/06/live-tail-amazon-cloudwatch-logs/) Live tail
    - view logs in real time
    - believe that logs are made available ahead of cloudwatch logs (?)

## DX for (Application) Logs on AWS

### Pre 2014
- non-existant

### 2014
- click through console to get to logs

### 2018
- piece together cw log insight query 

### 2023 
- use case of live debugging made easier with live tail

<!-- > NOTE: in terms of **new log related cloudwatch services**, AWS has released about one every four years. calling a new log service in 2027! -->
