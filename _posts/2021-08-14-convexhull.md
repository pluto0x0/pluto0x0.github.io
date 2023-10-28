---
title: 模板：凸包周长
math: true
taggs:
- 计算几何
- 模板
- 凸包
categories: 计算几何
---

<https://www.luogu.com.cn/record/55936318>

使用单调栈，$$O(n \, \log n)$$

```cpp
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
#define D(x) cout << #x << " : " << x << endl
using namespace std;
typedef double db;
const int N = 1e5 + 11;

struct point {
    db x, y;
    point() { x = y = 0.0; }
    point(db p, db q) { x = p, y = q; }
    friend bool operator<(point a, point b) {
        if (b.x == a.x) return b.y < a.y;
        return b.x < a.x;
    }
    friend point operator-(point a, point b) {
        return point(a.x - b.x, a.y - b.y);
    }
    friend db operator*(point a, point b) { return a.x * b.y - a.y * b.x; }
} a[N];

db dis(point p, point q) {
    return sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y));
}

int n, stk[N * 2], tp;
bool used[N];

int main() {
    cin.tie(0);
    cin.sync_with_stdio(false);

    cin >> n;
    rep(i, 1, n) cin >> a[i].x >> a[i].y;
    sort(a + 1, a + 1 + n);

    memset(used, 0, sizeof used);
    stk[tp = 1] = 1;
    rep(i, 2, n) {
        while (tp >= 2 &&
               (a[stk[tp]] - a[stk[tp - 1]]) * (a[i] - a[stk[tp]]) < 0)
            used[stk[tp--]] = 0;
        used[i] = true;
        stk[++tp] = i;
    }
    int tp0 = tp;
    per(i, n - 1, 1) {
        if (!used[i]) {
            while (tp > tp0 &&
                   (a[stk[tp]] - a[stk[tp - 1]]) * (a[i] - a[stk[tp]]) < 0)
                used[stk[tp--]] = 0;
            used[i] = true;
            stk[++tp] = i;
        }
    }

    db ans = 0;
    rep(i, 1, tp - 1) ans += dis(a[stk[i]], a[stk[i + 1]]);
    printf("%.2lf\n", ans);
    return 0;
}
```
