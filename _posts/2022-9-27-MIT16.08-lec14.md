---
title: MIT18.06 Linear Algebra (14)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec14

# orthogonal vectors（正交）

$x^\top y=0$

$\Vert x\Vert ^2+\Vert y\Vert ^2=\Vert x+y\Vert ^2$

## Subspace

Subspace S is orthogonal to subspace T

means: **every vector in S is orthogonal to every vector in T.**

**row space is orthogonal to null space.**

null space and row space are orthogonal **complement** in $\mathbb{R}^n$

that means: null space contains **all** vectors $\bot$ row space.

 

# solve $A^\top A \hat{x}=A^\top B$

from $Ax=B$ to $A^\top A \hat{x} = A^\top B$, to find “best” solution $\hat{x}$.

1. $N(A^\top A)=N(A)$
2. $rank(A^\top A)= rank(A)$
3. $A^\top A$  is invertible iff A has independent columns. (upd@0429: equivalent to 1. and 2. )

## proof of $N(A^\top A)=N(A)$

[Prove $\operatorname{rank}A^TA=\operatorname{rank}A$ for any $A\in M_{m \times n}$](https://math.stackexchange.com/questions/349738/prove-operatornamerankata-operatornameranka-for-any-a-in-m-m-times-n)