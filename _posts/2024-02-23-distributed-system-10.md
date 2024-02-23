---
title: Distributed System (10)
date: 2024-02-23 07:02:03
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Distributed Systems
# image:
#   path: ../upload/img/2024-02-22-distributed-system-8-image-6.png
---

## Leader Election

- Any process can call for an election.
- A process can call for at most one election at a time.
- Multiple processes are allowed to call an election simultaneously.
  - All of them together must yield only a single leader
- The result of an election should not depend on which process
calls for it.

### Election Problem

A run of the election algorithm must always guarantee:

- **Safety**: For all non-faulty processes p:
  - p has elected:
    1) (q: a particular non-faulty process with the best attribute value)
    2) or Null
- **Liveness**: For all election runs:
  - election run terminates
  - for all non-faulty processes p: p’s elected is not Null

At the end of the election protocol, the non-faulty process with the
best (highest) election attribute value is elected.
