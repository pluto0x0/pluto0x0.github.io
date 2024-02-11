---
title: Reinforcement Learning (6)
date: 2024-02-11 07:51:18
img_path: /_posts/
math: true
---

Recall $V^*, Q^*, V^\pi, Q^\pi$.

$$
V^*(s)=\max _{a \in A}(\underbrace{R(s, a)+\gamma \mathbb{E}_{S^{\prime} \sim P(\cdot \mid s, a)}\left[V^*\left(s^{\prime}\right)\right]}_{Q^*(s, a)})
$$

## Bellman Operator

$$
\begin{gathered}
\forall f: S\times A \to \mathbb{R}, \\
(\mathcal{T}f) (s,a) = (R(s,a) + \gamma \mathbb{E}_{s'\sim P(\cdot|s,a)}[\max_{a'} f(s', a')]) \\
\text{where} \; \mathcal{T}: \mathbb{R}^{SA} \to \mathbb{R}^{SA}.
\end{gathered}
$$

then

$$
\begin{gathered}
Q^* = \mathcal{T} Q^* \\
V^* = \mathcal{T} V^* \\
\end{gathered}
$$

i.e. $Q^*$ and $V^*$ are fixpoints of $\mathcal{T}$.

## Value Interation Algorithm (VI)

$$
\text{funtion } f_0 = \vec{0} \in \mathbb{R}^{SA} 
$$

Interation to calculate fix points:

for $k = 1,2,3, \cdots$,

$$
f_k = \mathcal{T} f_{k-1}
$$

How to do interation

$$
\forall s,a: \; f_1(s,a) \leftarrow \mathcal{T} f_0(s,a)
$$

- synchronized iteration: use all functions values from old version during the update.
- asynchronized iteration

## Convergence of VI

lemma: $\mathcal{T}$ is a $\gamma$**-contraction** under $\|\cdot\|_{\infty}$ where $\|\cdot\|_{\infty} := \max_{x\in (\cdot)}x$

which means 

$$
\|Tf-f\|_{\infty}\leq\gamma\|f-f\|_{\infty}
$$


