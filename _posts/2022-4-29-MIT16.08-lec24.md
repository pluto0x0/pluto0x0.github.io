---
title: MIT18.06 Linear Algebra (24)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-4-29
img_path: /upload/
math: true
---

# lec24

# Markov Matrix

$$
A=\left[\begin{array}{ccc}.1 & .01 & .3 \\.2 & .99 & .3 \\.7 & 0 & .4\end{array}\right]
$$

## properties

1. All entryis $\ge 0$
2. All columns add to $1$
3.  $\lambda =1$ is an eigen value
4. all other eigen value $|\lambda_i|<1$ 

## steady state

$$
u_k=A^ku_0=c_1\lambda _1x_1+c_2\lambda _2x_2+\cdots+c_n\lambda _nx_n
$$

if $\lambda_1=1$, the steady state of $u_k$ ($k\to \infty$) is $c_1x_1$ i.e. the $x_1$ part of $u_0$.

## why $\lambda =1$ is an eigenvalue?

$$
A-1 I=\left[\begin{array}{ccc}-.9 & .01 & .3 \\.2 & -.01 & .3 \\.7 & 0 & -.6\end{array}\right]
$$

All columns in $A-I$ adds up to $0$ $\stackrel{?}{\longrightarrow}$ $A-I$ is **singular**

Beacuse rows are dependent. 

$$
row_1+row_2+\cdots+row_n=0
$$

i.e. $(1,1,1)$ is in $N((A-I)^\top)$

# Application of Marcov matrix: population

$$
\begin{bmatrix}u_{cal} \\u_{mass}\end{bmatrix}_{0}=\begin{bmatrix}0\\1000\end{bmatrix}
$$

$$
\begin{bmatrix}u_{cal} \\u_{mass}\end{bmatrix}_{k+1} =\begin{bmatrix}.9 & .2 \\.1 & .8\end{bmatrix}\begin{bmatrix}u_{cal} \\u_{mass}\end{bmatrix}_{k}
$$

$.1$ of California population $\to$ Massachusetts 

$.2$ of Massachusetts population $\to$ California

find eigenvalue and eigenvectors:

$$
 \lambda = 1, .7
$$

$$
u_0=\begin{bmatrix}0 \\ 1000\end{bmatrix}=\frac{1000}{3} \begin{bmatrix}2 \\ 1\end{bmatrix}+\frac{2000}{3} \begin{bmatrix}-1 \\ 1\end{bmatrix}
$$

$$
u_{k}=c_{1}{\color{Red} 1} ^{k}\begin{bmatrix}
2 \\
1
\end{bmatrix}+c_{2}(.7)^{k}\begin{bmatrix}
-1 \\
1
\end{bmatrix}
$$

## steady state

$$
u_k=\frac{1000}{3} \begin{bmatrix}2 \\ 1\end{bmatrix}
$$

# Fourier Series

## intro

$x_i$ are orthonormal basis.

$$
v=x_1q_1+x_2q_2+\dots+x_nq_n
$$

How to get $x_i$?

e.g.

$$
q_1^\top v=x_1q_1q_1^\top+0+\cdots+0=x_1
$$

i.e. (writing in the form of matrix)

$$
\begin{aligned}
\begin{bmatrix}
 \vdots &  & \vdots\\
 q_1 & \cdots & q_n\\
 \vdots &  & \vdots
\end{bmatrix}
\begin{bmatrix}
x_1 \\
\vdots  \\
x_n
\end{bmatrix} & = v \\
Qx & = v
\end{aligned}
$$

$$
x=Q^{-1}v=Q^\top v
$$

## Fourier Series

$$
f(x)=a_{0}+a_{1} \cos x+b_{1} \sin x+a_{2} \cos 2 x+b_{2} \sin 2 x+\cdots
$$

$q_i$ are orthogonal, and $\sin$, $\cos$ are orthogonal funtions. How come?

### orthogonal funtions

like inner product, $f=\cos x$ and $g=\sin x$ are orthogonal funtions means:

$$
f^{\top} g=\int_{0}^{2 \pi} f(x) g(x) d x=\left.\frac{1}{2}(\sin x)^{2}\right|_{0}^{2 \pi}=0
$$

find the coefficient:

$$
a_1=\frac{f^\top \cos(x)}{\cos^\top \cos(x)}=\frac{\int_{0}^{2\pi}f(x)\cos(x) \mathrm{d}x}{\int_{0}^{2\pi}\cos(x)^2\mathrm{d}x}=\frac{1}{\pi}\int_{0}^{2\pi}f(x)\cos(x) \mathrm{d}x
$$