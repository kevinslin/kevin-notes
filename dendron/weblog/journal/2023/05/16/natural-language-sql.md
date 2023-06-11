---
id: 5zhh9eoljlajaq56irv1qy9
title: Natural Language SQL
desc: ''
updated: 1684603588177
created: 1684253612262
htag: ideas
topic: schemas
tags: []
---

Imagine if you could query your knowledge base with SQL. 

```sql
select n.*, s.*, ... from notion n where n.person = "jonny apples" join slack s on n.person = s.person
```

## Context
Started listening to [Lenny's Podcast](https://www.lennyspodcast.com/) to get a sense for how great PMs think about product. A question I particularly like is about the speakers favorite interview questions. 
My recent favorite is from from Laura Modi (Bobbie) - "Teach me something" 

My workflow is to listen to podcasts on overcast and then share it to notion if there is something noteworthy. I will add the note in the comments. 
I recently had a use case of compiling all such interview questions and was looking for a way of extracting this information from notion.

> ASIDE: Notion's API has no `LIST` method for any of its entities, to get documents, you need to use the `search` API 

Looked into pre-built ways of getting the data.

- airbyte: no comment support
- notion (built-in zip): no comment support
- metano: they use the airbyte container, so same limitations apply

The next step of this project would be to ingest comments, probably by forking the airbyte notion connector. But this was too much of a lift given a passing curiosity so I've settled on recording the progress here. 

Really, what I want at the end of the day is a natural language SQL interface over my notion so I can do something like the below:
```sql
select '%interview questions%' from notes where title LIKE '%lenny podcast%'
```
