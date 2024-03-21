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
: design features $\phi(s) \in \mathbb{R}^d$ ("featurizing states"), and approximate $\mathrm{V}^\pi(\mathrm{s}) \approx \theta^{\top} \phi(\mathrm{s})$