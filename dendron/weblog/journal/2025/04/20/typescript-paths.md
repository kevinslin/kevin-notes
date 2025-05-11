---
id: yzgp0lptheak55c8in0r43u
title: TypeScript Paths
desc: ''
updated: 1746922432135
created: 1745187184608
topic: dev
---

According to the [official typescript docs](https://www.typescriptlang.org/tsconfig/#paths), `paths` is **a series of entries which re-map imports to lookup locations relative to the baseUrl if set, or to the tsconfig file itself otherwise.**

A common use case is rebinding long javascript imports into shorter ones. For example, take the following configuration:
```ts
compilerOptions: {
  "paths": {
    "@/*": [
      "src/*"
    ]
  },  
}
```

This allows you to map longer file imports into shorter ones. Say you're importing something from `src/bar/one/two/three/utils.ts`
```ts
// before
import foo from "../../../../src/foo"

// after
import foo from "@/foo"
```

There is an important caveat at the bottom of this entry that is easily missed.

> Note that this feature does not change how import paths are emitted by tsc, so paths should only be used to inform TypeScript that another tool has this mapping and will use it at runtime or when bundling.

This means that when transpiled to javascript, we get the following code:
```js
const foo = require("@/foo")
```

Note that the path never gets translated back into the original relative path, instead the ts compiler directly copies the re-mapped import path into javascript which leads to an import error. 

The solution is to require a separate `module-alias` module. This needs to be imported at the entry point of you script

```ts
const moduleAlias = require('module-alias')
...
```

You then also need to add a special directive in `package.json` that copies over the `paths` mapping from `tsconfig.json`
```json
  "_moduleAliases": {
    "@": "./src/"
  },
```

This problem gets compounded if you also use [Jest](https://jestjs.io/) or [webpack](https://webpack.js.org/) which also have separate module resolution systems. 
Shudder forbid you try to debug this in vscode with a custom `launch.json` to step through a jest test 🫣
