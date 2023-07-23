---
id: ob7jrgaaarj3xmb18goa6mv
title: Weekly Review
desc: ''
updated: 1689515807637
created: 1689515241820
topic: journal
---

Published a [pricing comparison](https://bit.kevinslin.com/p/youre-paying-too-much-for-cloudwatch) between cloudwatch logs, datadog, and a homegrown solution using firehose/s3/athena this week. 

I knew that the difference would be stark but the actual results were still surprising to me. When compared to datadog, querying logs using s3/athena is not 50% cheaper, or even 90%, it is 98% cheaper without any additional optimization or tuning. 

You might not get all the nice things that datadog provides out of the box (mainly correlation with traces and metrics and the single pane of glass) but at some point, you have to ask yourself if that's worth the crazy margins. 

### Understanding Kafka with Factorio
- url: https://www.notion.so/Understanding-Kafka-with-Factorio-by-Ruurtjan-Pul-Medium-faeec3e9c3b94e4da0460760221eec22?pvs=4

This article reminds me that I've been meaning to write an article explaining how "The Darkest Dungeon" is actually a game about founding a startup. 

Conquering the darkest dungeon is having a successful outcome. The intermediary dungeons are the intermediary stages of a VC backed company (seed, A, B, etc).

Wandering through any particular dungeon, you build up stress in both cases. Have too much stress and you will get afflictions (eg. burnout). To keep the stress at bay, you need ~~torchlight~~ momentum. The more of it you have, the more slowly stress builds and the easier it is to ~~fight~~ grow your market.

For particularly long ~~dungeons~~ stretches, you need to camp and regroup at certain checkpoints to recover sanity and stress. 

A full writeup to be done at a later date.
