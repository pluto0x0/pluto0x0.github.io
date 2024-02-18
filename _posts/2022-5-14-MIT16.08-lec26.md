---
title: MIT18.06 Linear Algebra (26)
categories:
- Course Notes
- Linear Algebra
tags: Linear Algebra
date: 2022-5-14
img_path: /upload/
math: true
---

# lec26

# Eigenvector of symmetric matrices

- A symmetric matrix has **only real eigenvalues**
- The eigenvectors can be **chosen orthonormal**
- proof
    
    [Orthogonality of Eigenvectors of a Symmetric Matrix Corresponding to Distinct Eigenvalues](https://yutsumura.com/orthogonality-of-eigenvectors-of-a-symmetric-matrix-corresponding-to-distinct-eigenvalues/)
    

$$
\begin{aligned}Au & = \lambda u\\Av & = \omega v\end{aligned}
$$

$$
\omega v^\top = v^\top A^\top = v^\top A \\
\omega v^\top u = v^\top Au=\lambda v^\top u \\
(\omega -\lambda )v^\top u = 0 \\
v^\top u = 0

$$

We can choose orthonormal eigenvectors. Therefor, for $S=S^\top$:

$$
S=Q \Lambda Q^{-1}=Q \Lambda Q^\top
$$

$$
S^\top=Q \Lambda^\top Q^\top=Q\Lambda Q^\top=S
$$

Why **real** eigenvalues?

$$
Ax=\lambda x\Longrightarrow A\bar{x}=\bar{\lambda }\bar{x}\Longrightarrow\bar{x}^{\top} A^{\top}=\bar{x}^{\top} \bar{\lambda}
$$

$$
Ax=\lambda x \Longrightarrow \bar{x}^\top Ax=\lambda \bar{x}^{\top}x \\
\bar{x}^\top A^{\top}=\bar{x}^{\top} \bar{\lambda} \Longrightarrow\bar{x}^{\top}A x=\bar{\lambda}\bar{x}^{\top}x
$$

$$
⁍
$$

$\lambda$ is real.

## break down $A=Q\Lambda Q^\top$

$$
A = 
\begin{bmatrix}
 \vdots & \vdots & \\
 q_1 & q_1 & \cdots\\
 \vdots & \vdots &
\end{bmatrix}
\begin{bmatrix}
 \lambda_1 &  & \\
  & \lambda_2 & \\
  &  & \ddots
\end{bmatrix}
\begin{bmatrix}
 \cdots & q_1^\top & \cdots \\
 \cdots & q_2^\top & \cdots \\
  & \vdots &
\end{bmatrix}=\lambda_{1} q_{1} q_{1}^{\top}+\lambda_{2} q_{2} q_{2}^{\top}+\cdots
$$

$q$ is a unit vector, so $q^\top q=1, qq^\top=\frac{qq^\top}{q^\top q}$, which is projection matrix.

every symmetricmatrix is a combination of mutually perpendicular projedtion matrices. **(spectral theorem)**

for symmetric matrices, the sign of pivots is the same as the sign of eigenvalues.

# Intro to Positive definite symmetric matrix

- all eigenvalues are positive
- all pivots are positive

all subdeterminate are positive.