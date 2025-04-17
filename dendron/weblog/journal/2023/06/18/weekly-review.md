---
id: u10mbsa9gg414yfi8nkzf1m
title: Weekly Review for 2023-06-18
desc: ''
updated: 1687147664562
created: 1687145068171
topic: journal
tags: []
---

Third week after the pivot. How time flies.

Priorities this week were split between more customer interviews and cofounder dating. 

Spent the last week exploring the PaaS on top of IaaC model. The space is crowded. [[co.nullstone]] and [[co.flightcontrol]] currently come closest to my vision of a simple cloud platform. They are both new YC minted startups founded within the last year. Neither have SOC2 compliance and both ask for `AdministratorAccess` which is a no go for many larger companies. 

## What I'm reading

### Obsidian Copilot: Have GPT help you write. 
- [Link](https://www.notion.so/Obsidian-Copilot-A-Prototype-Assistant-for-Writing-and-Thinking-Hacker-News-6ddf39f547c249dd941ddb4b3ba2f527?pvs=4)

It seems every note taking tool is adding GPT integration. Currently, I find LLM models to not be great at producing good content. They are effective however, in brainstorming ideas and helping find relevant notes.

Related:
* [[co.mem]] 
* [[groups.every]] 


### DevOps Is Bullshit (2022) 
- [Link](https://www.notion.so/DevOps-Is-Bullshit-2022-Hacker-News-7d9abc4734654692bb5753f7c5e94322?pvs=4)


Agree on all counts. But what are we going to do about it? 

Related:
* [[co.massdriver]]

### No, you don't need to test every line of your CDK application 
- [Link](https://www.notion.so/No-you-don-t-need-to-test-every-line-of-your-CDK-application-theburningmonk-com-d2e2dbb78e604c6d97874b94fe2ffdba?pvs=4)

When it comes to infrastructure, what is the role of unit test? Since infrastructure code has minimal or no business logic, what value do unit tests add? 

Most examples that people have (eg. tags, security policies, etc) fall under the provenance of **governance**. Since these rules apply on an organization level, it makes more sense to enforce them using organization wide checks (eg. Amazon Config, SCP policies, etc) vs doing the tests on the infrastructure level

Related:
* [[vpkg.null-label]]


