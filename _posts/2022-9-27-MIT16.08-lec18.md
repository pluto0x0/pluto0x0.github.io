---
title: MIT18.06 Linear Algebra (18)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec18

$$
\left|\begin{array}{ll}a & b \\c & d\end{array}\right|=a d-b c
$$

# determinate

- $\det I=1$
- Exchange rows, reverse sign of $\det$ , so $\det P=1$ or $-1$
- $\begin{vmatrix} ta & tb\\ c & d\end{vmatrix} =t\begin{vmatrix} a & b\\ c & d\end{vmatrix}$
- $\begin{vmatrix} a+a' & b+b'\\ c & d\end{vmatrix} =\begin{vmatrix} a & b\\ c & d\end{vmatrix} + 
\begin{vmatrix} a' & b'\\ c & d\end{vmatrix}$
- If two rows are equal, $\det=0$
- substract $l*row$ from rows, $\det$ remain same.

## triangular

$$
\begin{vmatrix}
 d_1 & * & *\\
 0 & d_2 & * \\
 0 & 0 & d_3
\end{vmatrix} = 
d_1d_2d_3
$$

if the matrix is singular, $\det = 0$.

- $\det AB=(\det A)(\det B)$, $\det A^{-1} = \frac{1}{\det A}$ ($A$ is invertible)
- $\det 2A=2^n\det A$
- $\det A^\top =\det A$