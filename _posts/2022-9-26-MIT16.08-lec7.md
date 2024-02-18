---
title: MIT18.06 Linear Algebra (7)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-26
img_path: /upload/
math: true
---

# lec7

# null space

the $x$ such that $Ax = \begin{bmatrix}
 0\\0\\0\\0
\end{bmatrix}$always gives a vector space. 

*Proof.*

$$
⁍
$$

where $C$ is a constant.

# rank

rank of $A$ = *#pivots* = ***#linear independent vectors.***

e.g.

$$
\begin{aligned}A=&\begin{bmatrix} \color{red}{1}  & 2 & 2 & 2\\ 2 & 4 & 6 & 8\\ 3 & 6 & 8 & 10\end{bmatrix} \\\to &\begin{bmatrix} \color{red}{1} & 2 & 2 & 2\\ 0 & 0 & \color{red}{2} & 4\\ 0 & 0 & 2 & 4\end{bmatrix} \\\to &\begin{bmatrix} \color{red}{1} & 2 & 2 & 2\\ 0 & 0 & \color{red}{2} & 4\\ 0 & 0 & 0 & 0\end{bmatrix} \\&\color{red}{\text{\#pivots=2}}\end{aligned}
$$

$$
\begin{aligned}A=&\begin{bmatrix} \color{red}{1} & 2 & \color{red}{2} & 2\\ \color{red}{0} & 0 & \color{red}{2} & 4\\ \color{red}{0} & 0 & \color{red}{0} & 0\end{bmatrix} \\&\color{red}{\text{pivot columns} } \\&\text{free columns}\end{aligned}
$$

$$
\left[\begin{array}{llll}1 & 2 & 2 & 2 \\0 & 0 & 2 & 4 \\0 & 0 & 0 & 0\end{array}\right]\left[\begin{array}{l}x_{1} \\x_{2} \\x_{3} \\x_{4}\end{array}\right]=0\\\Rightarrow\left\{\begin{array}{r}
x_{1}+2 {\color{Red} x_{2}} +2 x_{3}+2{\color{Red}  x_{4}} =0\\
2 x_{3}+4 {\color{Red} x_{4}} =0
\end{array}\right.
$$

$x_2, x_4$ can be any number (free column)

Let $\left[\begin{array}{l}x_{2} \\x_{4}\end{array}\right]=\left[\begin{array}{l}1 \\0\end{array}\right]$,

$x=\left[\begin{array}{c}x_{1} \\1 \\x_{3} \\0\end{array}\right] \rightarrow\left[\begin{array}{c}-2 \\1 \\0 \\0\end{array}\right]$

(special solution 1)

Let $\left[\begin{array}{l}x_{2} \\x_{4}\end{array}\right]=\left[\begin{array}{l}1 \\1\end{array}\right]$

$x=\left[\begin{array}{c}x_{1} \\0 \\x_{3} \\1\end{array}\right] \rightarrow\left[\begin{array}{c}2 \\0 \\-2 \\0\end{array}\right]$

(special solution 2)

$x=c\left[\begin{array}{c}-2 \\1 \\0 \\0\end{array}\right]+d\left[\begin{array}{c}2 \\0 \\-2 \\0\end{array}\right]$

is the null space

# RREF (reduced row echelon form)

$$
\begin{aligned}&\left[\begin{array}{llll}1 & 2 & 2 & 2 \\0 & 0 & 2 & 4 \\0 & 0 & 0 & 0\end{array}\right] \text{(U:upper)}\\\to & \left[\begin{array}{llll}1 & 2 & 0 & 2 \\0 & 0 & 2 & 4 \\0 & 0 & 0 & 0\end{array}\right] \\\to &\left[\begin{array}{cccc}1 & 2 & 0 & -2 \\0 & 0 & 1 & 2 \\0 & 0 & 0 & 0\end{array}\right] \text{(R:reduced row echelon form)}\end{aligned} 
$$

$$
\left[\begin{array}{cccc}1 & 2 & 0 & -2 \\0 & 0 & 1 & 2 \\0 & 0 & 0 & 0\end{array}\right] \stackrel{\text { col exchange }}{\longrightarrow}\left[\begin{array}{cc|cc}1 & 0 & 2 & -2 \\0 & 1 & 0 & 2 \\\hline 0 & 0 & 0 & 0\end{array}\right] \left( \begin{bmatrix}
\begin{array}{c|c} 
I & F\text{(free vaible)} \\ \hline
Z\text{(zeros)} & Z\text{(zeros)}
\end{array}
\end{bmatrix}\right )
$$

# Special solution

$$
\begin{bmatrix} I & F\end{bmatrix}\begin{bmatrix} -F\\I\end{bmatrix}=0
$$

$\begin{bmatrix} -F\\I\end{bmatrix}$is a special solution.

e.g.

$$
I=\begin{bmatrix} 1 & 0\\ 0 & 1\end{bmatrix},F=\begin{bmatrix}1 \\ 1\end{bmatrix}
$$

then $x=\begin{bmatrix}-1 \\-1 \\1\end{bmatrix}$is the special solution.

null space = $c\begin{bmatrix}-1 \\-1 \\1\end{bmatrix}$($\dim N(A) = \text{\#cols of A} - r=1$ )