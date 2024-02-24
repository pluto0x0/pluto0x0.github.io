---
title: Distributed System (11)
date: 2024-02-23 21:32:31
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Distributed Systems
---

## Consensus

- Each process proposes a value.
- All processes must agree on one of the proposed values.

### Required Properties

- **Termination**: Eventually each process sets its decision variable.
  - **Liveness**
- **Agreement**: The decision value of all correct processes is the same.
  - If Pi and Pj are correct and have entered the decided state, then di = dj.
  - **Safety**
- **Integrity**: If the correct processes all proposed the same value, then any correct process in the decided state has chosen that value.

### Round-based algorithm

Assume

- proposals are sent at time $s$.
- $\epsilon$: Worst-case skew
- $T$: Maximum message transfer time (including local processing)

Round-based algorithm

- For a system with at most $f$ processes crashing
  - All processes are synchronized and operate in “rounds” of time.
    - One round of time is equivalent to $\epsilon + T$ units.
- At each process, the i-th round
  - starts at local time $s + (i -1)*(\epsilon + T)$
  - ends at local time $s + i*(\epsilon + T)$
- The start or end time of a round in two different processes differs by at most $\epsilon$.
- The algorithm proceeds in $f+1$ rounds.
- Assume communication channels are reliable.

$\text{Values}_{i}^{r}$: the set of proposed values known to $P_i$ at the beginning of round $r$

- Initially $\text{Values}_{i}^{1} = \{v_i\}$:
  - for r = 1 to f+1 do
    - B-multicast $(\text{Values}_{i}^{r-1} - \text{Values}_{i}^{r})$
    - $\text{Values}_{i}^{r+1} = \text{Values}_{i}^{r}$
    - wait until one round of time expires
    - for each $v_j$ received in this round
      - $\text{Values}_{i}^{r+1} = \text{Values}_{i+1}^{r} \cup v_j$
- $d_i = \min(\text{Values}_{i}^{f+2})$

### Paxos Consensus Algorithm

Three types of roles:

- **Proposers**: propose values to acceptors.
  - All or subset of processes.
  - Having a single proposer (leader) may allow faster termination.
- **Acceptors**: accept proposed values (under certain conditions).
  - All or subset of processes.
- **Learners**: learns the value that has been accepted by majority of acceptors.
  - All processes. 

<!-- #### Try 1: Single Phase

- A proposer multicasts its proposed value to a large enough set (larger than majority) of acceptors.
- An acceptor accepts the first proposed value it receives.
- If majority of acceptors have accepted the same value v, then v is the decided value.  -->

#### Phase 1

- A proposer selects a proposal number (n) and sends a *prepare*
request with n to majority of acceptors, requesting:
  - Promise me you will not reply to any other proposal with a lower
number.
  - Promise me you will not accept any other proposal with a lower
number.
- If an acceptor receives a *prepare* request for proposal #n, and it
has not responded to a *prepare* request with a higher number, it
replies back saying:
  - *OK*! I will make that promise for any request I receive in the future.
  - (If applicable) I have already accepted a value v from a proposal with lower number m < n. The proposal has the highest number among the ones I accepted so far

#### Phase 2:

- If a proposer receives an *OK* response for its *prepare* request
#n from a majority of acceptors, then it sends an *accept* request
with a proposed value. What is the proposed value?
  - The value $v$ of the highest numbered proposal among the received
responses.
  - Any value if no previously accepted value in the received responses.
- If an acceptor receives an *accept* request for proposal #n, and it
has not responded a *prepare* request with a higher number, it
accepts the proposal
- What if the proposer does not hear from majority of acceptors?
  - Wait for some time, and then issue a new request with higher
number..