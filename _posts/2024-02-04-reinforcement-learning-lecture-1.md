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
V^*(d) = \min\{3 + V^*(g) ,\, 2 + V^*(f)\
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


## Model-based RL:

The states are unknown.
Learn by **trial-and-error**

![alt text](../upload/img/2024-02-04-reinforcement-learning-lecture-1-image-2.png){: w="500" }
_a trajectory: s0>c>e>F>G_

Need to recover the graph by collecting multiple **trajectories**.

Use imperial frequency to find probabilities.

Assume states & actions are visited uniformly.

### exploration problem

Random exploration can be inefficient:

![alt text](../upload/img/2024-02-04-reinforcement-learning-lecture-1-image-5.png){: h="400" }
_example: video game_

## example: video game

Objective: 

$$
\mathbb{E}\left[\sum_{t=1}^{\infty} r_t \mid \pi\right] \; \text{or} \;
\mathbb{E}\left[\sum_{t=1}^{\infty} \gamma^{t-1} r_t \mid \pi\right]
$$

Problem: the graph is too large

![alt text](../upload/img/2024-02-04-reinforcement-learning-lecture-1-image-4.png){: w="300" }

- there are states that the RL model have never seen.
- therefore need generalization
- 