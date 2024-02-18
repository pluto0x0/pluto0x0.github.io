---
title: MIT18.06 Linear Algebra (8)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-26
img_path: /upload/
math: true
---

# lec8

# Solve $Ax=b$

$$
\left[\begin{array}{llll}1 & 2 & 2 & 2 \\2 & 4 & 6 & 8 \\3 & 6 & 8 & 0\end{array}\right]\left[\begin{array}{l}x_{1} \\x_{2} \\x_{3} \\x_{4}\end{array}\right]=\left[\begin{array}{l}b_{1} \\b_{2} \\b_{3}\end{array}\right](Ax=B)
$$

4 variables, 3 equations.

$$
\left[\begin{array}{llll|l}1 & 2 & 2 & 2 & b_{1} \\2 & 4 & 6 & 8 & b_{2} \\3 & 6 & 8 & 10 & b_{3}\end{array}\right] \rightarrow\left[\begin{array}{llll|l}1 & 2 & 2 & 2 & b_{1} \\0 & 0 & 2 & 4 & b_{2}-2 b_{1} \\0 & 0 & 0 & 0 & b_{3}-b_{2}-b_{1}\end{array}\right]
$$

$$
\Rightarrow b_3-b_2-b_1=0
$$

## solvability

$Ax=b$ is solvable when $b$ is in $C(A)$ .

## steps

1. Find particular $x_p$ so that $Ax_p=b$
    - set all free variables = 0
    - find $x_p$
2. Find  so $Ax_n=b$
3. $A(x_p+x_n)=b$

e.g.

$$
\left[\begin{array}{llll}1 & 2 & 2 & 2 \\2 & 4 & 6 & 8 \\3 & 6 & 8 & 10\end{array}\right]\left[\begin{array}{l}x_{1} \\x_{2} \\x_{3} \\x_{4}\end{array}\right]=\left[\begin{array}{l}1 \\5 \\6\end{array}\right]
$$

$$
\left[\begin{array}{cccc|c}{\color{Red} 1}  & 2 & 2 & 2 & 1 \\0 & 0 & {\color{Red}2}  & 4 & 3 \\0 & 0 & 0 & 0 & 0\end{array}\right]\\ {\color{Red} \text{pivots}} 
$$

row $\left[\begin{array}{llll|l}0 & 0 & 0 & 0 & 0\end{array}\right]$ tell that it is **solvable.**

- free variables: $x_2,x_4$,
- set $x_2=x_4=0$
- $\left\{ \begin{aligned}
1x_1+2x_2+2x_3+2x_4&=1\\
2x_3+4x_4&=3
\end{aligned}\right.
\Rightarrow
x_p=\left[\begin{array}{c}
-2 \\
0 \\
3 / 2 \\
0
\end{array}\right]$
- set free variables = $\begin{bmatrix} 1\\0\end{bmatrix}$and $\begin{bmatrix} 1\\0\end{bmatrix}$, get $x_{n}=\left[\begin{array}{c}-2 \\1 \\0 \\0\end{array}\right] \text { and }\left[\begin{array}{r}2 \\0 \\-2 \\1\end{array}\right]$
- $X_{\text {complete }}=\left[\begin{array}{c}-2 \\0 \\3 / 2 \\0\end{array}\right]+C_{1}\left[\begin{array}{c}-2 \\1 \\0 \\0\end{array}\right]+C_{2}\left[\begin{array}{c}2 \\0 \\-2 \\1\end{array}\right]$