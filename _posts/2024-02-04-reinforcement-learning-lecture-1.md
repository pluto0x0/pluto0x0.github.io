---
title: Reinforcement Learning (1)
date: 2024-02-04 17:42:46
img_path: /_posts/
math: true
# mermaid: true
category: CourseNotes
tags: CS443
---

## example: Shortest Path

![alt text](../upload/img/2024-02-04-reinforcement-learning-lecture-1-image.png){: w="500"}
_Shortest Path_

- nodes: stats
- edges: actions

Greedy is not optimal.

**Bellman Equation** (Dynamic Programing):  

$$
V^*(d) = \min\{3 + V^*(g) ,\, 2 + V^*(f)\}
$$

## Stochastic Shortest Path

Markov Decision Process (MDP)

![alt text](../upload/img/2024-02-04-reinforcement-learning-lecture-1-image-1.png){: w="500" }
_Stochastic Shortest Path_

**Bellman Equation**

$$
V^*(c) = \min\{4 + 0.7 × V^*(d) + 0.3 × V^*(e) ,\, 2 + V^*(e)\}
$$

optimal policy : $\pi^*$


## Reinforcement Learning:

the states are unknown.
Learn by **trial-and-error**

![alt text](../upload/img/2024-02-04-reinforcement-learning-lecture-1-image-2.png){: w="500" }
_the states are unknown_

