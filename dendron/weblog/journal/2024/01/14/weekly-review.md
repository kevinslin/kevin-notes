---
topic: journal
id: ov4mpcgdpgmjm7k3yux7z6a
title: Weekly Review for 2024-01-14
desc: ''
updated: 1705209310858
created: 1705208203310
---

### [How Adobe is managing the AI copyright dilemma, with general counsel Dana Rao — Decoder with Nilay Patel — Overcast](https://overcast.fm/+QLduCUFk8)

the failure of the $20 billion Adobe Figma deal sets a stark precedent for potential m&a moving forward.

the deal was held up by European regulars that wanted adobe to prove the deal wouldn't harm **future** competition.
m&a usually gets blocked for anti-competitiveness in the **present** - this was the first time that the concept of "future competition" was both introduced and used as grounds to block a deal.

regardless of what you might have felt about adobe, setting a precedent for blocking mergers due to things that haven't means that m&a is that much harder, if not out of the picture entirely, for late stage startups. this could not have come at a worst time as these are the same startups that are now underwater due to changes in interest rates and massive cuts in valuations 
jkk

### [#324 – Daniel Negreanu: Poker — Lex Fridman Podcast — Overcast](https://lexfridman.com/daniel-negreanu/?utm_source=rss&utm_medium=rss&utm_campaign=daniel-negreanu)

<!-- https://www.notion.so/324-Daniel-Negreanu-Poker-Lex-Fridman-Podcast-Overcast-0cc3810a5edf497cb8868e53b937a8ff?pvs=4 -->

poker has many analogies to life. there is both skill and luck. skill comes through in the long run but has to be backed by consistent training and mental dicipline. 

daniel talks about a poker hand as not a single hand but representing a range of hands. that is to say, based on whats on the table and play history, this dictates the range of hands the player has and the optimal moves to make at any given point. 

translated into life, every decision is not a binary choice but represent a range of possibilities. the outcome of any individual decision is hard to gauge but there are more optimal ranges of decision spaces for one to get into.

### [Removing data transfer fees when moving off Google Cloud](https://cloud.google.com/blog/products/networking/eliminating-data-transfer-fees-when-migrating-off-google-cloud/)

google cloud removing egress fees when migrating off google cloud is nice PR but costs them little and doesn't actually address the problems with egress and vendor lock in.

some background - in the cloud, ingress is cheap (usually free) but egress is not (eg. for AWS ec2, this starts at $0.09/GB)
this is often used as an example of vendor lock in - its cheap to put data in but expensive to get it out

the role of egress in the role of cloud migration is negligible in the vast majority of cases - its usually a small multiple of what you pay for storage and is going to be miniscule compared to the cost of the engineering effort needed for the migration. 

lock in happens more as a result of avoiding data transfer rates between clouds - that is to say, if you're running a service on one cloud, you're incentivized to run all downstream services on the same cloud to avoid transfer rates

google cloud's "no transfer fees" only apply when you commit to moving EVERYTHING off google cloud in a 60 day time period. this is problematic because:
1. when companies migrate, they don't typically migrate everything. there's usually a subset of legacy workloads that is not worth the effort to move
2. even if the intent is to migrate all services, you probably still want to leave some service on standby in case regressions come up during the migration
3. 60 days is not a lot of time to migrate clouds if you're already entrenched

