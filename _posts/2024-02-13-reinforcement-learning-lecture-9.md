---
title: Reinforcemant Learning (9)
date: 2024-02-13 14:03:05
img_path: /_posts/
math: true
mermaid: true
categories:
- Course Notes
- Reinforcement Learning
---

## recap

in policy iteration, appply greedy algo very time.

\#steps are finite.

## another proof

### performance-difference lemma (P-D lemma)

> this is a fundamental tool in RL.
> many deep RL models relies on this lemma
{: .prompt-info }

$\forall \pi,\pi', s$,

$$
V^{\color{red}{\pi'}}(s) - V^{\pi}(s) = \frac{1}{1-\gamma} E_{s'\sim d_s^{\color{red}{\pi'}}} \left[Q^\pi(s', {\color{red}{\pi'}})-V^\pi(s')\right]
$$

apply the lemma in the policy iteration steps:

$$
V^{\pi_{k+1}}(s) - V^{\pi_k}(s) = \frac{1}{1-\gamma} E_{s'\sim ?} \left[Q^{\pi_k}(s', \pi_{k+1})-\boxed{V^{\pi_k}(s')}\right]
$$


and 

$$
\boxed{V^{\pi_k}(s')} = Q^{\pi_k}(s', \pi_k)
$$

and RHS $\ge 0$  is trivial. QED

### Proof of lemma

