---
id: v4nk0oga2gx75dzpmnhmpv4
title: Pruning (git) history
desc: ''
updated: 1684688533786
created: 1684688396721
---

## Context
Realized my git repo was taking a while to clone so looked to prune it. 
Asked chat gpt for a git command to locate git objects by file size. 
It came up with this beauty (had to do a little fine tuning on the initial result because all mac unix utilities are horribly out of date)

```sh
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {print substr($0, 6)}' | \
  sort --numeric-sort --key=2 | \
  cut -f-12,41- | \
  numfmt --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest
```

Truncated output running against my notes repo:
```
...
45fd38e  7.6MiB notes/Notes & Settings
25b23e7  8.2MiB .dendron.cache (conflicted copy 2021-12-06).json
bfccf6f   71MiB assets 2/images/10008_.mkv 
```

Had some dropbox merge conflicts as well as some media assets in my repo back from the old days. 
All these files are already deleted by still exist in my git history. 

I used [BFG Git Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/) to prune them from the history.
Git has a built-in mechanism for this known as `git-filter-branch` but here lie dragons as the command is notoriously easy to mess up and takes a long time to wrong.
BFG is the faster and simpler alternative that allows you to prune history in 4 steps.

1. Clone repo
    ```sh
    $ git clone --mirror git@github.com:kevinslin/***.git
    ```
2. Strip past blobs
    ```sh
    $ java -jar bfg-1.14.0.jar --strip-blobs-bigger-than 5M ***.git

    Using repo : /Users/kevinlin/tmp/***.git
    Scanning packfile for large blobs: 58185
    Scanning packfile for large blobs completed in 601 ms.
    Found 6 blob ids for large blobs - biggest=74909145 smallest=7395974
    Total size (unpacked)=114709406
    Found 14070 objects to protect
    Found 2 commit-pointing refs : HEAD, refs/heads/master

    Cleaning
    --------

    Found 3179 commits
    Cleaning commits:       100% (3179/3179)
    Cleaning commits completed in 15,132 ms.

    Updating 1 Ref
    --------------

            Ref                 Before     After   
            ---------------------------------------
            refs/heads/master | 784ebfc9 | 6c6b87dc

    Updating references:    100% (1/1)
    ...Ref update completed in 26 ms.

    ...

    Deleted files
    -------------

            Filename                                                                      Git id            
            ------------------------------------------------------------------------------------------------
            .dendron.cache (Kevins-MacBook-Pro.local's conflicted copy 2021-07-08).json | 50ccb5e2 (7.1 MB) 
            .dendron.cache (Kevins-MacBook-Pro.local's conflicted copy 2021-07-29).json | 061f830b (7.4 MB) 
            .dendron.cache (Kevins-MacBook-Pro.local's conflicted copy 2021-11-08).json | 8aa72e90 (7.6 MB) 
            .dendron.cache (Kevins-MacBook-Pro.local's conflicted copy 2021-12-06).json | 25b23e73 (8.2 MB) 
            10008_.mkv                                                                  | bfccf6fe (71.4 MB)
            Notes & Settings                                                            | 45fd38ef (7.6 MB) 
    ```
3. Expire old reflogs
    ```sh
    $ git reflog expire --expire=now --all && git gc --prune=now --aggressive

    Enumerating objects: 57893, done.
    Counting objects: 100% (57893/57893), done.
    Delta compression using up to 10 threads
    Compressing objects: 100% (57478/57478), done.
    Writing objects: 100% (57893/57893), done.
    Selecting bitmap commits: 2853, done.
    Building bitmaps: 100% (133/133), done.
    Total 57893 (delta 34710), reused 13977 (delta 0), pack-reused 0
    ```
4. Push 
    ```sh
    git push
    ```

## Results

Git repo size before pruning:
```sh
$ du -sh .git
146M    .git
```

After pruning
```sh
$ du -sh .git
34M    .git
```
