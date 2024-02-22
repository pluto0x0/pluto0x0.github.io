---
title: Distributed System (4)
date: 2024-02-20 22:50:28
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Distributed Systems
image:
  path: ../upload/img/2024-02-20-distributed-system-4-image-2.png
---

## Event Ordering

Three types of events:

- Local computation
- Sending a message
- Receiving a message

### Happened-Before Relationship

- e $\rightarrow$ e' means e happened before e'.
- e $\rightarrow_i e'$ means e happened before $e'$, as observed by $P_{i}$

HB rules:

- If $\exists P_{i}, e \rightarrow_{i} e'$ then $e \rightarrow e'$.
- For any message $m$, send $(m) \rightarrow$ receive $(m)$
- If $e \rightarrow e'$ and $e' \rightarrow e''$ then $e \rightarrow e''$

> This is also called “causal” or “potentially causal” ordering.
{: .prompt-info }

if $a \nrightarrow e$ and $e \nrightarrow a$ then $a \| e$, i.e. **a and e are concurrent**.

### Lamport’s Logical Clock

![alt text](../upload/img/2024-02-20-distributed-system-4-image.png){: w="400" }

Algorithm: for each process $P_i$:

1. init local lock $L_i = 0$
2. $L_i += 1$ before timestamping each event
3. for each message $m$ to send, send $(m,L_i)$
4. upon receiving $(m,t)$
   - $L_i = \max(t, L_i)$
   - Do step (2)

if events $e \to e'$, then $L(e) < L(e’)$

### Vector Clocks

![alt text](../upload/img/2024-02-20-distributed-system-4-image-1.png){: w="400" }

$V_i[j]$ is the clock for process $P_j$ as maintained by $P_i$

Algorithm: for each process $P_i$:

1. initializes local clock $V_i[\cdot] = 0$
2. $V_i[i] += 1$ before timestamping each event.
3. for each message $m$ to send, send $(m, V_i)$
4. upon receiving $(m, v)$
   - $\forall j : V_i[j] = \max(V_i[j], v[j])$
   - Do step (2)

Comparing Vector Timestamps

- Let $V(e)=V$ and $V\left(e'\right)=V'$
- $V=V'$, iff $V[i]=V'[i]$, for all $i=1, \ldots, n$
- $V \leq V$ ', iff $V[i] \leq V'[i]$, for all $i=1, \ldots, n$
- $V<V'$, iff $V \leq V'$ and $V \neq V'$
- e $\rightarrow e'$ iff $V<V'$
- e $\| e'$ iff $\left(V \nless V'\right.$ and $\left.V' \nless V\right)$

## Global State (or Global Snapshot)

State of each process (and each channel) in the system at a
given instant of time.

### definitions

For a process $P_{i}$,
where events$\mathbf{e}_i^0, \mathbf{e}_i^1, \ldots$ occur:

- history$(P_i) = h_i = <e_i^0, e_i^1, \ldots>$
- prefix history$(P_i^k) = h_i^k = <e_i^0, e_i^1, \ldots, e_i^k>$
- $s_i^k$: $P_i$'s state immediately after k-th event.

For a set of process $<P_1, P_2, \ldots, P_n>$,

- global history: $H=\cup_i\left(h_i\right)$
- global state: $S=\cup_i\left(s_i\right)$
- a cut $C \subseteq H=h_1^{c_1} \cup h_2^{c_2} \cup \ldots \cup h_n^{c_n}$
- the frontier of $C=\{e_i^{c_i}, i=1,2, \ldots n\}$

### Consistent cut

A cut C is consistent iff

$$\forall e \in  C,  \text{if } f\to e \text{ then } f \in C$$

![alt text](../upload/img/2024-02-20-distributed-system-4-image-2.png){: w="600" }