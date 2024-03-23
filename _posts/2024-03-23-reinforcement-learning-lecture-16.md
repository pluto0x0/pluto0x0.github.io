---
title: Reinforcemant Learning (16)
date: 2024-03-22 17:02:00
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Reinforcement Learning
---

## Q-learning

Update rule:

$$
Q\left(s_t, a_{t}\right) \leftarrow Q\left(s_{t}, a_{t}\right)+\alpha\left(r_{t}+\gamma \max _{a^{\prime}} Q\left(s_{t+1}, a^{\prime}\right)-Q\left(s_{t}, a_{t}\right)\right)
$$

Q-learning is off-policy: how we take actions have nothing to do with our current Q-estimate (or its greedy policy). i.e. Q-learning always taks $\max _{a^{\prime}} Q\left(s_{t+1}, a^{\prime}\right)$ no matter what the real policy is.

e.g. in the cliff setting, the optimal can always be found, no matter the choice of $\epsilon$.

### Exercise: Multi-step Q-learning?

Does the target $r_{t}+\gamma r_{t+1}+\gamma^2 \max _{a^{\prime}} Q\left(s_{t+2}, a^{\prime}\right)$ work? If not, why?