---
id: e5p7gvonqhpz1auqjcszm6n
title: Vector Gotchas
desc: ''
updated: 1697334624891
created: 1697334410221
tags: []
topic: o11ty
---

Some sharp edges when using vector:
- when using the `reduce` transformer, you can't applya `merge_strategy` on nested fields. this is a bug and theres an open [issue](https://github.com/vectordotdev/vector/issues/17637) on it
