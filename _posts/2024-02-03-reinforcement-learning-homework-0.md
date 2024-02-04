---
title: Reinforcement Learning Homewor (0)
date: 2024-02-03 00:41:03
img_path: /_posts/
math: true
---

## 1

Among all probability distributions over $[a, b] \in \mathbb{R}$, which distribution has the highest variance? How large is
that variance?

### Proof

$$
P(x) = \begin{cases}
    \frac{1}{2} & x = a, b \\
    0 & \text{otherwise}
\end{cases}
$$

then 

$$
\operatorname{Var}(x) = \mathbb{E}\left(\left(x-\frac{a+b}{2}\right)^2\right) = \left(\frac{a+b}{2}\right)^2
$$

## 2

Let $X, Y$ be two random variables that follow some joint distributions over $\mathcal{X} \times \mathbb{R}$. Let $f: \mathcal{X} \rightarrow \mathbb{R}$ be a real-valued function. Prove that

$$
\mathbb{E}\left[(Y-f(X))^2\right]-\mathbb{E}\left[(f(X)-\mathbb{E}[Y \mid X])^2\right]=\mathbb{E}\left[(Y-\mathbb{E}[Y \mid X])^2\right] .
$$

### Proof

It suffies to prove

$$
\begin{gathered}
\mathbb{E}\left[(Y-f(X))^2 - (f(X)-\mathbb{E}[Y \mid X])^2 - (Y-\mathbb{E}[Y \mid X])^2\right] = 0 \\

\text{i.e.}\quad \mathbb{E}\left[\left(E\left[Y|X\right]-Y\right)\left(E\left[Y|X\right]-f\left(X\right)\right)\right]=0 .
\end{gathered}
$$

Given $E[Y|X]$ is a function of $X$, let $g(X) := E[Y|X] - f(X)$ then it suffies to prove

$$
\mathbb{E}[\mathbb{E}[Y|X]g(X)] = \mathbb{E}[Y g(X)] .
$$

then

$$
\begin{aligned}
    \text{LHS} &= \sum_{x_i} \boxed{\mathbb{E}[Y|X=x_i]} g(x_i) P_X(x_i) \\
    &= \sum_{x_i} g(x_i) P_X(x_i) \boxed{\sum_{y_i}y_i\frac{P_{X,Y}(x_i,y_i)}{P_X(x_i)} } \\ 
    &= \sum_{x_i} \sum_{y_i} g(x_i) y_i P_{X,Y}(x_i,y_i) \\
    &= \text{RHS} \blacksquare
\end{aligned}
$$

### Notes

Let $f: \mathcal{X} \rightarrow \mathbb{R}$ be a estimator from $X$ to $Y$, this equation shows that square error ($l_2$ loss) $\mathbb{E}\left[(Y-f(X))^2\right]$ is at least $\mathbb{E}\left[(Y-\mathbb{E}[Y \mid X])^2\right]$ for $\forall f$ and thus cannot be arbitrarily small.

## 3


Let $A \in \mathbb{R}^{n \times n}$ be a positive-definite real symmetric matrix, and $b \in \mathbb{R}^n$ be a vector. $\lambda$ is the largest eigenvalue of $A$, that is,

$$ \lambda = \max_{z:||z||_2=1} ||Az||_2. \quad (1) $$

Let $x^*$ be the solution to $x^* = Ax^* + b$. Define $x_0 = 0$ and for $t > 0$, $x_t := Ax_{t-1} + b$. Prove that $||x_t - x^*||_2 \leq \lambda^t ||x^*||_2$.

(Hint: show that $||x_t - x^*||_2 \leq \lambda ||x_{t-1} - x^*||_2$). Also, you do not need to know any additional properties about the largest eigenvalue of matrix; the proof is elementary given Eq. (1).)
