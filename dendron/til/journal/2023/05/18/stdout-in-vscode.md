---
id: e6j59s5796nonnmb2aw8508
title: Stdout in Vscode
desc: ''
updated: 1684601764472
created: 1684447884052
tags: []
url: ''
date: ''
htag: til
hierarchy: vpkg.vscode.qa
topic: vscode
---

To get standard out when debugging nodejs, require the following settings:

```json
  "configurations": [
      "console": "internalConsole", 
      "outputCapture": "std",
  ]
```

<!-- [[vpkg.vscode.qa]]  -->



