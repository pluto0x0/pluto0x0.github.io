---
title: Distributed System (6-7)
date: 2024-02-05 14:06:55
img_path: /_posts/
math: true
categories:
- Course Notes
- Distributed Systems
image:
    path: ../upload/img/2024-02-05-distributed-system-6-image.png
---

## linearization

- **Liveness**: guarantee that something good will happen eventually
- **Safety**: guarantee that something bad will never happen.
- **Stable**: once true, stays true forever afterwards

## Multicast

### Basic Multicast (B-Multicast)

- B-multicast(group $g$, message $m$):
  - for each process $p$ in $g$, send $(p,m)$.
- receive($m$): B-deliver($m$) at $p$

### Reliable Multicast (R-Multicast)

- **Integrity**: A correct process $p$ delivers a message $m$ at most once.
- **Validity**: If a correct process multicasts (sends) message $m$, then it will eventually deliver $m$ to **itself**. (**Liveness**)
- **Agreement**: If a correct process delivers message $m$, then all the other correct processes in group($m$) will eventually deliver $m$.
- Validity and agreement together ensure overall liveness: if some
correct process multicasts a message m, then, **all correct processes**
deliver m too.

R-multicast is reliable even after **the sender crashes**.

### Implementing R-Multicast

On initialization:

- Received $:= \\{\\}$

For process $p$ to R-multicast message $m$ to group $g$

- B-multicast$(g,m)$, (notice $p\in g$)

On B-deliver$(m)$ at process $q$ in $g=$ group$(m)$

- if $m \notin$ Received
  - Received $:=$ Received $\cup \{ m \}$
  - if $p \ne q$:
    - B-multicast$(g, m)$
  - R-deliver$(m)$

## Ordered Multicast

### FIFO ordering

For a process, if it sends $m_1$ before $m_2$, then all processes recieves $m_1$ before $m_2$.

### Causal ordering

If multicasts $m_1 \to m_2$ ($m_1$ cause $m_2$, which means a process sends $m_2$ after recieving $m_1$), then all processes recieves $m_1$ **before** $m_2$.

Causal ordering implies FIFO ordering, because multicasts that sent by a process can be regarded as Causal

### Total ordering

For **any** pair of multicasts $m_1$, $m_2$, all processes recieving them recieves them **in the same order**.

Total Ordering doesn't imply Causal Ordering

## implementing ordered multicast

### Implement FIFO multicast

Each process has a sequence vector $P_i[1..N]$

On process $P_j$ sending multicast ($g$, $m$):

- $P_j[j] = P_j[j] + 1$
- B-multicast($g$, $\{m, P_j[j]\}$)

On process $P_i$ recieving multicast $\{m, S\}$ from $P_j$:

- buffer it until $S = P_i[j] + 1$, then
  - deliver$(m)$
  - $P_i[j] += 1$

### Implement causal order multicast

On process $P_i$ sending multicast ($g$, $m$):

- $P_j[j] = P_j[j] + 1$
- B-multicast($g$, $\{m, P_j[j]\}$)

On process $P_i$ recieving multicast $\{m, V[1 \ldots n]\}$ from $P_j$:

- buffer it until $V[j] = P_i[j] + 1$ and $\forall k\ne j: V[k] \le P_i[k]$
  - deliver$(m)$
  - $P_i[j] = V[j]$

## Implement total order multicast

A special process as **sequencer**.

On process $P_i$ sending multicast ($g$, $m$):

- B-multicast$(\{g, \text{sequencer}\}, m)$

Sequencer:

- init: $S = 0$
- On sequencer recieving multicast $\{m, S\}$ from $P_j$:
  - $S = S + 1$
  - B-multicast$(g, \{ \text{"order"}, m ,S \})$

Process $P_i$:

- init: $S_i = 0$
- On process $P_i$ recieving B-deliver$(m)$ from $P_j$:
  - buffer it until
<br>i. B-deliver$(g, \{ \text{"order"}, m ,S \})$ from sequencer, and
<br>ii. $S == S_i + 1$
<br>, then:
  - deliver$(m)$
  - $S_i = S_i + 1$

### ISIS algorithm for total ordering

Sender multicasts message to everyone.

Each message recieved by a process may have:

- agreed priority
- proposed priority
- a marker: undeliverable or not

Each processes $P_i$ have

- largest **agreed priority** $a_i$
- largest **proposed priority** $p_i$
- an priority queue of messages order by **agreed priority** or **proposed priority**

To send a total order multicast $m$ to all processes in $g$ by $P_i$:

- B-multicast$(g, \{ m, id\})$ where $id$ is an identifier for $m$.
- take the largest **proposed priority** collected from all other process as agreed priority $a$.
- $a_i = \max(a_i, a)$
- B-multicast$(g, \{ id, a\})$ **(here a can be `a:i`, i.e. attached with process id to avoid same priority)**
- set $a$ as the agreed priority of $m$
- mark $m$ as diliverable
- update the priority queue
- if the message $m'$ at the top of the queue is deliverable:
  - deliver$(m')$

Upon process $P_j$ recieving from $P_i$

- if received $\{ m, i\}$:
  - take $p_j := \max(p_j, a_j) + 1$ as the new proposed priority.
  - send$(P_i, p_j)$
- if received $\{ id, a\}$:
  - $a_i = \max(a_i, a)$
  - set $a$ as the agreed priority of $m$
  - mark $m$ as diliverable
  - update the priority queue
  - if the message $m'$ at the top of the queue is deliverable:
    - deliver$(m')$

<video controls src="/upload/img/2024-02-05-distributed-system-6-ISIS.mp4" title="ISIS algorithm for total ordering"></video>

> ISIS algorithm takes longer time than sequencer algorithm.
{: .prompt-info }

### Proof of ISIS algorithm

two messages: $m_1$, $m_2$, two procesess $p$, $q$.
Assume $p$ delivers $m_1$ first.

When $p$ delivers $m_1$, $m_2$ is either

- in queue and deliverable.
  - agreed_priority$(m_1)$ $<$ agreed_priority$(m_2)$
- in queue. not deliverable.
  - agreed_priority$(m_1)$ $<$ propose_priority$(m_2)$ $\le$ agreed_priority$(m_2)$
- not in queue.
  - agreed_priority$(m_2)$ $\ge$ propose_priority$(m_2)$ $>$ agreed_priority$(m_1)$

Therefore
agreed_priority$(m_1)$ $<$ agreed_priority$(m_2)$

And if $q$ delivers $m_2$ first, Contradiction.
