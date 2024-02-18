---
title: MIT18.06 Linear Algebra (11)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec11

# matrix space

$S$ : space of 3x3 symmetric matrix : 6 dimension

$U$: space of 3x3 upper triangular matrix : 6 dimension

$S\cup U$ is not a matrix space.

$S\cap U$ is a matrix space, $\dim(S\cap U)=3$

$S+U$ : any of $S$ **+** any of $U$ = all 3x3’s.

$\dim(S+U)=9$

$\dim(S + U) + \dim(S \cap U) = \dim(S) + \dim(U) = 12$

solution to:

$$
\frac{d^2y}{dx^2}+y=0
$$

is

$$
y=c_1\sin x+c_2\cos x
$$

$y$ is a vector space, too.

All **rank 1 matrix** : $A=UVT$ where $U,V$ are column vectors.

All matrix can be a combination of **rank one matrices**.

All rank 4 matrices is **not** a matrix space.  $rank(A + B) \le rank(A) + rank(B)$

$S$ = all $V$ in $\mathbb{R}^4$ with $v_1+v_2 + v_3 + v_4 = 0$

$S$ is a vector space, $\dim(S) = 3$

$S$ is null space to $A = \begin{bmatrix}1 & 1 & 1 & 1\end{bmatrix}$ i.e. $AV = 0$ $S$ 是 $A = \begin{bmatrix}1 & 1 & 1 & 1\end{bmatrix}$ 的空空间，即 $AV = 0$ ,kms

$\dim N(A) = n − r$

e.g. $A = \begin{bmatrix} 1 & 1 & 1 & 1 \end{bmatrix}, r = 1, n = 4, \dim N(A) = 4 - 1 = 3$

$A = \begin{bmatrix}1 \text{(pivot)} & | & 1 & 1 & 1 \text{(free varibles)}\end{bmatrix}$

Basis for $S$ i.e. Special solution for $N(A)$:

$\begin{bmatrix}  -1\\1\\0\\0 \end{bmatrix}, \begin{bmatrix}  -1\\0\\1\\0 \end{bmatrix}, \begin{bmatrix}  -1\\0\\0\\1 \end{bmatrix}$

$N(AT)={0}, \dim N(AT) =0$

# small world graph

## Graph

**Graph = {nodes, edges}**