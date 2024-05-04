---
id: ky430yx6hvrsaycj41847r2
title: Memory DB
desc: ''
updated: 1714318713170
created: 1714270939829
topic: aws
---

[Amazon MemoryDB: A fast and durable memory-first cloud database](https://www.amazon.science/publications/amazon-memorydb-a-fast-and-durable-memory-first-cloud-database)

great paper from AWS about the system architecture of memorydb (a highly available redis compatible in-memory database)

many nuggets here - what I particularly liked is the choice of using  a distributed transaction log as a means of achieving consensus (having a set of distributed nodes agree on a common truth)

for leader election, all nodes will attempt to conditionally write themselves into the transaction log - the node that "wins" becomes the leader and the rest have the write fail. the leader then writes heartbeats into the log to maintain leadership. the system will know that the leader is not available when the heartbeats fail and a new leader "election" will begin again.

this turns the complicated process of consensus that is usually achieved via more complicated means like paxos into a conditional write operation. 

when building software, having solid data structures greatly simplifies, and sometimes simply makes possible, great applications.
when building distributed systems, having the right highly available database and storage service, does the same thing
