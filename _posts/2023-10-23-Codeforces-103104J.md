---
title: "Codefoeces 103104J: Similar Triangles"
math: true
categories: Codeforces
---
https://codeforces.com/gym/103104/problem/J

## 大意

输入三个点表示一个三角形，输出最小的与这个三角形的相似的三角形。
共 $T\le 10^4$ 组数据， $|x|,|y|\le 10^9$ .

## 方法

原三角形的点记为$(x_i', y_i')$将一个点平移至 $(0,0)$，与之相似的三角形的两点$(x_i, y_i)$可以用一个线性变换表示：

$$
M = \begin{pmatrix}
 a & -b\\
 b & a
\end{pmatrix} \quad a,b \in \mathbb{Z}
$$

$$
M
\begin{pmatrix}
x_i \\
y_i
\end{pmatrix} = 
\begin{pmatrix}
x_i' \\
y_i'
\end{pmatrix}
$$

表示把原有的基底 $(1,0)$， $(0,1)$ 映射成 $(a,b)$， $(-b,a)$ 。

并且

$$
\left|\begin{pmatrix}
x_i' \\
y_i'
\end{pmatrix}\right|^2
=
(a^2+b^2)
\left|\begin{pmatrix}
x_i \\
y_i
\end{pmatrix}\right|^2
$$


因此计算三边长平方的gcd，记为$g$，如果存在$a^2+b^2=g$，
相应的有

$$
M^{-1} = \begin{pmatrix}
 a & b\\
 -b & a
\end{pmatrix}
\frac{1}{a^2+b^2} 
$$

$$
\begin{pmatrix}
x_i \\
y_i
\end{pmatrix} = 
M^{-1} \begin{pmatrix}
x_i' \\
y_i'
\end{pmatrix}
$$

以此得到相似三角形的点$(x_i, y_i)$，否则无解。

*这里忽略了$a^2+b^2=g$无解的情况，事实证明不影响答案正确性。*

## 代码

```cpp
#include <cmath>
#include <iostream>
using namespace std;
typedef long long ll;

ll xa, ya, xb, yb, xc, yc;

ll gcd(ll x, ll y) {
    if (!y) return x;
    return gcd(y, x % y);
}

void test_l(ll l) {
    for (ll a = 1; a * a < l; a++) {
        ll b_ = ll(sqrt(l - a * a));
        if (a * a + b_ * b_ == l) {
            for (ll b = -b_; b != b_; b = b_) {
                ll Xb = a * xb + b * yb, Yb = -b * xb + a * yb;
                ll Xc = a * xc + b * yc, Yc = -b * xc + a * yc;
                if (Xb % l == 0 && Yb % l == 0 && Xc % l == 0 && Yc % l == 0) {
                    printf("0 0 %lld %lld %lld %lld\n", Xb / l, Yb / l, Xc / l, Yc / l);
                    return;
                }
            }
        }
    }
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        cin >> xa >> ya >> xb >> yb >> xc >> yc;
        xb -= xa, xc -= xa;
        yb -= ya, yc -= ya;
        ll lb = xb * xb + yb * yb, lc = xc * xc + yc * yc,
           la = (xb - xc) * (xb - xc) + (yb - yc) * (yb - yc);
        ll lgcd = gcd(gcd(lb, lc), la);
        test_l(lgcd);
    }
    return 0;
}
```
