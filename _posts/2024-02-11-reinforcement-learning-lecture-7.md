---
title: Reinforcement Learning (7)
date: 2024-02-11 15:54:31
img_path: /_posts/
math: true
categories:
- Course Notes
- Reinforcement Learning
---

greedy policy:

$$
\pi^\star (s) = \arg\max_{a\in A} Q^\star (s, a)
$$

sequence of function:

$$
f_0, f_1, f_2, \cdots \to Q^\star 
$$

define

$$
\pi_{f_k}^\star (s) = \arg\max_{a\in A} f_k(s, a)
$$

Claim:

$$
\Vert V^\star  -V^{\pi_f} \Vert \le \frac{2 \Vert f - Q^\star  ||_\infty}{1-\gamma}
$$

define operator $\mathcal{T}$:

$$
(\mathcal{T}f)(s)=\max_{a \in A}\left(R(s, a)+\gamma E_{s^{\prime} \sim P(\cdot \mid s, A)}\left[f\left(s^{\prime}\right)\right]\right)
$$

> Note:
> the $\mathcal{T}$ in $\mathcal{T}Q^\star $ and $\mathcal{T}V^\star $ are **not the same**.
{: .prompt-tip }

## $V^\star $ Iteration

$$
\begin{gathered}
    f_0 = \vec{0} \\
    f_k \leftarrow \mathcal{T}f_{k-1}
\end{gathered}
$$

then

$$
f_k(s)=\max _{\text {all possible } \pi} \mathbb{E}\left[\sum_{t=1}^k \gamma^{t-1} r_t \mid s_1=s, \pi\right]
$$

> This is derived my the definaion of operator $\mathcal{T}$.
{: .prompt-tip }

Claim:

$$
\Vert f_k  -V^\star  \Vert \lesssim \gamma^k
$$

step 1: $f_k \le V^\star $

step 2: 

$$
\begin{aligned}
f_k \ge &\boxed{\mathbb{E}\left[\sum_{t=1}^\infty \gamma^{t-1} r_t \mid s_1=s, \pi^\star \right]} - \mathbb{E}\left[\sum_{t=k+1}^\infty \gamma^{t-1} r_t \mid s_1=s, \pi^\star \right] \\
\ge&\boxed{V^\star } - r^k V_{\max} \blacksquare
\end{aligned}
$$