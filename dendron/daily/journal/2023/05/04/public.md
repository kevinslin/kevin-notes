---
id: pqvq6wtxl0lfk5x22mpx5io
title: Dendron Redeployment Challenges
desc: ''
updated: 1684602274982
created: 1683254761339
htag: journal
topic: dev
tags: []
---

## Goals
- [ ] aws reference guide
- [w] republish dendron
- [x] reach out to 3 people

## Notes

Ended up not being able to work on the reference guide today. Decided to redeploy Dendron today and pull in some dependabot updates. 
Mostly aimed at kicking the tires of running a deployment after 5 months of inactivity. 

This proved more difficult than expected - our last project was an incomplete transition to bundle sqlite with Dendron. 
This meant downloading platform specific binaries of [[vpkg.node-sqlite3]] and doing targeted builds for each platform for vscode. 

We modified github actions to do this and build 32/64/arm versions of all platforms that are supported by vscode. Unfortunately, this was only tested on the darwin platform. The binaries for both linux and windows had issues and these became apparent after publishing and users of those platforms reporting issues. 

I assumed the work we'd done prior basically worked and just required deployment - this was a bad assumption on my part. 
I should have verified that the platform specific builds worked on different platforms. 

