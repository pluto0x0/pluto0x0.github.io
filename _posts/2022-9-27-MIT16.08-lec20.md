---
title: MIT18.06 Linear Algebra (20)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec20

# 2x2 inverse

$$
\left[\begin{array}{ll}a & b \\c & d\end{array}\right]^{-1}=\frac{1}{a d-b c}\left[\begin{array}{cc}d & -b \\-c & a\end{array}\right]
$$

# inverse

$$
A^{-1}=\frac{1}{\det A} C^{\top}
$$

for cofactor $C$, see [cofactor](lec19%20505965e578ce42dc84cc6817c92e5549.md) 

## proof

check:

$$
A C^\top=(\det A) I
$$

$$
\left[\begin{array}{ccc}
a_{11} & \cdots & a_{1 n} \\
\vdots & & \vdots \\
a_{n 1} & \cdots & a_{n n}
\end{array}\right]\left[\begin{array}{ccc}
C_{11} & \cdots & C_{n 1} \\
\vdots & & \vdots \\
C_{1 n} & \cdots & C_{nn} \\
\end{array}\right]
=
\left[\begin{array}{cccc}
    \det A & 0 & 0 \\
    0 & \ddots & 0 \\
    0 & 0 & \det A
    \end{array}\right]
$$

why get 0?

in $A=\left[\begin{array}{ll}a & b \\c & d\end{array}\right]^{-1},C^\top = \left[\begin{array}{cc}d & -b \\-c & a\end{array}\right]$:

$$
 a(-b)+ba
$$

means:

$$
\begin{vmatrix} a & b\\ a & b\end{vmatrix} = 0
$$

# Cramer's rule

Solve $Ax=b$

$$
x=A^{-1}b=\frac{1}{\det A}C^\top b
$$

then

$$
x_j=\frac{\det B_j}{\det A}
$$

where

$$
B_j = 
\left[\begin{array}{cccccc}
    a_{11} & \cdots & a_{1\,j-1} & b_{1} & a_{1 \,j+1} & \cdots & a_{1 n} \\
    a_{21} & \cdots & a_{2\,j-1} & b_{2} & a_{2 \, j+1} & \cdots & a_{2 n} \\
    \vdots & & \vdots & \vdots & \vdots &  & \vdots \\
    a_{n 1} & \cdots & a_{n\,j-1} & b_{n} & a_{n\,j+1} & \cdots & a_{n n}
    \end{array}\right]
$$

Because:

$$
x_1 \det A= \det B_1=\begin{vmatrix}
 \vdots & A_{12} & \cdots & A_{1n}\\
b & \vdots &  & \vdots \\
\vdots & A_{n2} & \cdots & A_{nn}
\end{vmatrix}
 = b_1C_{11} + \cdots + b_nC_{n1}
=
C^\top b
$$

# determinate and volume

find area of $\triangle OAB$:

$$
\frac{1}{2} \begin{vmatrix} x_A & y_A \\ x_B & y_B\end{vmatrix}
$$

find area of $\triangle ABC$:

$$
\frac{1}{2} \begin{vmatrix} x_A & y_A & 1\\ x_B & y_B & 1\\ x_C & y_C & 1\end{vmatrix}
$$