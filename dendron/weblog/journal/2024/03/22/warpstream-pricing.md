---
id: wp02ox8e4mh8ltyu34hj880
title: Warpstream Pricing
desc: ''
updated: 1711408834899
created: 1711127361027
topic: review
---

Been spending a lot of time studying pricing pages as we're working on creating a public one for [Nimbus](https://nimbus.dev/).

I really like the pricing page by [WarpStream](https://www.warpstream.com/pricing), for having both technical depth as well as being optimized for sales.

For context, Warpstream is a "a drop-in replacement for Apache Kafka, designed from the ground up to minimize costs and operations"

What I liked about their pricing page:

1. Detailed cost estimation
2. Immediately answering the main question
3. Effective competitor questions


### 1. Detailed Cost Estimation

Most cost estimators I see are a single slider with a number that goes into no detail for how that number was derived. Warpstream publishes all their assumptions and gives a detailed cost breakdown based on them. Some examples of assumptions:

> - ~10 MiB/sec of compressed write throughput per CPU core can be achieved for both WarpStream Agents and Kafka Brokers.
> - We assume a 5:1 compression ratio.
> - Both Kafka and WarpStream utilize highly available three availability zone deployments.
> 
> ...

The explanations are enough to assure me that Warpstream didn't just cherrypick settings to make their costs look good. 

### 2. Immediately answering the main question

Warpstream offers kafka at a 80% discount and the number one question on my mind is how they do this. They address this in the FAQ.

> WarpStream is compatible with the Apache Kafka® protocol, but we are not running Kafka. Instead, we run a stateless Agent that has no local disks, and writes directly to object storage, which avoids 100% of cross-AZ replication charges. These stateless Agents are also much easier to operate than Kafka brokers, so you can drastically reduce the amount of time that you spend managing your streaming infrastructure by switching to WarpStream. 
> 
> {Half a page of additional context}...


The tldr: they build a cloud native service that uses object store as the backend. This avoids managing a whole lot of state and gets replication for free. They are also clever during service discovery to make sure that read/writes don't incur cross-az traffic costs. They go into enough detail that as an engineer, I can understand how they achieve their savings.

### 3. Effective competitor questions

"Competitor Questions" is a term I use when a service lists questions that are clearly a shot at showcasing the weakness of competitors. For example - newrelic's [pricing page](https://newrelic.com/pricing) has a bit about "Do you charge per host". This is aimed at datadog and other competitors that have per host pricing which new relic can happily answer **no** to.  In turn, the rest of the industry has a question in their FAQ about "Do you charge per seat"...

WarpStream has the following competitor questions which are all properties of vendors hosting a traditional kafka service:

- Is replication included in WarpStream's storage pricing?
- Does WarpStream charge me for the number of Agents that I am running?
- Does WarpStream charge for partitions?
- Is there a limit on the number of partitions per Agent?

### Parting Thoughts

My last though is not specific to anything about the pricing page but rather a call out that I have a soft spot for cloud native service. Now I am biased given [my background](https://www.linkedin.com/in/kevinslin-nimbus/details/experience/) but I'm a firm believer that the **decoupling of compute and storage** in the cloud is the **most effective means** we have today for **achieving scale at cost**. A nice side benefit of this decoupling, once you put in the engineering effort, is that you get a lot of things for "free" (eg. no need for replication, elimination of "data nodes", radically simpler architecture, etc)
