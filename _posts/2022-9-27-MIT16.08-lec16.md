---
title: MIT18.06 Linear Algebra (16)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec16

# Least square

find a line $y=C+Dx$ through: $(1,1)(2,2)(3,2)$:

$$
\begin{bmatrix} 1 & 1\\ 1 & 2\\ 1 & 3\end{bmatrix}\begin{bmatrix} C \\ D\end{bmatrix}=\begin{bmatrix}1 \\ 2 \\ 2\end{bmatrix}
$$

in the form of

$$
Ax=b
$$

Minimize : 

$$
\Vert Ax-b\Vert ^2=\Vert e\Vert ^2
$$

that is, finding $P$ (**projection** vector)

$$
A\hat x=P
$$

Steps:

$$
\begin{align}A^\top (b-A\hat x) & = 0 \\A^\top b & = A^\top A\hat x \\\hat x & = (A^\top A)^{-1} A^\top b\end{align}
$$

get:

$$
\hat x = \begin{bmatrix} C \\ D\end{bmatrix}=\begin{bmatrix} 2/3\\1/2\end{bmatrix}
$$

which means the line is

$$
y=\frac{1}{2}x+\frac{2}{3} 
$$

# When $A^\top A$ is invertible

If  $A$ has independent columns, then $A^\top A$ is invertible.

to prove: if $A$ has dependent cols, if $A^\top A x=0$ then $x=0$

$N(A^\top A) =N(A)$ see [proof of $N(A^\top A)=N(A)$ ](lec14%20e323f8c6256b4c4f8fd632761950a29f.md) 

trick

$$
\begin{aligned}
A^\top Ax & = 0 \\
x^\top A^\top A x & = 0\\
(Ax)^\top Ax & = 0 \\
Ax & = 0 \text{(square)} \\
x & = 0 \text{(A has independent columns)} 
\end{aligned}
$$

that means  $A$ is invertible.

# Special case of independent columns

Columns are **perp. unit vectors.**

e.g.

orthonormal vector