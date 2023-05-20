---
id: 5m0ttcdz94n75rgxo4ujyoh
title: Gpt Link Organizer
desc: ''
updated: 1684601808456
created: 1683902204999
tags: []
url: ''
date: ''
original_vault: kevin-public
public: true
htag: til
topic: llm
---
You can use GPT to organize links

## Prompt 

```md
Add markdown links to terms that they match up with

## Example
text="""
- Dev
    * Getting started
"""

Links:
ecs.account-settings.md
ecs.clusters.md
ecs.container-agent.md
ecs.container-instances.md
ecs.getting-started.md

output="""
- Dev
    * [Getting started](./ecs.getting-started.md)
"""

## End Example

text="""
- Dev
    * Getting started
    * Developer tools overview
    * Account settings
    * Tutorials

- Topics
    * Clusters
    * Task definitions
    * Container instances
    * Container agent
    * Scheduling tasks
    * Services

- Common
    * Resources and tags
    * Monitoring
    * Working with other services
    * Troubleshooting
"""

Links:
ecs.account-settings.md
ecs.clusters.md
ecs.container-agent.md
ecs.container-instances.md
ecs.developer-tools-overview.md
ecs.getting-started.md
ecs.monitoring.md
ecs.resources-and-tags.md
ecs.scheduling-tasks.md
ecs.services.md
ecs.task-definitions.md
ecs.troubleshooting.md
ecs.tutorials.md
ecs.working-with-other-services.md
```

## Response

```md
- Dev
    * [Getting started](./ecs.getting-started.md)
    * [Developer tools overview](./ecs.developer-tools-overview.md)
    * [Account settings](./ecs.account-settings.md)
    * [Tutorials](./ecs.tutorials.md)

- Topics
    * [Clusters](./ecs.clusters.md)
    * [Task definitions](./ecs.task-definitions.md)
    * [Container instances](./ecs.container-instances.md)
    * [Container agent](./ecs.container-agent.md)
    * [Scheduling tasks](./ecs.scheduling-tasks.md)
    * [Services](./ecs.services.md)

- Common
    * [Resources and tags](./ecs.resources-and-tags.md)
    * [Monitoring](./ecs.monitoring.md)
    * [Working with other services](./ecs.working-with-other-services.md)
    * [Troubleshooting](./ecs.troubleshooting.md)
```
