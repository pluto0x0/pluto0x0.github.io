---
title: MIT18.06 Linear Algebra (1-3)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-13
img_path: /upload/
math: true
---

# 矩阵乘法的性质

顺序不能改变，可以任意添加括号

$$
(AB)C=A(BC)
$$

# 矩阵乘法的定义

## 从单个元素

$$
C_{ij}=\sum_{k}A_{ik}B_{kj}
$$

## 从列

![Clip_20220306_122632.png](Clip_20220306_122632.png)

A * col 1 of B = col 1 of C
cols of B 对 cols of A的线性组合

## 从行

row 1 of A * B = row 1 of C

![Clip_20220306_134437.png](Clip_20220306_134437.png)

## 列x行

$$
\begin{bmatrix}  a&b \\  c&d\end{bmatrix}\begin{bmatrix}  e & f & g \\  h & i & j\end{bmatrix} =\begin{bmatrix}  a \\  c\end{bmatrix}\begin{bmatrix}  e & f & g\end{bmatrix}+\begin{bmatrix}  b \\  d\end{bmatrix}\begin{bmatrix}  h & i & j\end{bmatrix}=C
$$

## 矩阵代替元素

$$
\begin{bmatrix}   \begin{array}{c | c}   A_1 & A_2 \\ \hline    A_3 & A_4   \end{array} \end{bmatrix}\begin{bmatrix}   \begin{array}{c | c}   B_1 & B_2 \\ \hline    B_3 & B_4   \end{array} \end{bmatrix}=\begin{bmatrix}   \begin{array}{c | c}   C_1 & C_2 \\ \hline    C_3 & C_4   \end{array} \end{bmatrix} \\C_1=A_1B_1+A_2B_3
$$

# 矩阵的逆（方阵）

## 性质

$$
A^{-1}A=I\text{(单位矩阵)}\\AA^{-1}=I
$$

即 左逆=右逆 （方阵）

矩阵的逆存在时，称矩阵为**可逆**（invertible）或 **非奇异**的（non-singular）

不可逆的矩阵：

e.g.

$$
A=\begin{bmatrix}  1 & 3 \\  2 & 6\end{bmatrix}
$$

$\begin{bmatrix}  1 & 3 \end{bmatrix}$ 与 $\begin{bmatrix}  2 & 6\end{bmatrix}$ 共线，所以$\begin{bmatrix}  1 & 3 \end{bmatrix}$ 与 $\begin{bmatrix}  2 & 6\end{bmatrix}$ 的线性组合无法得到$\begin{bmatrix}  1 & 0\end{bmatrix}$或$\begin{bmatrix}  0 & 1 \end{bmatrix}$

$$
⁍
$$

$$
proof.\;if  \exists A^{-1}: \\(A^{-1}A)x=Ix=x \\A^{-1}(Ax)=A^{-1}0=0 \\ \Rightarrow x=0
$$

## 求解逆矩阵：Gauss- Jordan消元法

e.g.

$$
A=\begin{bmatrix} 1 & 3\\ 2 & 7\end{bmatrix} , A^{-1} = ?
$$

$$
\begin{align}   &\begin{array}{c}   \begin{bmatrix} \begin{array}{cc|cc}1 & 3 & 1 & 0 \\2 & 7 & 0 & 1\end{array}\end{bmatrix} \\A\;\;\;I\end{array}\\\to &\begin{array}{c}   \begin{bmatrix} \begin{array}{cc|cc}1 & 3 & 0 & 1 \\0 & 1 & -2 & 1\end{array}\end{bmatrix}\end{array} \\\to &\begin{array}{c}   \begin{bmatrix} \begin{array}{cc|cc}1 & 0 & 7 & -3 \\0 & 1 & -2 & 1\end{array}\end{bmatrix}\\I \;\;\;\;A^{-1}\end{array}\end{align}
$$

$$
A^{-1} = \begin{bmatrix} 7 & -3\\ -2 & 1\end{bmatrix}
$$

$$
proof. \\ EA=I\Rightarrow E=A^{-1} \\ IE=E=A^{-1}
$$

## 一般Gauss消元

$$
\begin{align} 
  &\begin{bmatrix}
\begin{array}{ccc|c} 
  1 & 12& 1 & 2 \\
  3 & 8 & 1 & 12 \\
  0 & 4 & 1 & 2 
\end{array}
\end{bmatrix} \\
\to &
\begin{bmatrix}
\begin{array}{ccc|c} 
  1 & 2 & 1 & 2 \\
  0 & 2 & -2 & 6 \\
  0 & 4 & -1 & 2 
\end{array}
\end{bmatrix} \\
\to &
\begin{array}{c} 
  \begin{bmatrix}
\begin{array}{ccc|c} 
  \color{red}{1} & 2 & 1 & 2 \\
  0 & \color{red}{2} & -2 & 6 \\
  0 & 0 & \color{red}{5} & -10 
\end{array}
\end{bmatrix} \\
\color{red}{\text{主元(pivot)}} \\
\text{上三角(upper triangle)矩阵}
\end{array}
\end{align}
$$

进行的初等变换等价于左乘一个消元矩阵 $E$.

e.g.

$$
E=\begin{bmatrix} 1 & 0 & 0\\ -3 & 1 & 0\\ 0 & 0 & 1\end{bmatrix}
$$

$EA$ : substract 3 * row 1 of $A$ from row 2 of $A$.