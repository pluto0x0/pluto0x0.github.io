---
title: MIT18.06 Linear Algebra (10)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec10

# 4 Subspaces

- column space $C(A)$
- null space $N(A)$
- row space $C(A^\top)$
- **left** null space $N(A^\top)$
    - $N(A^\top)^\top A=0$

$C(A) \neq C(\operatorname{RREF}(A))$

# How to find $N(A^\top)$

$$
\begin{bmatrix}\begin{array}{c|c} A_{m\times n} & I_{m\times m}\end{array}\end{bmatrix}\stackrel{\text{elimination}}{\longrightarrow}\begin{bmatrix}\begin{array}{c|c} R_{m\times n} & E_{m\times m}\end{array}\end{bmatrix}
$$

e.g.

$$
\begin{bmatrix}\begin{array}{cccc|ccc}  1 & 2 & 3 & 1 & 1 & 0 & 0\\ 1 & 1 & 2 & 1 & 0 & 1 & 0\\ 1 & 2 & 3 & 1 & 0 & 0 & 1\end{array}\end{bmatrix}\longrightarrow \begin{bmatrix}\begin{array}{cccc|ccc}  1 & 0 & 1 & 1 & -1 & 2 & 0\\ 0 & 1 & 1 & 0 & 1 & -2 & 0\\ 0 & 0 & 0 & 0 & -1 & 0 & 1\end{array}\end{bmatrix}
$$

$E A=\left[\begin{array}{cccc}-1 & 2 & 0 \\-1 & -1 & 0 \\-1 & 0 & 1\end{array}\right]\left[\begin{array}{llll}1 & 2 & 3 & 1 \\1 & 1 & 2 & 1 \\1 & 2 & 3 & 1\end{array}\right]=\left[\begin{array}{llll}1 & 0 & 1 & 1 \\0 & 1 & 1 & 0 \\0 & 0 & 0 & 0\end{array}\right]=R$

$$
\therefore \begin{bmatrix} -1 & 0 & 1\end{bmatrix}A = \begin{bmatrix} 0 & 0 & 0 & 0\end{bmatrix}=\mathrm{0}^\top  \\N(A^\top)=\begin{bmatrix}-1 \\0 \\1\end{bmatrix}
$$

# Intro to matrix space

all $3\times 3$ matrices.

Subspace:

- diagonal matrices (对角矩阵)
- upper triangular matrices
- symmetric matrices

## dimension

dimension of all $3\times 3$ matrices?

: 9

upd

dimension of all $3\times 3$ upper-triangular matrices : 6