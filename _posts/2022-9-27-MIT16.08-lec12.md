---
title: MIT18.06 Linear Algebra (12)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-9-27
img_path: /upload/
math: true
---

# lec12

# Graph

**Graph : Node, Edge**

![https://s2.loli.net/2022/03/03/NAMjh9YdnCwl2QZ.png](https://s2.loli.net/2022/03/03/NAMjh9YdnCwl2QZ.png)

$nodes : n = 4 \\ edges : m = 5$

e.g. An electrical network.

## Incidence Matrix (关联矩阵)

$A = \begin{bmatrix}  -1 & 1 & 0 & 0 \\  0 & -1 & 1 & 0 \\  -1 & 0 & 1 & 0 \\  -1 & 0 & 0 & 1 \\  0 & 0 & -1 & 1 \end{bmatrix}$

1,2,3 is a loop. (loop means **linear dependent)**

### *A* and *N*(*A*)

$x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix}$, the potential at nodes.

$Ax = \begin{bmatrix}  x_2 - x_1 \\  x_3 - x_2 \\  x_3 - x_1 \\  x_4 - x_1 \\  x_4 - x_3 \end{bmatrix}$ , the potential differences.

$Ax = 0 \Rightarrow x = c\begin{bmatrix}  1 \\ 1 \\ 1 \\ 1 \end{bmatrix}$

$rank(A)=n-1$ (ground one node to settle all other nodes, $rank(A)+rank(N(A))=n$).

### $A^T$ and $N(A^T)$

$A^Ty=0\\dim (N(A^T))=m − r = 5 − 3 = 2$

$A^T y= \begin{bmatrix}  -1 & 0 & -1 & -1 & 0 \\  -1 & -1 & 0 & 0 & 0 \\  0 & 1 & 1 & 0 & -1 \\  0 & 0 & 0 & 1 & 1 \end{bmatrix} \begin{bmatrix}  y_1 \\  y_2 \\  y_3 \\  y_4 \\  y_5 \end{bmatrix} = \begin{bmatrix}  0 \\ 0 \\ 0 \\ 0 \end{bmatrix}$

![https://s2.loli.net/2022/03/03/sHoz8QTmVdUX2x5.png](https://s2.loli.net/2022/03/03/sHoz8QTmVdUX2x5.png)

Implies KCL, with y being current :

first row :

$\begin{bmatrix}  -1 & 0 & -1 & -1 & 0 \end{bmatrix} \begin{bmatrix}  y_1 \\  y_2 \\  y_3 \\  y_4 \\  y_5 \end{bmatrix} = \begin{bmatrix}  0 \end{bmatrix}$

$\iff − y1 − y3 − y4 = 0$

Basis for $N(A^T)$ : $\begin{bmatrix}  1\\1\\-1\\0\\0 \end{bmatrix},\begin{bmatrix}  0\\0\\1\\-1\\1 \end{bmatrix}$

pivot columns of $A^T$ ($r$ independent edges) is a **tree** (a graph with no loops).

$$
\begin{aligned}
    \dim N(A^T) &= m-r \\
    \#loops &= \#edges - (\#nodes-1) \\
\end{aligned}
$$

Euler’s Law:

$$
\#nodes − \#edges + \#loops = 1
$$

### Summarize

$$
e=Ax\\
y = Ce\\
A^T=0 \\
\Rightarrow A^TCAx = f
$$

$e$: potential difference

$c$: constant

$f$: current source (0 if no source)

note: $A^TCA$ is symmetric.