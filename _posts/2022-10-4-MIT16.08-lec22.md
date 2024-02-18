---
title: MIT18.06 Linear Algebra (22)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-10-4
img_path: /upload/
math: true
---

# lec22

We have $n$ independent eigenvectors of $A$, and put them in columns of matrix $S$.

# $AS$

$$
AS=\begin{bmatrix}
 \vdots &  & \vdots\\
 \lambda_1x_1 & \cdots & \lambda_nx_n\\
 \vdots &  & \vdots
\end{bmatrix}=
\begin{bmatrix}
 \vdots &  & \vdots\\
 x_1 & \cdots & x_n\\
 \vdots &  & \vdots
\end{bmatrix}
\begin{bmatrix}
 \lambda_1 & 0 & 0\\
 0 & \ddots  & 0\\
 0 & 0 & \lambda_n
\end{bmatrix}
=S\Lambda
$$

if $n$ eigen vectors are independent, 

$$
\begin{aligned}
AS & = S\Lambda \\
S^{-1}AS & = \Lambda\\
A & = S\Lambda S^{-1}
\end{aligned}
$$

# eigenvalues of $A^2$

if

$$
Ax=\lambda x
$$

$$
A^2x=\lambda Ax=\lambda^2 x
$$

also

$$
A^2 = S\Lambda S^{-1}S\Lambda S^{-1}=S\Lambda^2S^{-1}
$$

$$
A^k = S\Lambda^kS^{-1}
$$

$A$ has **independent eigenvectors** if all $\lambda$s are **different**.

If have **repeated eigenvalues**, may or may not have n **independent eigenvectors**.

# $u$

start with given vector $u_0$

$$
⁍
$$

$$
\rightarrow u_k=A^k u_0
$$

## solve $u_{100}$

write $u_0$ as combination of eigenvectors.

$$
u_0 = c_1x_1+c_2x_2+\cdots+c_nx_n
$$

then calculate $Au_0$:

$$
Au_0 = c_1Ax_1+c_2Ax_2+\cdots+c_nAx_n \\
 = c_1 \lambda_1 x_1+c_2\lambda_2 x_2+\cdots+c_n\lambda_n x_n \\
$$

$$
A^{100}u_0 = c_1 \lambda_1^{100} x_1+c_2\lambda_2^{100} x_2+\cdots+c_n\lambda_n^{100} x_n \\
$$

$$
 A u_{0}=S \Lambda S^{-1} u_{0}=S \Lambda S^{-1}(S c)=S \Lambda c\\
u_{100} = A^{100} u_{0}=S \Lambda^{100} c
$$

# Example of Fib. Sequence

$$
F_{k+2}=F_{k+1}+F_{k}
$$

  

$$
u_k = \left[\begin{array}{c}F_{k+1} \\F_{k}\end{array}\right],u_{k+1}=\left[\begin{array}{ll}1 & 1 \\1 & 0\end{array}\right]\left[\begin{array}{c}F_{k+1} \\F_{k}\end{array}\right]=A u_k
$$

Find eigenvalue of $A$:

$$
\lambda ^2 - \lambda -1=0 \Rightarrow \lambda =\frac{1\pm \sqrt[]{5} }{2} 
$$