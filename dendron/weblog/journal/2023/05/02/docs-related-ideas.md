---
id: minijsfdl21eswrropmp8jn
title: Docs Related Ideas
desc: ''
updated: 1683044228688
created: 1683042124322
tags:
  - ideas
htag: docs
---

The write the docs conference is coming up this week. Been thinking of various doc related ideas for the conference

My shortlist

- coverage report for documentation #stage.sprout
    - interest: high
    - difficulty: days
    - features:
        - convert markdown into spec
        - verify your doc matches the spec
            - sections
            - headers
            - style
    - analogies: 
        - types systems
        - borrow checker
    - markets:
        - who: doc writers
        - who: open source founder
            - value: 
                - better adoption of open source project
                - less support request
            - metrics:
                - star count going up
                - help request going down
    - competitors:
        - vale
        - grammarly
    
- refactor documentation #stage.seed
    - difficulty: unkown
    - interest: mid
    - features:
        - if doc doesn't match spec, autofix it
    - analogies: 
        - refactoring
            - extract component
            - refactor docs
    - markets:
        - who: doc writers
    - dependsOn: coverage report for documentation

- api reference vs library reference #stage.sprout
    - we have docs based on openapi spec, what about libraries?
    - eg: lodash
    - features:
        - yaml -> function generation
        - docs
        - arguments
        - return values
        - example
            - toggle between languages
        - interpreter (eg. runkit)
        - link to source code
        - link to package manager library

- ctrl f/replace but semantically #stage.seed
    - interest: high
    - what: find all occurences of some {action-with-different-tenses} and replace it

- entity/concept extractor
    - what: extract all entities of the given doc
- taxonomy extractor
    - what: extract taxonomy for doc

- related material #stage.germ
    - what: for each doc, show stream of recent news/updates (eg. discord, stack overflow, etc)
