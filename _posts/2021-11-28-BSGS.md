---
title: BSGS以及例题
math: true
---

求解 
$$a^x \equiv b \pmod p$$
考虑分块，令
$$x = A\lceil\sqrt{p}\rceil - B$$
其中 $0 \le B < \lceil\sqrt{p}\rceil$
那么
$$a ^ {A\lceil\sqrt{p}\rceil - B} \equiv b \pmod p$$
也即
$$a ^ {A\lceil\sqrt{p}\rceil} \equiv b\cdot a^B \pmod p$$
其中 $a ^ {\lceil\sqrt{p}\rceil}$ 为常数，枚举 $B$ 将 $b\cdot a^B$ 插入hash map，再枚举 $A$ 查询 $a ^ {A\lceil\sqrt{p}\rceil}$ 即可。

[例题](https://www.luogu.com.cn/problem/P3846)

```cpp
using ll = long long;
int mod, b, a;

int qpow(int x, int y) {
    int r = 1;
    while (y) {
        if (y & 1) r = ll(r) * x % mod;
        x = ll(x) * x % mod;
        y >>= 1;
    }
    return r;
}

unordered_map<int, int> mp;

int BSGS(int a, int b) {
    const int bond = int(sqrt(mod)) + 1, c = qpow(a, bond);
    for (int i = 1, t = ll(b) * a % mod; i <= bond; i++, t = ll(t) * a % mod) mp[t] = i;
    for (int i = 1, t = c % mod; i <= bond; i++, t = ll(t) * c % mod)
        if (mp.count(t)) return ll(i) * bond - mp[t];
    return -1;
}

signed main() {
    cin >> mod >> a >> b;
    int r = BSGS(a, b);
    if (r == -1) return cout << "no solution" << endl, 0;
    cout << r << endl;
    return 0;
}
```

值得一提的是，BSGS求出的x是最小的解。

# 二次/n次剩余

考虑
$$x ^ a \equiv b \pmod p$$
设 $g$ 为 $p$ 的原根，则 $\exist c : g ^ c \equiv x \pmod p$

于是问题可以写为
$$g^{ac} \equiv b \pmod p$$
其中 $g^a$ 为常数，用BSGS求解 $c$ 即可,复杂度 $O(\sqrt{p})$。

## 求所有解

> 在知道 $x_0\equiv g^{c}\pmod p$ 的情况下，我们想得到原问题的所有解。首先我们知道 $g^{\varphi(p)}\equiv 1\pmod p$，于是可以得到
>
>$$ \forall\ t \in \mathbb{Z},\ x^a \equiv g^{ c \cdot a + t\cdot\varphi(p)}\equiv b \pmod p $$
>
>于是得到所有解为
>
>$$ \forall\ t\in \mathbb{Z},a\mid t\cdot\varphi(p),\ x\equiv g^{c+\frac{t\cdot\varphi(p)}{a}}\pmod p $$
>
>对于上面这个式子，显然有 $\frac{a}{\gcd(a,\varphi(p))} \mid t$。因此我们设 $t=\frac{a}{\gcd(a,\varphi(p))}\cdot i$，得到
>
>$$ \forall \ i\in \mathbb{Z},x\equiv g^{c+\frac{\varphi(p)}{\gcd(a,\varphi(p))}\cdot i}\pmod p $$
>
>这就是原问题的所有解。

# Reference
<https://oi-wiki.org/math/number-theory/bsgs/>


