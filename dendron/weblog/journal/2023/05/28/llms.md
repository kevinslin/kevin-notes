---
id: ig8gvdgtu8n0lbwqork5f0p
title: Some notes on code generation
desc: ''
updated: 1685330208836
created: 1685329534405
topic: llm
---

### Use typed function interfaces

Prompt for shared libraries

```diff
  Now that we have a list of files, we need to understand what dependencies they share.
  Name and briefly describe what is shared between the files we are generating, including exported variables, data schemas, and function signatures.
  Exclusively focus on the names of the shared dependencies, and do not add any other explanation. 
+ For function signatures, include the function name and the input and output parameters. Add type annotations to the function signatures
```

```diff
-1. adjustHeadingLevel (function) - exported from utils.ts, used to adjust the heading level of the selected text.
+- adjustHeadingLevel function signature: adjustHeadingLevel(text: string, adjustment: number): string
```


### Call out missing dependencies 

```md
a vscode extension that lets the user adjust the heading level of the selected text. it should have three commands: increase heading level, decrease heading level, and set heading level

Important details:

- make sure the following files are present:
    - tsconfig.json
    - .gitignore
- created a shared `utils.ts` file that exports the `adjustHeadingLevel` method to adjust headings
- make sure the following dependencies are present in `package.json`
    - vscode-test version `1.6.1`
    - `@types/mocha` dependency
- make sure to include `.vscode/launch.json` as one of the mandatory files
    - it should have a "extensionHost" launch task
    - it should have "--disable-extensions" as one of the "args"
```

### Specify unit test

Prompt
```diff
    - it should have a "extensionHost" launch task
    - it should have "--disable-extensions" as one of the "args"
+ - make sure that there are unit tests for the vscode extension
```

<!--|backlinks:[[task.2023.05.27.smol-ai-part-2.log]]|-->
