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

### Example: Tetris Game

![alt text](../upload/img/2024-03-20-reinforcement-learning-lecture-14-image-1.png)
_Tetris Game_

The state space is exponentially large: each block be occupied / not occupied.

Featurize: # of blocks on each column. In the example, the feature is $
(4\;4\;5\;4\;3\;3\;3\;\cdots)$

### Monte-Carlo Vaule Prediction

$$
V^\pi(s)=\mathbb{E}[G \mid s]=\argmin_{f:S\to \mathbb R} \mathbb{E}\left[(f(s)-G)^2\right]
$$