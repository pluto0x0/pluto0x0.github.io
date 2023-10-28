---
title: 快速数论变换（NTT）
tags: [多项式, NTT]
categories: 数学
toc:  true
math: true
---

## 前置知识

[FFT](/数学/2021/09/07/fft/)

## 问题引入

FFT用的是浮点运算，并且用到了 $\sin \; \cos$ 函数，运算效率比较低并且精度不足。

而NTT用的是数论变换，都是整数运算。

## 原根

<https://oi-wiki.org/math/number-theory/primitive-root/>

<https://zhuanlan.zhihu.com/p/166043237>

## NTT

模数 $p = 998244353 = 7\times 17 \times 2^{23}$ 的原根 $g=3$ ，将 $g_n=g^{\frac{p-1}{n}}$ 看作是FFT中的 $\omega_n$ ，它们具有相同的性质：

$$\begin{aligned}
g_n^n &\equiv 1 \mod p \\
\omega_n^n &= 1
\end{aligned}$$

$$\begin{aligned}
g_n^{n/2} &\equiv -1 \mod p \\
\omega_n^{n / 2} &= -1
\end{aligned}$$

## 示例代码

模板：[高精度乘法](https://www.luogu.com.cn/problem/P1919)

```cpp
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
#define D(x) cout << #x << " : " << x << endl
using namespace std;
typedef long long ll;
const int N = 1 << 21;
const int mod = 998244353;

int rev[N];

int qpow(int x, int y) {
    int ret = 1;
    while (y) {
        if (y & 1) ret = (ll)ret * x % mod;
        x = (ll)x * x % mod;
        y >>= 1;
    }
    return ret;
}

void change(int y[], int n) {
    rep(i, 0, n - 1) {
        rev[i] = rev[i >> 1] >> 1;
        if (i & 1) rev[i] |= n >> 1;
    }
    rep(i, 0, n - 1) if (i < rev[i]) swap(y[i], y[rev[i]]);
}

void ntt(int y[], int n, int op) {
    change(y, n);
    for (int h = 2; h <= n; h *= 2) {
        int gn = qpow(3, (mod - 1) / h);
        for (int j = 0; j < n; j += h) {
            int g = 1;
            rep(k, j, j + h / 2 - 1) {
                int u = y[k], t = (ll)g * y[k + h / 2] % mod;
                y[k] = (u + t) % mod, y[k + h / 2] = (u - t + mod) % mod;
                g = (ll)g * gn % mod;
            }
        }
    }
    if (op == -1) {
        reverse(y + 1, y + n);      //begin with y+1 !
        int inv = qpow(n, mod - 2);
        rep(i, 0, n - 1) y[i] = (ll)y[i] * inv % mod;
    }
}

char a[N], b[N];
int x[N], y[N];
int ans[N];

int main() {
    scanf("%s %s", a, b);
    int l1 = strlen(a), l2 = strlen(b), n = 1;
    while (n < l1 + l2) n *= 2;
    rep(i, 0, l1 - 1) x[i] = a[l1 - 1 - i] - '0';
    rep(i, l1, n - 1) x[i] = 0;
    rep(i, 0, l2 - 1) y[i] = b[l2 - 1 - i] - '0';
    rep(i, l2, n - 1) y[i] = 0;
    ntt(x, n, 1), ntt(y, n, 1);
    rep(i, 0, n - 1) x[i] = 1ll * x[i] * y[i] % mod;
    ntt(x, n, -1);
    rep(i, 0, n - 1) ans[i] = x[i];
    rep(i, 0, n - 1) ans[i + 1] += ans[i] / 10, ans[i] %= 10;
    while (ans[n - 1] == 0 && n > 1) n--;
    per(i, n - 1, 0) putchar(ans[i] + '0');
    return 0;
}
```

对于 $\texttt{op == -1}$ 的情况，这里采用了[方法二](https://oi-wiki.org/math/poly/fft/#_14)

