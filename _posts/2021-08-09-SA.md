---
title: 后缀数组简述
math: true
tag: SA
---
[模板题](https://www.luogu.com.cn/problem/P3809)

```cpp
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
using namespace std;
const int N = 1000011;

int n, sa[N], rk[N], cnt[N], id[N], oldrk[N];
char a[N];

void getSA() {
    memset(cnt, 0, sizeof cnt);
    int m = max(n, 256);
    rep(i, 1, n) cnt[rk[i] = a[i]]++;
    rep(i, 1, m) cnt[i] += cnt[i - 1];
    rep(i, 1, n) sa[cnt[rk[i]]--] = i;
    for (int w = 1; w < n; w *= 2) {
        int pos = 0;
        rep(i, n - w + 1, n) id[++pos] = i;
        rep(i, 1, n) if (sa[i] > w) id[++pos] = sa[i] - w;
        memset(cnt, 0, sizeof cnt);
        rep(i, 1, n) cnt[rk[id[i]]]++;
        rep(i, 1, m) cnt[i] += cnt[i - 1];
        per(i, n, 1) sa[cnt[rk[id[i]]]--] = id[i];
        memcpy(oldrk, rk, sizeof rk);
        pos = 0;
        rep(i, 1, n) rk[sa[i]] =
            oldrk[sa[i]] == oldrk[sa[i - 1]] &&
                    oldrk[sa[i] + w] == oldrk[sa[i - 1] + w]
                ? pos
                : ++pos;
    }
}

int main() {
    scanf("%s", a + 1);
    n = strlen(a + 1);
    getSA();
    rep(i, 1, n) printf("%d ", sa[i]);
    return 0;
}
```
