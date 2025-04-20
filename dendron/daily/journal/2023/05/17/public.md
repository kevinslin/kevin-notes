---
id: anpq6f6k8jmby1eciy8zsr2
title: CRM Data Syncing Architecture
desc: ''
updated: 1684602154546
created: 1684380089972
htag: journal
topic: schemas
tags: []
---

Been working on a new project involving syncing data from various CRMs into a datawarehouse and then syncing that data back into said CRMs. 

While the data is inside the warehouse, a user should be able to edit the individual entries and have them synced back to the CRM. At the same time, we also want users to still be able to edit entries in the CRMs directly. We want to do this without creating an endless loop of updates. 

I got inspired by the redux architecture and decided to model this as a "unidirectional data flow" problem. Data only flows in one direction and is never mutated from inside the db. 

That means the following pipeline:
```
- source data -> airbyte (etl) -> datawarehouse (postgres) -> dbt -> hightouch (Retl) -> source data
```

I have a dbt transformation that merges all contact data into a single table, with properties from the same user merged by last updated time across different CRMs. 

The main challenge involves allowing for updates from the datawarehouse (or in my case, retool on top of the warehouse) without mutating the data. 
