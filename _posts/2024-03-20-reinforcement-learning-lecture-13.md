---
title: Reinforcemant Learning (13)
date: 2024-03-20 14:43:00
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Reinforcement Learning
---

## TD($\lambda$): Unifying TD(0) and MC

- 1-step bootstrap (TD(0)): $r_1 + \gamma V(s_{i+1})$
- 2-step bootstrap: $r_1 + \gamma r_{i+1} + \gamma^2 V(s_{i+2})$
- 3-step bootstrap: $r_1 + \gamma r_{i+1} + \gamma^2 r_{i+2} + \gamma^3 V(s_{i+3})$
- ...
- $\infty$-step bootstrap: $r_1 + \gamma r_{i+1} + \gamma^2 r_{i+2} + \gamma^3 r_{i+3} + \cdots$ is Monte-Carlo.

### Proof of TD($\lambda$)'s correctness

E.g. in 2-step bootstrap,

<!--  proving

$$
\mathbb{E}(G_t) := 
\mathbb{E}[r_1 + \gamma r_{t+1} + \gamma^2 V(s_t+2)|s_t]
=
\mathbb{E}[(\mathcal T^\pi)(s_t)|s_t]
$$

suffies. -->

With [Law of total expectation](https://en.wikipedia.org/wiki/Law_of_total_expectation),

$$
\begin{aligned}
 & \mathbb{E}[r_1 + \gamma r_{t+1} + \gamma^2 V(s_{t+2})|s_t] \\
=& \mathbb{E}[r_t + \gamma(r_{t+1}+\gamma V(s_{t r})) | s_t] \\
=& \mathbb{E}[r_t] + \gamma \mathbb{E}_{s_{t+1}|s_t}\big[\mathbb{E}[(r_{t+1}+\gamma V(s_{t r})) | s_t, s_{t+1}]\big] \\
=& \mathbb{E}[r_t + \gamma (\mathcal{T}^\pi)(s_{t+1}) | s_t ] \\
=& ((\mathcal{T}^\pi)^2 V)(s)
\end{aligned}
$$

### TD($\lambda$)

For n-step bootstrap, give a $(1-\lambda)\lambda^n$ weight.

- $\lambda = 0$: Only n=1 gives the full weight. TD(0).
- $\lambda \to 1$: (almost) Monte-Carlo.

#### forward view and backward view

Forward view

$$
\begin{gathered}
(1-\lambda)\cdot (r_1+\gamma V(s_2)-V(s_1)) \\
(1-\lambda) \lambda \cdot(r_1+\gamma r_2+\gamma^2 V(s_3)-V(s_1)) \\
(1-\lambda) \lambda^2 \cdot(r_1+\gamma r_2+\gamma^2 r_3+\gamma^3 V(s_4)-V(s_1)) \\
\cdots
\end{gathered}
$$

, and so on.

Backward view

$$
\begin{gathered}
1                  \cdot (r_1 + \gamma V(s_2) - V(s_1)) \\
\lambda \gamma     \cdot (r_2 + \gamma V(s_3) - V(s_2)) \\
\lambda^2 \gamma^2 \cdot (r_3 + \gamma V(s_4) - V(s_3)) \\
\cdots
\end{gathered}
$$
