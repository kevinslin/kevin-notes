---
id: u2xdpkyrxgz7cows09161yp
title: Publishing with Datasett
desc: ''
updated: 1682978944963
created: 1682960190821
htag: vpkg.datasette
public: false
---

Decided to keep a weblog my activites.

This is styled after the weblog of Simon Willison, one of the co-creators of DJango. 
Specifically, this is a fork of [Simon's TIL](https://til.simonwillison.net/) project. 

Steps of forking the project can be found in [[task.2023.04.28.simon-datasette-based-blog.log]]

This post goes over some of the design decisions made during the fork

### Buy, Build, or Fork

In companies, the tradeoff with any software is whether its better to purchast it or build it in house.
The less talked about option is to fork.
I've worked with datasette in the past, respect the work that simon is doing, and since most of my notes are already in a sqlite backend because of Dendron, decided to fork it.

### Reprsenting topics

Simon has the notion of topics - these are tags. Dendron has hierarchies. Figuring out how to merge the two.

Some options:
1. Use tags for my entries
2. Keep hierarchies and make topics reflect that

To do 2, there is the challenge that hierarchies only belong in one place. This was a concious decision on our part.
Alias notes. Lets collapse tags and hiearchies. 

So this post write here is published under `weblog.journal.2023.05.01.publishing-with-datasette`.

I want to relate it to [[vpkg.datasette]]. This is a wikilink on a private note
I also want it to show up under the tag `pkg/datasette`

For now, I've settled on putting it under the `htag` block

### Hierarchy vs Linear Feed

Dendron is hierarchical. This feed is not.
Since its all in sqlite, we can make it hierarchal at some point. for now, going to keep this as is. A linear feed

### Publishing Method

Publishing is based on hiearchies

### Deletion

If there is a file that is not 


<!--|NO_PUBLISH:START|-->
##  Appendix
* [[people.simon-willison]]
* [[vpkg.til-simon]]
<!--|NO_PUBLISH:STOP|-->
