---
id: 7c2253yms78clp5mx92vwvh
title: Log
desc: ''
updated: 1684285684138
created: 1683817362705
---

### 2023-05-16
1. get all aws repos
1. get doc urls of all repos
    - initially use langchain, realize this was overkill, took multiple choices to find given url
    - use serpapi to search google for docs
        - limit to results that have .html (otherwise will get the index page)
    - this had to be retried a few times, flaky internet, use python notebook to do this
1. get toc of all repos
    - do a curl request of well known apis
1. reachitect 

### 2023-05-12

- trying to preview gitbook build locally. this used to work fine bu they've went `notion` and made this no longer a workflow [2023-05-12 06:56]  [^1]
    - theres [instructions](https://til.secretgeek.net/gitbook/use_gitbook_locally.html) to do this still using the gitbook cli but been running into issues with `node-gyp` and an xcode and none of the [suggested fixes](https://github.com/nodejs/node-gyp/issues/569) have helped
    - this is not a hill I want to die on, so moving forward
    - using the `git push` workflow for now

- fix various publishing issues [2023-05-12 07:05]
    - proper h1 titles

- > ASIDE: why is the outline view not showing up in gitbook?
    - gremlins, they are now starting to show up...
    - gitbook requires [minimium width](https://docs.gitbook.com/product-tour/navigation#on-this-page) to show page outline
        - see https://www.notion.so/Gitbook-story-f185468fded342f4b5eac21ba1698115?pvs=4
    - this means people using arc browser witll not be able to see it :(

- generate the sidebar  [^2]
    - manually generate summary file [2023-05-12 07:45]

- > ASIDE: spent 30minutes wrestling with jest & esm. did not get it to function, working without them at this moment [^3]

- setup plausible analytics and custom domain [2023-05-12 16:24]

[^1]: [[task.2023.05.12.get-gitbook-to-work-locally]]
[^2]: [[task.2023.05.12.update-summary-file]]
[^3]: [[jest with esm|task.2023.05.12.jest-with-esm]]

- finish automatically generating sidebar [2023-05-12 10:14] [^2] 
    - interested to see if path from gitbooksummary is relative from root 
        - its not, relative from SUMMARY.md file 

### 2023-05-11
- source: [[task.2023.05.11.extract-other-emphasis-items]]

- Extract admonitions from AWS docs
- Start with `**Notes**`, expand to `**Tips**, **Important**, and **Considerations**`

- All notes rendering on the same page [2023-05-11 10:31]
- HTML and MD render

- Switch interface to be vfile based, allows for writing directories [2023-05-11 13:57]
- Chunk vfiles together in `runBeforeAllWriteHook` instead of hacking `runAfterAllWriteHook` to write files
- Publish to gitbook [2023-05-11 14:58]
