---
title: Reinforcemant Learning (14)
date: 2024-03-20 18:20:00
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Reinforcement Learning
---

## Value Prediction with Function Approximation

tabular representation vs. function approximation
: function approximation can handle infinite state space (can't enumerate through all states).

linear function approximation
: design features $\phi(s) \in \mathbb{R}^d$ ("featurizing states"), and approximate $\mathrm{V}^\pi(\mathrm{s}) \approx \theta^{\top} \phi(\mathrm{s}) + b$, where $\theta$ should be fixed among features (in the following parts, $b$ is **ignored** because it can be reached by appending a $1$ to the feature vector).
> tabular value function can be interpreted as feature vector $\in \mathbb{R}^S$:
> $[0,\cdots, 0, 1, 0, \cdots, 0]$ where the position of the $1$ indicates the state.
{: .prompt-info }

### Example: Tetris Game

![alt text](../upload/img/2024-03-20-reinforcement-learning-lecture-14-image-1.png)
_Tetris Game_

The state space is exponentially large: each block be occupied / not occupied.

Featurize: # of blocks on each column. In the example, the feature is $
(4\;4\;5\;4\;3\;3\;3\;\cdots)$

### Monte-Carlo Vaule Prediction

$$
V^\pi(s)=\mathbb{E}[G \mid s]=\arg\min_{f:S\to \mathbb R} \mathbb{E}\left[(f(s)-G)^2\right]
$$

Is a regression problem.

> Why the expectation is the argmin? See [here](./reinforcement-learning-homework-0/#notes)
{: .prompt-tip }

The same idea applies to non-linear value function approximation
More generally & abstractly, think of function approximation as
searching over a restricted **function space**, which is a set whose
members are functions that map states to real values.

E.g. a function space of linear value function approximation:

$$
\mathscr{F}=\left\{\mathrm{V}_\theta: \theta \in \mathbb{R}^{\mathrm{d}}\right\} \text {, where } \mathrm{V}_\theta(\mathrm{s})=\theta^{\top} \phi(\mathrm{s})
$$

- typically only a small subset of all possible functions
- Using "all possible functions" = tabular!
- Equivalently, tabular MC value prediction can be recovered by choosing $\phi$ as the identity features $\phi(\mathrm{s})=\left\\{\mathbb{I} \left[\mathrm{~s}=\mathrm{s}^{\prime}\right]\right\\}_{\mathrm{s}^{\prime} \in \mathrm{S}}$

Find the function:

$$
\min _{V_\theta \in \mathscr{F}} \frac{1}{n} \sum_{i=1}^n\left(V_\theta\left(s_i\right)-G_i\right)^2
$$

SGD: uniformly sample $i$ and

$$
\theta \leftarrow \theta-\alpha \cdot\left(\mathrm{V}_\theta\left(\mathrm{s}_{\mathrm{i}}\right)-\mathrm{G}_{\mathrm{i}}\right) \cdot \nabla \mathrm{V}_\theta\left(\mathrm{s}_{\mathrm{i}}\right)
$$

### Interprete Td(0) with Linear Approximation

TD(0) iteration is equivalent to

$$
\theta \leftarrow \theta+\alpha\left(G_t-\phi\left(s_t\right)^{\top} \theta\right) \phi\left(s_t\right) .
$$

Here $\theta$ is the tabular value function and $\phi$ is $[0,\cdots, 0, 1, 0, \cdots, 0]$, as mentioned [here](#value-prediction-with-function-approximation).

### TD(0) with Linear Approximation

In TD(0), we do

$$
V\left(s_t\right) \leftarrow V\left(s_t\right)+\alpha\left(r_t+\gamma V\left(s_{t+1}\right)-V\left(s_t\right)\right) ,
$$

which, with all steps on $t$, gets

$$
V_{k+1} \leftarrow \mathcal{T}^\pi V_k .
$$

i.e.

$$
V_{k+1}(s)=\mathbb{E}_\pi\left[r+\gamma V_k\left(s^{\prime}\right) \mid s\right]
$$

Similar to Linear Approximation, **rewriting expectation with a regression problem**,

$$
\begin{gathered}    
V_{k+1}(s)=

\arg\min_{f:s\to \mathbb{R}} \mathbb{E}_\pi\left[ \big(f(s)-(r+\gamma V_{s})\big)^2\right] \\

\approx \arg\min_{V_\theta\in \mathscr{F}} \frac{1}{n} \sum_{i=1}^n\big(V_\theta(s_i)-r_i-\gamma V_k(s^{\prime})\big)^2 . \\

\end{gathered}
$$

And the SGD steps should be

$$
\theta \leftarrow \theta+\alpha\left(V_\theta\left(s_t\right)-r_t-\gamma V_k\left(s_{t+1}\right)\right) \nabla V_\theta\left(s_t\right)
$$