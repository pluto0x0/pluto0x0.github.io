---
title: 树状数组进阶应用
tags: [树状数组]
categories: 数据结构
toc:  true
math: true
---

## 单点修改，区间查询

普通树状数组即可，略。

## 区间修改，单点查询

树状数组维护差分数组即可。

## 区间修改，区间查询

还是考虑维护差分数组。

易知：
 $$a_i=\sum\limits_{j=1}^i b_j$$ 

那么 $$a$$ 的前缀和：

$$
\begin{aligned}
s_i &= \sum\limits_{j=1}^i a_j \\
&=\sum\limits_{j=1}^i \sum\limits_{k=1}^j b_k \\
&=\sum\limits_{j=1}^i (i-j+1)b_j \\
&=(i+1)\sum\limits_{j=1}^i b_j - \sum\limits_{j=1}^i j\times b_j
\end{aligned}
$$

分别维护 $$b_i$$ 的前缀和和 $$(b_i \times i)$$ 的前缀和。

[模板](https://loj.ac/p/132)

```cpp
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
#define D(x) cout << #x << " : " << x << endl
using namespace std;
typedef long long ll;
const int N = 1e6 + 5;

int n, q;
ll t1[N], t2[N];

void add(int pos, ll val) {
    ll val2 = val * (ll)pos;
    for (; pos <= n; pos += (pos & -pos))
        t1[pos] += val, t2[pos] += val2;
}

void add(int l, int r, ll val) { add(l, val), add(r + 1, -val); }

ll sum(ll *ptr, int pos) {
    ll ans = 0;
    for (; pos; pos -= (pos & -pos)) ans += ptr[pos];
    return ans;
}

ll sum(int pos) { return (pos + 1) * sum(t1, pos) - sum(t2, pos); }

ll sum(int l, int r) { return sum(r) - sum(l - 1); }

template <typename T>
void read(T &x) {
    x = 0;
    char ch = getchar();
    T f = 1;
    for (; !isdigit(ch); ch = getchar())
        if (ch == '-') f = -1;
    for (; isdigit(ch); ch = getchar()) x = x * 10 + ch - '0';
    x *= f;
}

int main() {
    memset(t1, 0, sizeof t1);
    memset(t2, 0, sizeof t2);

    read(n), read(q);
    rep(i, 1, n) {
        ll tmp;
        read(tmp);
        add(i, i, tmp);
    }
    while (q--) {
        int op, l, r;
        read(op), read(l), read(r);
        if (op == 1) {
            ll x;
            read(x);
            add(l, r, x);
        } else {
            cout << sum(l, r) << endl;
        }
    }

    return 0;
}
```

## 二维树状数组：单点修改，区间查询

从一维的树状数组类推。

 $$s_{a,b} = \sum\limits_{i=a - \operatorname{lowbit}(a)+1}^{a} \; \sum\limits_{j=b-\operatorname{lowbit}(b)+1}^b a_{i,j}$$ 

[模板](https://loj.ac/p/133)

```cpp
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
#define D(x) cout << #x << " : " << x << endl
using namespace std;
typedef long long ll;
const int N = (1 << 12) + 5;

int n, m;
ll s[N][N];

void add(int x, int y, int val) {
    for (int i = x; i <= n; i += (i & -i))
        for (int j = y; j <= m; j += (j & -j)) s[i][j] += (ll)val;
}

ll sum(int x, int y) {
    ll ret = 0;
    for (int i = x; i; i -= (i & -i))
        for (int j = y; j; j -= (j & -j)) ret += s[i][j];
    return ret;
}

ll sum(int x, int y, int X, int Y) {
    return sum(X, Y) - sum(X, y - 1) - sum(x - 1, Y) +
           sum(x - 1, y - 1);
}

int main() {
    memset(s, 0, sizeof s);
    cin >> n >> m;
    int op, a, b, c, d;
    while (scanf("%d %d %d %d", &op, &a, &b, &c) == 4) {
        if (op == 1)
            add(a, b, c);
        else {
            scanf("%d", &d);
            printf("%lld\n", sum(a, b, c, d));
        }
    }

    return 0;
}
```
注意：修改/查询时**不能**用x/y作为循环变量！

## 二维：区间修改，区间查询

同样考虑维护差分矩阵。

矩阵如何差分？可以将 $$a$$ 看作差分矩阵 $$b$$ 的矩阵前缀和，那么反过来用 $$a$$ 表示 $$b$$ ：

 $$b_{i,j} = a_{i,j} - a_{i-1,j} - a_{i,j - 1} + a_{i-1,j-1}$$ 

但其实这个式子并不重要，我们只需要知道 $$a$$ 是 $$b$$ 的前缀和就行了。即

 $$a_{x,y} = \sum\limits_{i=1}^x \sum\limits_{j=1}^y b_{i,j}$$ 

同样计算 $$b$$ 的贡献：

$$
\begin{aligned}
s_{x,y} &= \sum\limits_{i=1}^x \sum\limits_{j=1}^y a_{i,j} \\
&= \sum\limits_{i=1}^x \sum\limits_{j=1}^y \sum\limits_{k=1}^i \sum\limits_{l=1}^j b_{k,l} \\
&= \sum\limits_{i=1}^x \sum\limits_{j=1}^y b_{i,j} \times (x-i+1)(y-j+1)\\
&= \sum\limits_{i=1}^x \sum\limits_{j=1}^y b_{i,j} \times \left[(x+1)(y+1)-(y+1)i - (x+1)j + ij\right ]\\
\end{aligned}
$$

于是分别维护 $$b_{i,j}$$ 、 $$(b_{i,j}\times i)$$ 、 $$(b_{i,j}\times j)$$ 、 $$(b_{i,j}\times i \times j)$$ 即可。

[模板](https://loj.ac/p/135)

```cpp
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
#define D(x) cout << #x << " : " << x << endl
using namespace std;
typedef long long ll;
const int N = 2048 + 5;

int n, m;
ll t[N][N], tx[N][N], ty[N][N], txy[N][N];

void add(int x, int y, ll val) {
    ll valx = val * (ll)x, valy = val * (ll)y, valxy = val * (ll)x * (ll)y;
    for (int i = x; i <= n; i += (i & -i))
        for (int j = y; j <= m; j += (j & -j)) {
            t[i][j] += val, tx[i][j] += valx;
            ty[i][j] += valy, txy[i][j] += valxy;
        }
}

void add(int x, int y, int X, int Y, ll val) {
    add(x, y, val), add(X + 1, y, -val);
    add(x, Y + 1, -val), add(X + 1, Y + 1, val);
}

ll sum(int x, int y) {
    ll ret = 0;
    for (int i = x; i; i -= (i & -i))
        for (int j = y; j; j -= (j & -j)) {
            ret += (ll)(x + 1) * (ll)(y + 1) * t[i][j];
            ret -= (ll)(y + 1) * tx[i][j];
            ret -= (ll)(x + 1) * ty[i][j];
            ret += txy[i][j];
        }
    return ret;
}

ll sum(int x, int y, int X, int Y) {
    return sum(X, Y) - sum(x - 1, Y) - sum(X, y - 1) +
           sum(x - 1, y - 1);
}

int main() {
    memset(t, 0, sizeof t);
    memset(tx, 0, sizeof tx);
    memset(ty, 0, sizeof ty);
    memset(txy, 0, sizeof txy);

    cin >> n >> m;
    int op, a, b, c, d, x;
    while (scanf("%d %d %d %d %d", &op, &a, &b, &c, &d) == 5) {
        if (op == 1) {
            scanf("%d", &x);
            add(a, b, c, d, (ll)x);
        } else {
            printf("%lld\n", sum(a, b, c, d));
        }
    }

    return 0;
}
```


# update@21-11-25

权值树状数组求第k大

```cpp
int findkth(int k) {
    int ans = 0, cnt = 0;
    for (int i = 20; i >= 0; --i) {
        ans += 1 << i;
        if (ans >= maxa \Vert  cnt + b[ans] >= k)
            ans -= 1 << i;
        else
            cnt += b[ans];
    }
    return ans + 1;
}
```
值域 $(0,maxa]$
