---
title: MIT18.06 Linear Algebra (4)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-5-6
img_path: /upload/
math: true
---

# lec4

# 基础性质

## 1

$$
⁍
$$

proof.

$$
(A B)\left(B^{-1} A^{-1}\right)=A\left(B B^{-1}\right) A^{-1}=A A^{-1}=I
$$

## 3

$$
(A B)^{\top}=B^{\top} A^{\top}
$$

## 2

$$
\left(A^{\top}\right)^{-1}=\left(A^{-1}\right)^{\top}
$$

proof.

$$
\begin{aligned}A A^{-1} &=I \\\left(A A^{-1}\right)^{\top} &=I^{\top} \\\left(A^{-1}\right)^{\top} A^{\top} &=I^{\top}=I\end{aligned}
$$

# $A=LU$分解

$A=LU$ without row exchange.

$$
A=\begin{array}{c}   \begin{bmatrix}   1 & 0 & 0 \\x & 1 & 0 \\x & x & 1\end{bmatrix} &\begin{bmatrix}   x & x & x \\0 & x & x \\0 & 0 & x\end{bmatrix} \\\text{L(lower)} & \text{U(upper)} \end{array}
$$

when #pivot = 0, need row exchange.

or:

$$
A=\left[\begin{array}{lll}
1 & 0 & 0 \\
x & 1 & 0 \\
x & x & 1
\end{array}\right]\left[\begin{array}{lll}
x & 0 & 0 \\
0 & x & 0 \\
0 & 0 & x
\end{array}\right]\left[\begin{array}{lll}
1 & x & x \\
0 & 1 & x \\
0 & 0 & 1
\end{array}\right]
$$

for $n \times n$ matrix, $\exists n!$ P’s.

# **置换矩阵（Permutation matrix）**

when n = 3, 6 permutation matrices:

$$
\begin{array}{l}{\left[\begin{array}{lll}1 & 0 & 0 \\0 & 1 & 0 \\0 & 0 & 1\end{array}\right]\left[\begin{array}{lll}0 & 1 & 0 \\1 & 0 & 0 \\0 & 0 & 1\end{array}\right]\left[\begin{array}{lll}0 & 0 & 1 \\0 & 1 & 0 \\1 & 0 & 0\end{array}\right]} \\{\left[\begin{array}{lll}1 & 0 & 0 \\0 & 0 & 1 \\0 & 1 & 0\end{array}\right]\left[\begin{array}{lll}0 & 1 & 0 \\0 & 0 & 1 \\1 & 0 & 0\end{array}\right]\left[\begin{array}{lll}0 & 0 & 1 \\1 & 0 & 0\\0 & 1 & 0\end{array}\right]}\end{array}
$$

$$
P^{-1}=P^{T}
$$

e.g. 

$$
\begin{array}{c}   \begin{bmatrix} 0 &0  &1 \\  1& 0 &0 \\0  & 0 &1\end{bmatrix} \\ A\end{array}
\begin{array}{c}   \begin{bmatrix} 0 &1  &0 \\  0& 0 &1 \\ 1& 0 &0\end{bmatrix} \\ A\end{array}=\begin{array}{c}   \begin{bmatrix} 1 &0  &0 \\  0& 1 &0 \\0  & 0 &1\end{bmatrix} \\ C\end{array}
$$

proof.

$$
\begin{array}{l}\because A_{i j}=1 \Rightarrow \text { row i of } C=\text { row j of } B \\\therefore \text { row j of } B=\text { col j of } A \\\therefore C_{i i}=A_{i j}=1 \\C=I\end{array}
$$