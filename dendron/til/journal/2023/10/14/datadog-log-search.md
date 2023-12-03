---
id: b0hinj9ypg1hvmp5arfge1v
title: Datadog Log Search
desc: ''
updated: 1701577319949
created: 1697341393003
tags: []
topic: o11ty
---

## Syntax for searching within an array of objects
 
```
@{PATH_TO_ARRAY}.{PATH_TO_ARRAY_OBJ_PROPERTY}:"foo"
```

Given the following data
```json
{
    "entries": [
        {
            "value": "foo"
        },
        {
            "value": "bar"
        }
    ]
}
```

Search for `entries` that contain the `value:foo`
```
@entries.value:"foo"
```
