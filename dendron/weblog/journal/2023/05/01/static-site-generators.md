---
id: s9t8fl6ckisxy9e8id7jqun
title: Some thoughts on static site generators
desc: ''
updated: 1684296891864
created: 1683003170608
tags:
  - status.draft
  - stage.seed
htag: take
---

There are a lot of static site generators in 2023. 
According to the [JamStack Page](https://jamstack.org/generators/), there are over 300 of them 🤯

I have used about a dozen over the years to host various things (and experimented with a dozen more). These are listed below:
- jekyll 
- gollumn
- gitbook
- hugo
- eleventy
- metalsmith
- middleman
- gatsby
- docusaurus
- nextjs

Websites started off as a static site. Think dreamweaver, geocities and the days of handcrafting HTML files. 

As more people came online, people wanted to build more ~~complicated~~ featureful systems (eg. comments, user accounts, etc) which led to the rise of content management systems (CMS) like wordpress (of which [43% of the internet](https://colorlib.com/wp/wordpress-statistics/) runs on)

As yet more people came online and technology evolved, people found issues with maintaining and scaling these large CMS systems and harkened for the simpler times of static pages. 

And thus, came static site generators (SSG)  that promised the best of both worlds - the simplicty of static pages with many of the features of large CMS systems. 

SSGs were made possible with rapid ~~consolidation~~ advancement of browser technology and javascript, whichh made it possible to implement server side features on the frontend. Static site generators generally work by transforming ~~markdown~~ plaintext into HTML, CSS & Javascript. They also incorporate frameworks like React and Vue. 

Funny enough, we are also now seeing a move back to server side applications with server side rendering (SSR) as developers realize that executing all logic on the client side could lead to long load times and bad SEO due to javascript heavy content not being well indexed by search engines. 

Bundling and unbundling. Client side and server side. Everything old is new again. And the cycle continues
