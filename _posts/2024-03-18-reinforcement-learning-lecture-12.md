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

Same as Monte-Carlo update rule, excepts that the "target" is $r_t+\gamma V\left(s_{t+1}\right)$, which is similar to the [empirical Bellman update](reinforcement-learning-lecture-11/#model-based-rl-with-a-sampling-oracle-certainty-equivalence-contd). <!-- (the differece is) -->

Recall that in [Monte-Carlo](reinforcement-learning-lecture-11/#monte-carlo-value-prediction), the "target" is $G_t=\sum_{t^{\prime}=t}^{t+H} \gamma^{t^{\prime}-t} r_{t^{\prime}}$ and is **independent** to the current value function.
While in TD(0), the target $r_t+\gamma V\left(s_{t+1}\right)$ is dependent to the current value function $V$. i.e.

Compared to value iteration:

$$
    V_{k+1}(s) := \mathbb{E}_{r,s'|s,\pi} \left[r+\gamma V_k\left(s^{\prime}\right)\right]
$$

and the equation above is

$$
    \approx \frac{1}{n} \sum_{i=1}^n\left(r_i+r V_k\left(s_i^{\prime}\right)\right)
$$

which is an approximate Value Iteration process, and notice that the whole iteraton through $i=1,\cdots, n$ is only 1 iteration (a $V_k$), so an outside loop is needed if we want to $V$ approximates real $V^\pi$.

### Understanding TD(0)

The "approximate" Value Iteration process above is similar to TD(0) but slightly different:
it uses a value function $V$ (which stays constant during updates) to update $V'$ which is another function. After long enough, we have $V'=\mathcal{T}^\pi V$ and do $V \leftarrow V'$, then repeat the process. Finally converges to $V^\pi$.

But in TD(0), we uses $V$ to update itself. The difference is "synchronous" vs "asynchronous".

> TD(0) is less stable
{: .prompt-info }
