---
title: MIT18.06 Linear Algebra (23)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-11-14
img_path: /upload/
math: true
---

# lec23

# differential equation $\frac{\mathrm{d}u}{\mathrm{d}t}=Au$

e.g. Solve

$$
\begin{array}{l}\frac{d u_{1}}{d t}=-u_{1}+2 u_{2} \\\frac{d u_{2}}{d t}=u_{1}-2 u_{2}\end{array}
$$

$$
\longrightarrow \frac{du}{dt} = Au
$$

where

$$
A=\left[\begin{array}{cc}-1 & 2 \\1 & -2\end{array}\right]
$$

and

$$
u(0)=\begin{bmatrix}u_1 \\ u_2\end{bmatrix}=\begin{bmatrix}1\\0\end{bmatrix}
$$

Find eigenvalues and eigenvectors of $A$:

$$
⁍
$$

$$
x_1 = \begin{bmatrix}2 \\ 1\end{bmatrix},x_2 = \begin{bmatrix}1 \\ -1\end{bmatrix}
$$

Then the **general solution** is:

$$
u(t)=c_1e^{\lambda_1t}x_1+c_2e^{\lambda_2t}x_2
$$

=$c_1e^{\lambda_1t}x_1$  and $c_2e^{\lambda_2t}x_2$ are both solutions.

e.g. plug $u=e^{\lambda_1t}x_1$ in $\frac{\mathrm{d}u}{\mathrm{d}t}=Au$,

$$
\lambda_1e^{\lambda_1t}x_1=Ae^{\lambda_1t}x_1 \\ \Rightarrow \lambda_1x_1=Ax_1
$$

1. stability ($u(t) \to 0$) : $\mathrm{Re} \lambda < 0$
2. steady state : $\lambda_1 = 0$ and other $\mathrm{Re} \lambda < 0$
3. blow up : $\forall \mathrm{Re}\lambda<0$

 for $2\times 2$ matrices, how to get $\mathrm{Re}\lambda_1<0, \mathrm{Re}\lambda_2<0$ ?

$$
\lambda_1+\lambda_2=\mathrm{tr}(A)<0\\ \lambda_1\lambda_2=\det(A)>0
$$

# Uncouple $\frac{\mathrm{d}u}{\mathrm{d}t}=Au$

Set

$$
u=Sv
$$

$$
\frac{\mathrm{d}u}{\mathrm{d}t}=S\frac{\mathrm{d}v}{\mathrm{d}t}=Au=ASv
$$

$$
\Rightarrow \frac{\mathrm{d}v}{\mathrm{d}t}=S^{-1} A S v=\Lambda v
$$

i.e.

$$
\frac{\mathrm{d}v_1}{\mathrm{d}t}=\lambda_1 v_1\\\vdots
$$

$v$’s are uncoupled.

So

$$
⁍
$$

$$
\therefore u=Sv = Se^{\Lambda t}v(0)=Se^{\Lambda t}S^{-1}u(0) \\= e^{At}u(0)
$$

> upd: what $e^{\Lambda t}$ means? [e^{\Lambda t}=\begin{bmatrix} e^{\lambda_1 t} & 0 & 0\\ 0 & \ddots  & 0\\ 0 & 0 & e^{\lambda_n t}\end{bmatrix}](lec23%20431e095ef43e40a2a215220f91024327.md)
> 

# Meaning of exponential of a matrix ($Se^{\Lambda t}S^{-1} = e^{At}$)

Taylor Series $e^{x}=\sum \frac{x^{n}}{n !}$:

 

$$
e^{A t}=I+A t+\frac{(A t)^{2}}{2}+\frac{(A t)^{3}}{6}+\cdots+\frac{(A t)^{n}}{n !}+\cdots
$$

also, $\frac{1}{1-x}=\sum_{0}^{\infty} x^{n}$: (for $|\lambda(At)|<1$)

$$
(I-A t)^{-1}=I+A t+(A t)^{2}+(A t)^{3} t+\cdots 
$$

Why $I+A t+\frac{(A t)^{2}}{2}+\frac{(A t)^{3}}{6}+\cdots+\frac{(A t)^{n}}{n !}+\cdots=Se^{\Lambda t}S^{-1}$ ?

$$
\begin{aligned}
e^{At} & = I+A t+\frac{(A t)^{2}}{2}+\frac{(A t)^{3}}{6}+\cdots+\frac{(A t)^{n}}{n !}+\cdots \\ & = SS^{-1}+S\Lambda S^{-1}t + \frac{S\Lambda^2 S^{-1}t^2}{2}+\cdots \\ & = Se^{\Lambda t}S^{-1}
\end{aligned}
$$

Because $\Lambda$  is **diagonal**,  (use Taylor series)

$$
e^{\Lambda t}=\begin{bmatrix} e^{\lambda_1 t} & 0 & 0\\ 0 & \ddots  & 0\\ 0 & 0 & e^{\lambda_n t}\end{bmatrix}
$$

# 2-order differential equation

Solve

$$
y''+by'+ky=0
$$

let

$$
 u= \begin{bmatrix}y' \\ y\end{bmatrix}\\ u'= \begin{bmatrix}y'' \\ y'\end{bmatrix}=\begin{bmatrix}-b & -k \\1 & 0\end{bmatrix}\begin{bmatrix}y' \\ y\end{bmatrix}
$$

that is in the form of $\frac{\mathrm{d}u}{\mathrm{d}t}=Au$