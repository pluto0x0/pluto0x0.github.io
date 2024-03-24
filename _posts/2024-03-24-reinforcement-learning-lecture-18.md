---
title: Reinforcemant Learning (17)
date: 2024-03-24 03:07:00
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Reinforcement Learning
---

## Application in contextual bandit (CB)

- The data point is a tuple $(x, a, r)$
- The function of interest is $(x, a, r) \mapsto r$
- The distribution of interest is $x \sim d_0, a \sim \pi, r \sim R(x, a)$
  - Let the joint density be $p(x, a, r)$
- The data distribution is $x \sim d_0, a \sim \pi_b, r \sim R(x, a)$
  - Let the joint density be $q(x, a, r)$
- IS estimator: $\frac{p(x, a, r)}{q(x, a, r)} \cdot r$
- Write down the densities
  - $p(x, a, r)=d_0(x) \cdot \pi(a \mid x) \cdot R(r \mid x, a)$
  - $q(x, a, r)=d_0(x) \cdot \pi_b(a \mid x) \cdot R(r \mid x, a)$
  - To compute importance weight, you don't need knowledge of $\mu$ or $R$ ! You just need $\pi_b$ (or even just $\pi_b(a \mid x)$, "proposal prob.")

- Let $\rho$ be a shorthand for $\pi(a \mid x)$, so estimator is $\rho \cdot r$
- $\pi_b$ need to "cover" $\pi$
  - i.e., whenever $\pi(a \mid x)>0  , we need $\pi_b(a \mid x)>0$
- A special case:
  - $\pi$ is deterministic, and $\pi_b$ is uniformly random $\left(\pi_b(a \mid x) \equiv 1 /|A|\right)$
  - $\frac{\mathbb{I}[a = \pi(x)]}{1/|A|} r$
    - only look at actions that match what $\pi$ wants to take and discard other data points
    - If match, $\rho=|A|$; mismatch: $\rho=0$
  - On average: only $1 /|A|$ portion of the data is useful

### A note about using IS

- We know that shifting rewards do not matter (for planning purposes) for fixed-horizon problems
- However, when you apply IS, shifting rewards do impact the variance of the estimator
- Special case:
  - deterministic $\pi$, uniformly random $\pi_b$,
  - reward is deterministic and constant: regardless of $(x, a)$, reward is always 1 (without any randomness)
  - We know the value of any policy is 1
  - On-policy MC has 0 variance
  - IS still has high variance!
- Where does variance come from?

$$
\begin{aligned}
& \frac{1}{n} \sum_{i=1}^n \frac{\mathbb{I}\left[a^{(i)}=\pi\left(x^{(i)}\right)\right]}{1 /|A|} \cdot r^{(i)}=\sum_{i=1}^n \frac{\mathbb{I}\left[a^{(i)}=\pi\left(x^{(i)}\right)\right] \cdot r^{(i)}}{n /|A|} \\
& =\frac{1}{n /|A|} \sum_{i: a^{(i)}=\pi\left(x^{(i)}\right)} r^{(i)}
\end{aligned}
$$

Because $n / \vert A\vert$ is the **expectaton** of # of sampling $a^{(i)}$ matches $\pi$ but not the true # of matched samples, which causes variance.

Solution: use true # of matched samples as denometer,

$$
\frac{1}{| \{ i:a^{(i)} = \pi^{(i)} \} |} \sum_{a^{(i)} = \pi^{(i)}}r_i
$$

## Multi-step IS in MDPs

- Data: trajectories starting from $s_1 \sim d_0$ using $\pi_b$ (i.e., $a_t \sim \pi_b\left(s_t\right)$ )
(for simplicity, assume process terminates in $H$ time steps)

$$
\left\{\left(s_1^{(i)}, a_1^{(i)}, r_1^{(i)}, s_2^{(i)}, \ldots, s_H^{(i)}, a_H^{(i)}, r_H^{(i)}\right)\right\}_{i=1}^n
$$

- Want to estimate $J(\pi):=\mathbb{E}_{s \sim d_0}\left[V^\pi(s)\right]$
- Same idea as in bandit: apply IS to the entire trajectory

===

- define $\tau$ as the whole trajectory. The function of interest is $\tau \mapsto \sum_{t=1}^H \gamma_{\partial}^{t-1} r_t$.
- Let the distribution of trajectory induced by $\pi$ be $p(\tau)$
- Let the distribution of trajectory induced by $\pi_b$ be $q(\tau)$
- IS estimator: $\frac{p(\tau)}{q(\tau)} \cdot \sum_{t=1}^H \gamma^{t-1} r_t$

How to compute $p(\tau)/q(\tau)$?

- $p(\tau)=d_0\left(s_1\right) \cdot \pi\left(a_1 \mid s_1\right) \cdot P\left(s_2 \mid s_1, a_1\right) \cdot \pi\left(a_2 \mid s_2\right) \cdots P\left(s_H \mid s_{H-1}, a_{H-1}\right) \cdot \pi\left(a_H \mid s_H\right)$
- $q(\tau)=d_0\left(s_1\right) \cdot \pi_b\left(a_1 \mid s_1\right) \cdot P\left(s_2 \mid s_1, a_1\right) \cdot \pi_b\left(a_2 \mid s_2\right) \cdots P\left(s_H \mid s_{H-1}, a_{H-1}\right) \cdot \pi_b\left(a_H \mid s_H\right)$

Here all $P(\cdot\vert\cdot)$ terms are cancelled out.

Let $\rho_t=\frac{\pi\left(d_t \mid s_t\right)}{\pi_b\left(a_t \mid s_t\right)}$, then $\frac{p(\tau)}{q(\tau)}=\prod_{t=1}^H \rho_t=: \rho_{1: H}$

### Examine the special case again

- $\pi$ is deterministic, and $\pi_b$ is uniformly random $\left(\pi_b(a \mid x) \equiv 1 /|A|\right)$
- $\rho_t=\frac{\mathbb{I}\left[a_t=\pi\left(s_t\right)\right]}{1 /|A|}$
- only look at trajectories where all actions happen to match what $\pi$ wants to take
  - Only if match, $\rho=|A|^H$; mismatch: $\rho=0$
- On average: only $1 /\vert A\vert^H$ portion of the data is useful
