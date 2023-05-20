---
id: f4d5p74j0tgemp4tmdx114c
title: Daily Journal
desc: ''
updated: 1684602172909
created: 1684436427516
htag: journal
topic: schemas
---

Had some time to work on my [digital notes](https://github.com/kevinslin/kevinweblog.git) today. 

Objectives in increasing levels of nicheness: 
- have permanent ids for urls
- enable pretty permanent urls
- enable automatic 301 redirects on pretty permanent urls

This is now shipped and you can see the results on this page. 

The url for this page is https://notes.kevinslin.com/pages/journal-public-f4d5p74j0tgemp4tmdx114c
- Only the last `-` delimited component gets parsed to determine the note to fetch (`f4d5p74j0tgemp4tmdx114c` in this case)
- The url itself is a slug made by joining the `{topic}-{filename}-{id}`

If I end up renaming the file (eg. s/public/somethingelse/g), the url woudl change to `https://notes.kevinslin.com/pages/journal-somethingelse-f4d5p74j0tgemp4tmdx114c`. The link will still work as the id portion is constant. The same would happen if I change the `topic`.

The most interesting part is the treatment of redirects. Any url that doesn't match a valid existing `{topic}-{filename}-{id}` path gets a 301 redirect to a valid note url based on the id. The 301 is important as it tells google to transfer any page rank from the previous note into the newly redirected path. 

<!-- [[daily.journal.2023.05.18.public.scratch]] -->
