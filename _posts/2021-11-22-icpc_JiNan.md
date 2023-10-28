---
title: icpc 济南区域赛
math: true
---

## Optimal Strategy

>有 n 件物品，第 i 件的价值为 a[i]。A 和 B 轮流取物品，A 先手。每个玩家都要最大化自己取到的物品的价值和，求有多少种可能的游戏过程。
>
>1 <= n <= 1 000 000
>
>1 <= a[i] <= n

>考虑最大值如果是偶数个，那么会每次被两个两个的取；如果是奇数个，那么会被先手立刻取走一个，变成偶数的情况。
>
>故容易得到答案为（c[i] 是价值为 i 的物品个数）

$$ \prod_{i=1}^{n}c_i!\binom{\sum_{j=1}^{i-1}c_j+\lfloor c_i/2\rfloor}{\lfloor c_i/2\rfloor} $$

价值最大的物品，一定两个两个地取。现在考虑出现了有一个更大价值的若干物品，那么这些价值更大的物品一定能成对地插入原来取物品产生的序列中的任意位置。

于是上式就是这一过程的模拟。

##

> 给定 $n$ 和次数不超过 $n$ 的整系数多项式 $f(x)$，计算 $\sum ^{\infty }_{i=0}\dfrac {f\left( i\right) }{i!}$ 。可以证明答案是 $e$ 的整数倍，只需输出这个倍数对 $P$ 取模的结果即可。
> 
> 数据范围：$1 \le n \le 100000,\; P = 998244353$

> 我们设 $a_n$ 表示 $f(x) = x^n$ 的答案，考虑计算这个数列的指数生成函数：
> $$g\left( x\right) =\sum _{n\geq 0}\dfrac {x^{n}}{n!}\sum _{i\geq 0}\dfrac {i^{n}}{i!}=\sum _{i\geq 0}\dfrac {1}{i!}\sum _{n\geq 0}\dfrac {\left( ix\right) ^{n}}{n!}=\sum _{i\geq 0}\dfrac {e^{ix}}{i!}=e^{e^{x}}=e^{e^{x}-1}e$$
>于是使用一次多项式 $\exp$ 即可算出答案，时间复杂度 $O(n \log n)$。值得一提，$a_n$ 恰好是 Bell 数，这也就证明了答案是 $e$ 的整数倍。

因为多项式 $\exp$ 要求常数项为0，因此必须将一个 $e$ 提出来。

结合指数生成函数 $\exp$ [的意义](https://oi-wiki.org/math/gen-func/egf/#_3)，不难发现 $a_n$ 即为就是 大小为 $n$ 的集合的分割数，即[Bell数](https://oeis.org/A000110)。 

以下是求 $a_n$ （Bell数）的代码（$n=100$）,配合[多项式模板](/?2021-11-27-%E5%A4%9A%E9%A1%B9%E5%BC%8F%E6%A8%A1%E6%9D%BF.md)使用。

```cpp
using namespace Poly;

int n, m;
poly x(100, 1), y;
int frac[101];
int ifrac[101];

void init() {
    int n = 100;
    frac[0] = 1;
    rep(i, 1, n) frac[i] = ll(frac[i - 1]) * i % mod;
    ifrac[n] = inv(frac[n]);
    per(i, n - 1, 0) ifrac[i] = ll(ifrac[i + 1]) * (i + 1) % mod;
}

int main() {
    init();
    int n = 100;
    Rep(i, 0, n) x[i] = ifrac[i];
    x = exp(x - 1);
    Rep(i, 0, n) x[i] = ll(x[i]) * frac[i] % mod;
    print(x);
    return 0;
}
```