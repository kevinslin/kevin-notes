---
id: ztuty6dr0sxn7f2cyacc0tt
title: Weekly Review
desc: ''
updated: 1686516376326
created: 1686515517693
topic: journal
tags: []
---

Second week after starting the pivot in earnest. 

Priorities this past week:
- customer interviews (seed and series A startup founders building on top of AWS)
- cofounder matching
- brainstorm ideas

I'm currently focused on the problem space of unlocking the cloud for developers. I'm not the first to do this but its a space where is still no end of pain points. 

While doing interviews, I've also been experimenting with quick prototypes for MVP services to get quick feedback.

Got the domain `nimbus.dev` to build a cmd+k extension for AWS. Found someone else already did something similar (https://cloudtempo.dev/). After trying it out, realized it wasn't really solving a problem that I would pay for.

My other prototype is an `imagevault.io` - this is a service to host public private images. The problem is for folks that use markdown as their knowledge base and git as version control. You want to have images but you don't want to check them into version control. You also want images to be private. A niche market but building this end to end service is also a good trial run at building an authenticated API first service on AWS.

The top pain points that stand out:
- complexity of specific AWS services (eg. cognito, api gateway, etc)
- paradox of choice: there are over a dozen different ways of hosting a private image on AWS 
- managing config and secrets for CDK

Otherwise, things I've been reading:
- Apple Launches the Vision Pro. My last team at Amazon prototyped experiences with the hololens. It did not get very fear. Apple has made the first version of mixed reality/"spatial computing" device that I find actually compelling 
<!-- > https://www.notion.so/Vision-Pro-06947aff68854b88ae10cd7c6bf07ca7?pvs=4 -->
- Google automatically lowers the quotas of some customer causing an outage. Some things never change... 
<!-- > https://www.notion.so/GCP-automatically-lowered-our-quota-caused-an-incident-and-refused-to-upgrade-Hacker-News-157e7b7aef29469e846fe59ebfae3846?pvs=4 -->
- AWS has officially retired its github documentation. A shame as I just built a project around extracting AWS docs...
<!-- https://www.notion.so/Retiring-the-AWS-Documentation-on-GitHub-Hacker-News-67c268b70b9c4476bccd9f5a20d385d4?pvs=4 -->

<!-- [[pkg.aws-doc-extractor]] -->
<!-- [[co.cloudtempo]] -->
