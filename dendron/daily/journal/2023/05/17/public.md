---
id: anpq6f6k8jmby1eciy8zsr2
title: Daily Journal
desc: ''
updated: 1684381307666
created: 1684380089972
htag: journal
---

Been working on building a universal address book that merges information from tools where I have contact information (linkedin, google, hubspot, etc) into a common datawarehouse (postgres) with a common schema. 

Once all contact data has been consolidated, I can dedup & merge information from different sources (eg. linkedin data into hubspot). 

Data in the data warehouse also syncs back to downstream sources.

My use cases for this:
- single source of truth for all my contact data
- automatically dedup and merge information across all contact sources
- run raw SQL against my contact data and be able to update information from contact sources via SQL 
- use analytics tools like metabase to build dashboards against my contact data
- leverage contact data inside of other tools (eg. autocomplete via chrome/vscode/native extension)


