---
title: "Codeforces 1553F: Pairwise Modulo"
math: true
categories: Codeforces
---

https://codeforces.com/problemset/problem/1553/F

## 大意

求

$$
p_k = \sum_{1 \le i, j \le k} a_i \bmod a_j,
$$

其中
$2 \le n \le 2 \cdot 10^5$， $1 \le a_i \le 3 \cdot 10^5$， $a_i \neq a_j$ if $i \ne j$

## 方法

考虑$p$的差分数组$P_i := p_i - p_{i - 1}$则有：

$$
P_m = \sum_{\max(i,j)=m} a_i \bmod a_j
$$

考虑从前到后枚举$a_i$，保证当前枚举的下标是所有枚举过的中最大的。

定义$d_v = \{0,1\}$ 表示是否有值为$v$的数出现过，那么对于当前的下标$i$，

$$
\sum_{j=1}^{i-1} a_i \bmod a_j = \sum_{j=1}^{\max(a_k)} (a_i \bmod j) d_j \\ =
\sum_{j=1}^{\max(a_k)} \left(a_i - j \left\lfloor \frac{a_i}{j} \right\rfloor\right) d_j = 
a_i\sum_{j=1}^{\max(a_k)} d_j - \sum_{j=1}^{\max(a_k)} \left\lfloor \frac{a_i}{j} \right\rfloor(jd_j)
$$

考虑用树状数组维护 $d_j$ 和 $jd_j$ 的前缀和，对 $\left\lfloor \frac{a_i}{j} \right\rfloor$ 进行整除分块，复杂度 $\mathrm{O}(n \sqrt{\max a_k}\log \max a_k)$。


接下来考虑

$$
\sum_{j=1}^{i-1} a_j \bmod a_i = \sum_{j=1}^{\max(a_k)} (j \bmod a_i) d_j =
\sum_{j=1}^{\max(a_k)} \left(j - a_i \left\lfloor \frac{j}{a_i} \right\rfloor\right) d_j
$$

此时 $ \left\lfloor \frac{j}{a_i} \right\rfloor$ 块的长度固定为 $a_i$

复杂度 $\mathrm{O}(\sum_i \frac{1}{a_i} \max a_k \log \max a_k) = \mathrm{O}(\max a_k \log n \log \max a_k)$

### 常数优化

开启O2下本地最大数据用时在1.5秒左右，不开启O2，在6.5秒左右。

考虑对于小区间直接循环求和而不使用树状数组，可以节省求和的开销。

优化后开启O2下本地最大数据用时在1.0秒左右，不开启O2，在2.5秒左右。


## 代码

```cpp
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 2e5;
const int MAXA = 3e5;
typedef long long ll;

int n, a[N + 1], maxa = 0;
ll s[MAXA + 1], s2[MAXA + 1];
int ss[MAXA + 1], ss2[MAXA + 1];
ll p[N + 1];

void add(ll arr[], int x, ll v) {
    for(; x <= maxa; x += x & (-x))
        arr[x] += v;
}

ll sum(ll arr[], int x) {
    if(x <= 0) return 0;
    ll ret = 0;
    for(; x ; x -= x & (-x))
        ret += arr[x];
    return ret;
}

#define S(arr, l, r) (sum(arr, r) - sum(arr, (l) - 1))

int main() {
    ios::sync_with_stdio(false);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        if (maxa < a[i]) maxa = a[i];
    }
    memset(s, 0, sizeof(s));
    memset(s2, 0, sizeof(s2));
    memset(ss, 0, sizeof(ss));
    memset(ss2, 0, sizeof(ss2));
    for (int i = 1; i <= n; i++) {
        p[i] += sum(s, maxa) * a[i];
        for(int v = a[i], l = 1, r = 1; v; l = r + 1, v = a[i] / l) {
            r = a[i] / v;
            if (r - l < 24) {
                int SS = 0, SS2 = 0;
                for(int j = l; j <= r; j++) SS += ss[j], SS2 += ss2[j];
                p[i] -= ll(SS2) * v;
            }
            else
                p[i] -= S(s2, l, r) * v;
        }
        p[i] += sum(s2, maxa);
        for(int l = 0, r = a[i] - 1; l <= maxa; l = r + 1, r = min(l + a[i] - 1, maxa))
            p[i] -= S(s, l, r) * l;
        add(s, a[i], 1), add(s2, a[i], a[i]);
        ss[a[i]]++, ss2[a[i]] += a[i];
    }
    for (int i = 1; i <= n; i++) cout << (p[i] += p[i - 1]) << " ";
    return 0;
}
```
