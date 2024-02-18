---
title: Reinforcement Learning Homework (0)
date: 2024-02-03 00:41:03
img_path: /_posts/
math: true
categories:
- Course Notes
- Reinforcement Learning
---

## 1

Among all probability distributions over $[a, b] \in \mathbb{R}$, which distribution has the highest variance? How large is
that variance?

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

\text{i.e.}\quad \mathbb{E}\left[\left(E\left[Y|X\right]-Y\right)\left(E\left[Y\vert X\right]-f\left(X\right)\right)\right]=0 .
\end{gathered}
$$

Given $E[Y\vert X]$ is a function of $X$, let $g(X) := E[Y\vert X] - f(X)$ then it suffies to prove

$$
\mathbb{E}[\mathbb{E}[Y|X]g(X)] = \mathbb{E}[Y g(X)] .
$$

then

$$
\begin{aligned}
    \text{LHS} &= \sum_{x_i} \boxed{\mathbb{E}[Y|X=x_i]} g(x_i) P_X(x_i) \\
    &= \sum_{x_i} g(x_i) P_X(x_i) \boxed{\sum_{y_i}y_i\frac{P_{X,Y}(x_i,y_i)}{P_X(x_i)} } \\
    &= \sum_{x_i} \sum_{y_i} g(x_i) y_i P_{X,Y}(x_i,y_i) \\
    &= \text{RHS} \;\blacksquare
\end{aligned}
$$

### Notes

Let $f: \mathcal{X} \rightarrow \mathbb{R}$ be a estimator from $X$ to $Y$, this equation shows that square error ($l_2$ loss) $\mathbb{E}\left[(Y-f(X))^2\right]$ is at least $\mathbb{E}\left[(Y-\mathbb{E}[Y \mid X])^2\right]$ for $\forall f$ and thus cannot be arbitrarily small.

## 3

Let $A \in \mathbb{R}^{n \times n}$ be a positive-definite real symmetric matrix, and $b \in \mathbb{R}^n$ be a vector. $\lambda$ is the largest eigenvalue of $A$, that is,

$$ \lambda = \max_{z:\Vert z\Vert _2=1} \Vert Az\Vert _2. \quad (1) $$

Let $x^\star$ be the solution to $x^\star = Ax^\star + b$. Define $x_0 = 0$ and for $t > 0$, $x_t := Ax_{t-1} + b$. Prove that $\Vert x_t - x^\star\Vert_2 \leq \lambda^t \Vert x^\star\Vert_2$.

(Hint: show that $\Vert x_t - x^\star\Vert_2 \leq \lambda \Vert x_{t-1} - x^\star\Vert_2$ ). Also, you do not need to know any additional properties about the largest eigenvalue of matrix; the proof is elementary given Eq. (1).)

### Proof

substitude

$$
b = x^\star - Ax^\star,
$$

then

$$
x_t = Ax_{t-1} + b = Ax_{t-1} + x^\star - Ax^\star,
$$

and it suffies to prove

$$
\begin{gathered}
    \Vert x_t - x^\star \Vert _2 \leq \lambda \Vert x_{t-1} - x^\star \Vert _2 \\
    \text{i.e.}\quad \Vert Ax_{t-1} - Ax^\star\Vert _2 \le  \lambda \Vert x_{t-1} - x^\star \Vert _2 \\
\end{gathered}
$$

With Equation (1),

$$
 \Vert A(x_{t-1} - x^\star)\Vert _2 \le  \lambda \Vert x_{t-1} - x^\star \Vert _2  \;\blacksquare
$$

## 4

Prove that $\gamma^{\frac{\log(1/\epsilon)}{1-\gamma}} \le \epsilon$ when $\gamma, \epsilon \in (0, 1)$.

(Hint: use the fact that $(1-1/x)^x< 1/e$ when $x > 1$)

### Proof

#### Lemma

$$
(1-1/x)^x< 1/e \quad\text{when}\quad x > 1
$$

It suffies to prove

$$
x\log\left(1-\frac{1}{x}\right) < -1.
$$

Substitude $u := 1-1/x$, then

$$
\log(u) < u-1
$$

holds.

For original proposition, substitude $u := \frac{1}{1-\gamma}$ and therefore $\gamma = 1 - \frac{1}{u}$,
then It suffies to prove

$$
\left( 1 - \frac{1}{u} \right)^{u \log(1/\epsilon)} \le \epsilon
$$

with the lemma,

$$
\left( 1 - \frac{1}{u} \right)^{u \log(1/\epsilon)} < \left( \frac{1}{e} \right)^{\log (1/\epsilon)} = \epsilon \;\blacksquare
$$

