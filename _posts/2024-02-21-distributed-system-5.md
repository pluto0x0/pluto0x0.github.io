---
title: Distributed System (5)
date: 2024-02-21 09:22:37
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Distributed Systems
image:
  path: 
---

## Chandy-Lamport Algorithm

(Snapshot should not interfere with normal application actions, and it should not require application to stop sending messages.)

First, initiator $P_i$:
- records its own state
- creates a special marker message.
- for $j=1\ldots n, j\ne i$
  - $P_i$ sends a marker message on outgoing channel $c_{ij}$
  - start recording $c_{ji}$

For other process $P_i$ receiving a marked message from channel $c_{ki}$,
- if it is the first time $P_i$ see marked message
  - $P_i$ records its own state
  - marks the state of $c_{ki}$ as "empty"
  - for $j=1\ldots n, j\ne i$
    - $P_i$ sends a marked message over $c_{ij}$
    - if $j\ne k$
      - start recording $c_{ji}$
- else
  - stop recording $c_{ki}$ (the state of channel contains all messages during recording)

<video controls src="../upload/img/2024-02-21-distributed-system-5-output.mp4" title="Title"></video>
