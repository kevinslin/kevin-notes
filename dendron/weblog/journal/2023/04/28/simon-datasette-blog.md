---
id: 4ahj6vy1l4e862ch2l2l16m
title: Simon TIL
desc: ''
updated: 1684601736461
created: 1684296269258
htag: take
topic: dev
---

This is a review of https://github.com/simonw/til

## Code Review
- source: https://github.com/simonw/til/blob/e2e4819d33613410efa533541262599f23fd6223/build_database.py#L32

- datasette
- very simple, single line of python

### Algo
- store text in folders
- go through all text in all folders
    - check if text exists in the db or is different
        - if different, get the html version of the text
- updated the created time and updated time based on the git commit

### Code Snippets

```py
root = pathlib.Path(__file__).parent.resolve()
...
def build_database():
    db = sqlite_utils.Database(repo_path / "tils.db")
    for filepath in root.glob("*/*.md"):
        ...
```

## Thoughts
Like Simon's code for simplicity. See the ReACT implementation. 
Original took a look at this because I was looking to refresh my blog and wanted some inspiration. 

Some changes:
- since my files are in Dendron, already have updated times
