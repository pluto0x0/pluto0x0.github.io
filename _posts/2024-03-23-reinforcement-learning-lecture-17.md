---
title: Reinforcemant Learning (17)
date: 2024-03-23 01:38:00
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Reinforcement Learning
---

## A Question

$a_1 a_2 a_3 a_4 a_5$

We do $V_\theta(s)\leftarrow V_\theta(s) + \alpha(r-\gamma V_\theta\left(s^{\prime}\right) - V_\theta(s))$ in TD(0).

What if we minimize the square error between $V_\theta(s)$ and its target, i.e. $\mathbb{E}_{s,r,s^{\prime}}\left[\left(V_\theta(s)-r-\gamma V_\theta\left(s^{\prime}\right)\right)^2\right]$ ?

No correct. It can be [decomposed](./reinforcement-learning-homework-0/#proof) as the sum of 2 parts:

- $\mathbb{E}_s\left[\left(V_\theta(s)-\left(\mathscr{T}^\pi V_\theta\right)(s)\right)^2\right]$
  - good. It's L-2 norm Bellman Error.
- $\gamma^2 \mathbb{E}_s\left[\operatorname{Var}_{s^{\prime} \mid s, \pi(s)} \left[ V_\theta\left(s^{\prime}\right)\right]\right]$
  - Not good. It penalize policy with large variance.
  - OK for deterministic environment because the variance is always $0$ in this case.

### Solution

If we have a simulator, for each $s$ in data, draw another independent state transition.

Minimize objective

$$
\mathbb{E}\left[\left(V_\theta(s)-r-\gamma V_\theta\left(s_A^{\prime}\right)\right)\left(V_\theta(s)-r-\gamma V_\theta\left(s_B^{\prime}\right)\right]\right.
$$

<!-- i.e. uses 2 distinct variables $s_B'$, $s_C'$. -->

"Double sampling" and Baird's residual algorithm (Bellman residual minimization).

## Convergence

- TD with function approximation can diverge in general
- Is it because of...
  - Randomness in SGD?
    - Nope. Even the batch version doesn't converge
  - Sophisticated, non-linear func approx?
    - Nope. Even linear doesn't converge.
  - That our function class does not capture V"?
    - Nope. Even if V" can be exactly represented in the function class ("realizable"), it still does not converge.

### example

```mermaid
graph LR
    1((1)) 
    --> 2((2))
    --> 3((3))
    --> 4((4)) 
    --> 5((5))
    --> 6((6))
    --> 7((7))
    --> 8((8))
    --> 9((9))
    --> 10((10))
    10 ~~~|"reward=Ber(0.5)"| 10
```

iterations

\#Iter | 1     | 2     | ...    | 9     | 10
-------|-------|-------|--------|-------|-------
1      |       |       |        |       | 0.501
2      |       |       |        | 0.501 | 0.501
...    |       |       |        |       |
10     | 0.501 | 0.501 |  0.501 | 0.501 | 0.501

Assume the function space has to possible values at each state:

<!-- 1     |2     |3      | ... | 8     | 9     | 10
------|------|-------|-----|-------|-------|------ -->
0.5   |0.5   | 0.5   | ... | 0.5   | 0.5   | 0.5
1.012 |0.756 |0.628  | ... | 0.504 | 0.502 | 0.501

(
0.5 and **0.502** have the same distance to **0.501**;
0.5 and **0.504** have the same distance to **0.502**;
...
)

then

\#Ite  | 1     | 2     | ...    | 9     | 10
-------|-------|-------|--------|-------|-------
1      |       |       |        |       | 0.501
2      |       |       |        | 0.502 | 0.501
...    |       |       |        |       |
10     | 1.012 | 0.756 | ...    | 0.502 | 0.501

Value deviates from 0.501 as iteration goes.

Say the function space is a **plane**, than the results of each iteration (bellman operator) is not on the plane, instead, their **projections** are picked.

We can only sample $x \sim q$ but want to estimate $\mathbb{E}_{x\sim p} f(x)$

Is (or importance weighted, or inverse propensity yscore Ps
estimator): 

$$
\frac{p(x)}{q(x)}f(x)
$$

Unbiasedness:

$$
\mathbb{E}_{x \sim q}\left[\frac{p(x)}{q(x)} f(x)\right]=\sum_x q(x)\left(\frac{p(x)}{q(x)} f(x)\right)=\sum_x p(x) f(x)=\mathbb{E}_{x \sim p}[f(x)]
$$

<!-- ### Application in contextual bandit (CB)

- CB: episodic MDP with $H=1$. Actions have no long-term effects. Just optimize the immediate reward.
  - $x \sim d_0$ : context distribution (corresponds to initial state distribution of the MDP)
  - agent takes an action $a$ based on $x$
  - agent observes reward $r \sim R(x, a)$

- The data point is a tuple $(x, a, r)$
- The function of interest is $(x, a, r) \mapsto r \quad \pi$ : target policy
- The distribution of interest is $x \sim d_0, a \sim \frac{\pi}{\Delta} r \sim R(x, a)$
- Let the joint density b $p(x, a, r) \nabla_{\pi_b \text { : behavior/logging policy }}$
- The data distribution is $x \sim d_0, a \sim \pi_k, r \sim R(x, a)$
- Let the joint density be $q(x, a, r)$ f
- IS estimator: $\frac{p(x, a, r)}{q(x, a, r)} \cdot r$ -->