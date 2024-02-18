---
title: MIT18.06 Linear Algebra (21)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-28
img_path: /upload/
math: true
---

# lec21

# eigen vector

find a function, in goes vector $x$, out comes vector $Ax$.

$Ax$ parallel to $x$ i.e. $Ax=\lambda x$

If $A$ is **singular**, $\lambda =0$ is an eigenvalue

## projection matrix

for any $x$ in the plane, $Px=x$ i.e. $\lambda =1$

for any  $x$ perpendicular to the plane, $Px = 0$, i.e. $\lambda = 0$

## All eigenvalues

$n\times n$  matrix has $n$ eigenvalues.

Sum of these eigenvalues = $\operatorname{tr}(A)$ (some if diagonal)

Product of eigenvalues = $\det(A)$

# Solve $Ax=\lambda x$

$$
(A-\lambda I)x=0
$$

$$
\Leftrightarrow  A-\lambda I \; \text{is singular} \Leftrightarrow  \det(A-\lambda I)=0
$$

E.g.

$$
A = \begin{bmatrix}
 3 & 1 \\
 1 & 3 \\
\end{bmatrix}
$$

$$
\det(A-\lambda I)=\begin{vmatrix}
3-\lambda & 1\\
 1 & 3-\lambda 
\end{vmatrix}
=(3-\lambda )^2-1
= \lambda ^2-{\color{Red} 6} \lambda +{\color{Red} 8} \\
(\text{6:trace, 8:det})

$$

# Example for rotation matrix

$$
Q = \begin{bmatrix} 0 & -1\\ 1 & 0\end{bmatrix}
$$

$$
\mathrm{tr}(A)=0=\lambda_1 + \lambda_2 \\\det(A) = 1 = \lambda_1\lambda_2
$$

$$
\lambda_1 = i,\lambda_2=-i \text{(conjugated)}
$$

if $A$ is symmetric, $\lambda$ will have no imaginary parts.

if $A=-A^\top$ , $\lambda$ will have pure imaginary parts.

# Example for triangular matrix

for

$$
\begin{bmatrix} 3 & 1\\ 0 & 3\end{bmatrix}
$$

$$
x_1=\begin{bmatrix}1 \\ 0
\end{bmatrix}
$$

no independent $x_2$.