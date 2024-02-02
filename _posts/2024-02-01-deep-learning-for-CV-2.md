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

![Alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-1.png){: w="300"}

![Alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-2.png){: h="200"}

## Linear classifier

![Alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-3.png){: w="300"}

![Alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-4.png){: w="300"}

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

## Empirical loss minimization

define expected loss

$$
L(f)=\mathbb{E}_{(x, y) \sim D}[l(f, x, y)]
$$

- $0-1$ loss
  - $l(f,x,y) = \mathbb{I}[f(x) \neq y]$
  - $L(f)=\operatorname{Pr}[f(x) \neq y]$
- $l_2$ loss
  - $l(f, x, y)=[f(x)-y]^2$
  - $L(f)=\mathbb{E}\left[[f(x)-y]^2\right]$
  
Find $f$ that minimizes

$$
\hat{L}(f)=\frac{1}{n} \sum_{i=1}^n l\left(f, x_i, y_i\right)
$$

- for $0-1$ loss
  - NP-hard
  - use surrogate loss functions instead
- $l_2$ loss
  - $\hat{L}(f_w) = \frac{1}{n} || Xw-Y ||_2$ is a convex function
  - $0 = \nabla || Xw-Y ||_2 = 2X^T (Xw - Y)$
  - $w = (X^T X)^{-1} X^T Y$

### Interpretation of $l_2$ loss

Assumption:

$y$ is normally distributed with mean $f_w(x) = w^Tx+b$

Maximum likelihood estimation:

$$ w_{ML} = \argmin_w - \sum_i \log P_w(y_i | x_i) $$

$$ w_{ML} = \argmin_w \sum_i - \log \left( \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( - \frac{[y_i-f_w(x_i)]^2}{2\sigma^2} \right) \right) $$

$$ w_{ML} = \argmin_w \sum_i \log \sqrt{2\pi\sigma^2} + \frac{[y_i-f_w(x_i)]^2}{2\sigma^2} $$

$$ w_{ML} = \argmin_w \sum_i [y_i-f_w(x_i)]^2 $$

### Problem of linear regression

![alt text](../upload/img/2024-02-01-deep-learning-for-CV-2-image-5.png)
_Linear regression is very sensitive to outliers_

