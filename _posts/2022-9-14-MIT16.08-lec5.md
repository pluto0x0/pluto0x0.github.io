---
title: MIT18.06 Linear Algebra (5)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-14
img_path: /upload/
math: true
---

# lec5

# $A=LU$

$\forall$  invertible $A$, $\exists PA=LU$

# transpose

$$
\left(A^{\top}\right)_{i j}=A j i
$$

# Symmetrix Matrix

$$
A^{\top}=A
$$

$R^{\top}R$ is always symmetric.

proof. $\left(R^{\top} R\right)^{\top}=R^{\top} R$

# Vector Space

e.g.

$\mathbb{R} ^2$ is all 2-d real vectors.

Vector space is **closed** to **addition** and **multiplication**.

# Subspace

Subspace of $\mathbb{R}^2$:

- $\mathbb{R}^2$
- any line through $\begin{bmatrix} 0\\0\end{bmatrix}$
- only $0$ vector

## Subspace of matrices

All the combinations of the column vectors of $A$ is called column space $C(A)$.