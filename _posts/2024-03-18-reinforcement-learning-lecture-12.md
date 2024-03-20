---
title: Reinforcemant Learning (12)
date: 2024-03-18 16:49:00
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Reinforcement Learning
---

### Every-visit Monte-Carlo

Suppose we Have a continuing task. What/if we cannot set the
starting state arbitrarily?

i.e. we have a single **long** trajectory with length $N$

$$
s_1, a_1, r_1,
s_2, a_2, r_2,
s_3, a_3, r_3,
\ldots
$$

- we can truncate $N/H$ truncations with length $H = O(1/(1-\gamma))$ from the long trajectory.
- we can shift the $H$-length window by 1 each time and get $N-H+1\approx N$ truncations.

This "walk" through the state space should have non-zero probability on each state, i.e. do not starve every states.

What if a state occures multiple times on a trajectory?

- approach 1: only the first occurance is used
- approach 2: all the occurances are used

## Alternative Approach: TD(0)

Again, suppose we have a single long trajectory $s_1, a_1, r_1, s_2, a_2, r_2$, $s_3, a_3, r_3, s_4, \ldots$ in a continuing task

TD(0): for $t=1,2, \ldots, V\left(s_t\right) \leftarrow V\left(s_t\right)+\alpha\left(r_t+\gamma V\left(s_{t+1}\right)-V\left(s_t\right)\right)$

TD
: temporal difference

TD_error
: $r_t+\gamma V\left(s_{t+1}\right)-V\left(s_t\right)$