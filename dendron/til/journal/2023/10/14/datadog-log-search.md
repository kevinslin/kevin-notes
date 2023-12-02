---
id: b0hinj9ypg1hvmp5arfge1v
title: Datadog Log Search
desc: ''
updated: 1697341493184
created: 1697341393003
tags: []
topic: null
---


### search within an array
```
@{myarray}.{key}:"foo"
```

- data
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

- query: match
```
@entries.value:"foo"
```

- query: nomatch
```
@entries.value:"somevalue"
```
