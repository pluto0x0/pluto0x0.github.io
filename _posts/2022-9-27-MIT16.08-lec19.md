---
title: MIT18.06 Linear Algebra (19)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec19

# 2x2 $\det$

$$
\left|\begin{array}{ll}a & b \\c & d\end{array}\right|=\left|\begin{array}{ll}a & 0 \\c & d\end{array}\right|+\left|\begin{array}{ll}0 & b \\c & d\end{array}\right|=\left|\begin{array}{ll}a & 0 \\c & 0\end{array}\right|+\left|\begin{array}{ll}a & 0 \\0 & d\end{array}\right|+\left|\begin{array}{cc}0 & b \\c & 0\end{array}\right|+\left|\begin{array}{ll}0 & b \\0 & d\end{array}\right| = ad-bc
$$

# 3x3 $\det$

what the survivors for 

$$
\begin{vmatrix} a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{vmatrix}
$$

?

$$
\begin{vmatrix} a_{11} & 0 & 0\\ 0 & a_{22} & 0\\ 0 & 0 & a_{33}\end{vmatrix}+\begin{vmatrix} a_{11} & 0 & 0\\ 0 & 0 & a_{23}\\ 0 & a_{32} & 0\end{vmatrix}+ \cdots
$$

$$
=a_{11}  a_{22}  a_{33}
-
a_{11}  a_{23} a_{32} 
\cdots

$$

# Big formula

$$
\operatorname{det} A=\sum_{n! \text { terms}} \pm a_{1\alpha} a_{2 \beta} a_{3\gamma} \cdots a_{n \omega}
$$

where $(\alpha, \beta, \gamma,\ldots, \omega)=\text { perm. of }(1,2, \ldots, n)$

# cofactor

$$
⁍
$$

[子式和余子式 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%AD%90%E5%BC%8F%E5%92%8C%E4%BD%99%E5%AD%90%E5%BC%8F)