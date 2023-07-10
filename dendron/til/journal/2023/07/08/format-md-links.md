---
id: 9oc3m0rm08k33b7bb3ig2i0
title: Disabling Auto Markdown Link Formatting in VScode
desc: ''
updated: 1688962481316
created: 1688834182242
tags:
  - papercut
traitIds:
  - til
topic: vscode
---


The `Version: 1.80.0-insider Commit: da7f05a70eb760e4ce1fe230ae158ae214433341` of vscode turns `markdown.editor.pasteUrlAsFormattedLink.enabled` on by default. This automatically turns urls pasted into vscode as markdown links. It is trigger happy and also fires erroneously (eg. `Note: key:value ` turns into a markdown link)

Solution is to set `markdown.editor.pasteUrlAsFormattedLink.enabled` to `false`
