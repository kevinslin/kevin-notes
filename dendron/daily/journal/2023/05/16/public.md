---
id: zckio8docgnws69fj5m9tcy
title: Daily Journal
desc: ''
updated: 1684298494711
created: 1684298143071
htag: journal
---

Experimenting with using langchain and jupyter notebooks for ad-hoc tasks. 

For example, matching aws git repositories with their corresponding services. 
This didn't require langchain - just needed semantic search. Since I already had langchain setup, it was simple enough to simply create a local chroma index of aws git repositories and then run it against service names. 

Excel is powerful because you don't need much ceremony to start getting value out of it. Copy and paste some values and you're ready with formulas. 

Code is harder to leverage in this fashion. In part, this is dictated by the language. It's hard to imagine anyone "quickly whipping together" java or c++ for something that might take a few minutes to do. 

But this is something you can do with "scripting languages" like python and nodejs. Add in GPT's ability to zero shot generate most of it, this means that scripting becomes almost real-time in the same sense that image generation is. 

But does this have to end with scripting? What if leveraging LLMs becomes as practical as excel?
