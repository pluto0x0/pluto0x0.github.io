---
title: MIT18.06 Linear Algebra (17)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec17

# Orthonormal vectors

$$
q_{i}^\top q_j=\left\{\begin{array}{ll}0 & \text { if } i \neq j \\1 & \text { if } i=j\end{array}\right.
$$

$$
⁍
$$

So $Q^\top = Q^{-1}$

We call  $Q$ **orthonormal** matrix when it’s **square**.

## **Hadamard matrix**

Let  $H$ be the n order Hadamard matrix, then 

$$
⁍
$$

is 2n order Hadamard matrix.

e.g.

$$
\begin{align}
H_1 & = \begin{bmatrix}1\end{bmatrix} \\
H_2 & = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \\
H_4 & = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 \end{bmatrix} \\
\vdots
\end{align}
$$

$\frac{1}{2}H_4$ is an orthonormal matrix.

# Gram-Schmidt

From any two vectors $a ,b$, get two orthogonal vectors $A,B$, and then get two orthonormal vectors $q_1, q_2$.

## Gram

$$
A=a
$$

$$
B=b-\frac{A^\top b}{A^\top A}A
$$

i.e. $B$ is the error vector $e$ in [lec15](https://www.notion.so/lec15-1cf9bf9e292c4607b7d24e1ebf2cbe9c?pvs=21), which is **perpendicular** to $A$, i.e. $A^\top B=0$

$$
C = c - \frac{A^\top C}{A^\top A}A - \frac{B^\top C}{B^\top B}B
$$

 $c$ is a known vector.

## Schmidt

$$
q_1 := \frac{A}{\Vert A\Vert }\\ q_2 := \frac{B}{\Vert B\Vert }\\ q_3 := \frac{C}{\Vert C\Vert }\\
$$

## $A=QR$

$$
A:=\begin{bmatrix} \vdots & \vdots\\a & b\\ \vdots & \vdots\end{bmatrix}
$$

$$
Q:=\begin{bmatrix} \vdots & \vdots\\q_1 & q_2\\ \vdots & \vdots\end{bmatrix}
$$

then

$$
⁍
$$

where $R$ is an upper triangular matrix.

Because:

$$
\begin{bmatrix}a  & b\end{bmatrix} =\begin{bmatrix}q_1  & q_2\end{bmatrix}\begin{bmatrix}a^\top q_1 & b^\top q_1 \\a^\top q_2 & b^\top q_2\end{bmatrix}
$$