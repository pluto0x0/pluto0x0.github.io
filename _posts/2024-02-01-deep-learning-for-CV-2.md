---
title: Deep Learning for Computer Vision (2)
date: 2024-02-01 01:25:06
img_path: /_posts/
math: true
mermaid: true
categories: CourseNotes
tags: CS444
image:
  path: ../upload/img/2024-02-01-deep-learning-for-CV-2-image.png
---

## The basic supervised learning framework

$$
y = f(x)
$$

- $y$: output
- $f$: prediction function
- $x$: input

training:

$$
{(x_1,𝑦1), …, (x_N,Y_N)}
$$ 

## Nearest neighbor classifier

$f(x)$ = label of the training example nearest to $x$

K-nearest neighbor classifier:

![Alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-1.png){: .w="70"}

![Alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-2.png){: .w="70"}

## Linear classifier

![Alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-3.png){: .w="50"}

![Alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-4.png){: .w="50"}

$$
f(x) = \operatorname{sgn} (w\cdot x + b)
$$

<details markdown="1">
<summary>NN vs. linear classifiers: Pros and cons</summary>

NN pros:

- Simple to implement
- Decision boundaries not necessarily linear
- Works for any number of classes
- Nonparametric method
NN cons:
- Need good distance function
- Slow at test time
Linear pros:
- Low-dimensional parametric representation
- Very fast at test time
Linear cons:
- Works for two classes
- How to train the linear function?
- What if data is not linearly separable?

</details>
