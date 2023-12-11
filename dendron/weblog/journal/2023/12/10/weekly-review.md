---
id: o9774hn913f6rht4l64kbc2
title: Weekly Review
desc: ''
updated: 1702269756484
created: 1702267881117
topic: journal
---

## [Show HN: Beeper Mini – iMessage client for Android | Hacker News](https://news.ycombinator.com/item?id=38531759)

Eric Migicovsky (founder, formerly founder of Pebble), launched an android chat app that can send and receive messages to an iPhone as [an apple device](https://github.com/JJTech0130/pypush). Apple finds a way to block them three days later. The Beeper team is now working on a patch to undo Apple's block. It's a real time cat and mouse escalation between two tech companies. 

Beeper Mini will be a future case study for platform risk. It's inconceivable that Apple would let a third party company use their proprietary iMessage network and it does seem that they have enough information at hand to detect Beeper traffic from regular iMessage traffic. And even if Beeper finds a way to surmount the technical challenges, it will probably face legal challenges from the big Apple. 

That said, as a startup in a anti-big tech climate, Beeper has the advantage in the court of public opinion. There's no better way of getting attention then picking a fight with the biggest figure in the room. But this might not be a fight that they can win. 

## [Rethinking serverless with FLAME | Hacker News](https://news.ycombinator.com/item?id=38542764)

Instead of rewriting applications to work within the constraints of a vendor specific serverless environment, the FLAME pattern advocates for applying the `fork` function to the cloud. This is to say - only delegate to a serverless environment the execution that needs to be massively scaled out, and in that case, copy the entire app + state so that no extra gymnastics is necessary to run the code. 

I think serverless is both overhyped and under utilized. Overhyped because of its many constraints and limitations but under utilized as companies that can use it well can have orders of magnitude differences in overhead cost as well as scaling capabilities. 

Serverless in some sense can be a cake that you can eat as well in the cost vs performance tradeoff but it requires a good understanding of servers, their limitations, and how to translate that into serverless. 
