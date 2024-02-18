---
title: Distributed System (6)
date: 2024-02-05 14:06:55
img_path: /_posts/
math: true
categories: CourseNotes DistributedSystem
---

## linearization

liveness: guarantee that something good will happen, eventually


Safety = guarantee that something bad will never happen.

• Stable = once true, stays true forever afterwards

## Ordered Multicast

### FIFO ordering

For a peocess, if it sends $m_1$ before $m_2$, then all processes recieves $m_1$ before $m_2$.

### Causal ordering

If multicasts $m_1 \to m_2$ ($m_1$ cause $m_2$, which means a process sends $m_2$ after recieving $m_1$), then all processes recieves $m_1$ **before** $m_2$.

Causal ordering implies FIFO ordering, because multicasts that sent by a process can be regarded as Causal

### Total ordering

For **any** pair of multicasts $m_1$, $m_2$, all processes recieving them recieves them **in the same order**.

Total Ordering doesn't imply Causal Ordering


## Ordered Multicast

### FIFO ordering

Each process has a sequence vector $P_i[1..N]$

On process $P_i$ sending multicast ($g$, $m$):

- $P_j[j] \leftarrow P_j[j] + 1$
- B-multicast($g$, $\{m, P_j[j]\}$)

On process $P_i$ recieving multicast $\{m, S\}$ from $P_j$:

- repeat until $S = P_i[j] + 1$
- $P_i[j] \leftarrow P_i[j] + 1$

## Causal Ordering

## Total ordering

categories: CourseNotes DistributedSystem
---

21 Feb

ISIS algorithm for tatal ordering

