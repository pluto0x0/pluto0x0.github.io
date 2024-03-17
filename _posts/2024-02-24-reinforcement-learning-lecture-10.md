---
title: Reinforcemant Learning (10)
date: 2024-02-24 03:06:58
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Reinforcement Learning
---

# The Learning Setting

## planning and learning

Planning:

- given MDP model, how to compute optimal policy
- The MDP model is known

Learning:

- MDP model is unknown
- collect data from the MDP: $(s,a,r,s')$.
- Data is limited. e.g., adaptive medical treatment, dialog systems
- Go, chess, ...
- Learning can be useful **even if the final goal is planning**
  - especially when $\vert S \vert$ is large and/or only blackbox simulator
  - e.g., AlphaGo, video game playing, simulated robotics

## Monte-Carlo policy evaluation

Given $\pi$, estimate $J(\pi):=\mathbb{E}_{s \sim d_0}\left[V^\pi(s)\right]$ ( $d_0$ is initial state distribution)
is the *actual* expectation of reward.

Monte-Carlo outputs some scalar $v$; accuracy measured by $\vert v-J(\pi)\vert$.
(by sampling different trajectories):

Data: trajectories starting from $s_1 \sim d_0$ using $\pi$ (i.e., $a_t=\pi\left(s_t\right)$ ).

$$
\left\{\left(s_1^{(i)}, a_1^{(i)}, r_1^{(i)}, s_2^{(i)}, \ldots, s_H^{(i)}, a_H^{(i)}, r_H^{(i)}\right)\right\}_{i=1}^n
$$

> this is called on-policy: evaluating a policy with data collected from the exactly same policy.
>
> Othwise, it is off-policy.
{: .prompt-info }

Estimator:

$$
\frac{1}{n} \sum_{i=1}^n \sum_{t=1}^H \gamma^{t-1} r_t^{(i)}
$$

> Guarantee: w.p. at least $1-\delta,\vert v-J(\pi)\vert  \leq \frac{R_{\max }}{1-\gamma} \sqrt{\frac{1}{2 n} \ln \frac{2}{\delta}}$ (larger n, higher accuracy)
>
> It is **independent** to the size of state space
{: .prompt-tip }

### Comment on Monte-Carlo

Monte-Carlo is a Zeroth-order (ZO) optimization method, which is not efficient.

- **first order**: gradient / first derivative (in DL/ML, **SDG**)
- **second order**: Hessian matrix / second derivative

## Model-based RL with a sampling oracle (Certainty Equivalence)

> Assuming the reward / probability is determined (constant) via sampling.
{: .prompt-info }

Assume we can sample $r \sim R(s, a)$ and $s^{\prime} \sim P(s, a)$ for any $(s, a)$

Collect $n$ samples per $(s, a):\\{\left(r_i, s_i^{\prime}\right)\\}_{i=1}^n$. Total sample size $n\vert S \times A\vert$

Estimate an empirical MDP $\hat{M}$ from data

- $\hat{R}(s, a):=\frac{1}{n} \sum_{i=1}^n r_i, \quad \hat{P}\left(s^{\prime} \mid s, a\right):=\frac{1}{n} \sum_{i=1}^n \mathbb{I}\left[s_i^{\prime}=s^{\prime}\right]$
- i.e., treat the empirical frequencies of states appearing in $\{s_i^{\prime}\}_{i=1}^n$ as the true distribution.

Plan in the estimated model and return the optimal policy

transition tuples: $(s_i, a_i, r_i, s_{i+1})$. Use $s_i, a_i$ to identify current state and action, use $r_i$ for reward and $s_{i+1}$ for transition.

extract transition tuples from trajectories.

### finding policy on estimated environment

**true** environment: $M = (S, A, P, R, \gamma)$

**estimated** environment: $\hat{M} = (S, A, \hat{P}, \hat{R}, \gamma)$

- notation: $\pi_{\hat{M}}, \, V_{\hat{M}}, \, \ldots$

performance measurement:

- in the **true** environment, use $\Vert V^\star - V^{\pi_f} \Vert$ where $f \approx Q^\star$
- in **estimated** environment, use $\Vert V_M^\star - V_M^{\pi_{\hat{M}}^\star} \Vert$, i.e. measure the optimal policy of estimated environment in the real environment.
