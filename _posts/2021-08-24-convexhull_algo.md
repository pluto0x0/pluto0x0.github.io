---
title: 一些凸包有关的算法
tags: [凸包]
categories: 计算几何 
toc:  true
math: true
---

## 判断点在凸包内

主要介绍二分法[^l1]

### 二分法

如图，
![n=8](https://i.loli.net/2021/08/23/uVdPtR12HTpyUMg.png)

可以通过向量叉积得到任意 $$\overrightarrow{V_0V_i}$$ 和 $$\overrightarrow{V_0P}$$ 的左右关系。

先通过 $$\overrightarrow{V_0V_1}$$ 和 $$\overrightarrow{V_0V_{n-1}}$$ 排除 $$P$$ 在灰色区域的情况。

显然通过二分，就能找到 $$\overrightarrow{V_0V_i}$$ 使得 $$\overrightarrow{V_0P}$$ 在 $$\overrightarrow{V_0V_i}$$ 和 $$\overrightarrow{V_0V_{i+1}}$$ 之间

接下来只需要判断 $$\overrightarrow{V_iP}$$ 是否在 $$\overrightarrow{V_iV_{i+1}}$$ 左侧即可（假定凸包以逆时针方向给出）。

#### Code

```cpp
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
#define D(x) cout << #x << " : " << x << endl
using namespace std;
const int N = 1001;

struct point {
    int x, y;
    point() { x = y = 0; }
    point(int p, int q) { x = p, y = q; }
    friend point operator-(point p, point q) { return point(p.x - q.x, p.y - q.y); }
    friend int operator*(point p, point q) { return p.x * q.y - p.y * q.x; } // cross product
} v[N];
int n;

bool check(point p) {
    if ((v[1] - v[0]) * (p - v[0]) < 0) return false;
    if ((v[n - 1] - v[0]) * (p - v[0]) > 0) return false;

    int l = 1, r = n - 1, mid;
    while (l <= r) {
        mid = (l + r) / 2;
        if ((v[mid] - v[0]) * (p - v[0]) > 0)
            l = mid + 1;
        else
            r = mid - 1;
    }
    return (v[l] - v[r]) * (p - v[r]) > 0;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> n;
    rep(i, 0, n - 1) cin >> v[i].x >> v[i].y;
    for (;;) {
        point q;
        cin >> q.x >> q.y;
        cout << (check(q) ? "In" : "Out") << endl;
    }
    return 0;
}
```

### 其他方法

判断内角和 $$360$$ ，射线相交……


## 凸包极值点

即一个凸包在某一个向量 $$\vec{u}$$ 方向上投影的极值点。[^l2]

![image.png](https://i.loli.net/2021/08/23/4ZsQFa9pOLhABRM.png)

对于任意向量 $$\vec{v}$$ ，可以通过 $$\vec{v} \cdot \vec{u}$$ 的正负性判断 $$\vec{v}$$ 在 $$\vec{u}$$ 投影的方向。


### 二分法

分类讨论：

![image.png](https://i.loli.net/2021/08/23/49sEFQtW178B2Nw.png)


### Code

```cpp
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
#define D(x) cout << #x << " : " << x << endl
using namespace std;
const int N = 1001;

struct point {
    int x, y;
    point() { x = y = 0; }
    point(int p, int q) { x = p, y = q; }
    friend point operator-(point p, point q) { return point(p.x - q.x, p.y - q.y); }
    friend int operator*(point p, point q) { return p.x * q.x + p.y * q.y; }  // dot product
} v[N], u;
int n;

inline bool up(int i, int j) { return (v[j] - v[i]) * u > 0; }  // check vector i -> j
inline bool up(int i) { return up(i, i == n - 1 ? 0 : i + 1); }

int find_max() {
    if (!up(0) && up(n - 1)) return 0;

    int l = 0, r = n, mid;
    while (l < r) {
        mid = (l + r) / 2;
        if (!up(mid) && up(mid - 1)) return mid;
        if (up(l)) {
            if (!up(mid))
                r = mid;
            else {
                if (up(l, mid))
                    l = mid;
                else
                    r = mid;
            }
        }

        else {
            if (up(mid))
                l = mid;
            else {
                if (!up(l, mid))
                    l = mid;
                else
                    r = mid;
            }
        }
    }
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> n;
    rep(i, 0, n - 1) cin >> v[i].x >> v[i].y;
    cin >> u.x >> u.y;

    cout << find_max() << endl;
    return 0;
}
```

注意 $$r$$ 初值为 $$n$$ 。

## 点到凸包的切线

容易发现，点到凸包的切线实际上就是凸包上各个点到某个点极角的极值，只要能得到两个点 $$V_i$$ 和 $$V_j$$ 关于点 $$P$$ 的“上下关系”，那么就可以套用**凸包极值点**的二分策略。

显然只要用 $$\overrightarrow{PV_i}\times \overrightarrow{PV_j}$$ 的正负性判断就行了。

### Code

在**凸包极值点**代码的基础上修改：

改成叉积：

```cpp
friend int operator*(point p, point q) { return p.x * q.y - p.y * q.x; }  // cross product
```

改变判定方式：

```cpp
inline bool up(int i, int j) { return (v[j] - u) * (v[i] - u) > 0; }  // check vector i -> j
```


[^l1]: <https://www.cnblogs.com/lxglbk/archive/2012/08/17/2644805.html>

[^l2]: <https://blog.csdn.net/u013279723/article/details/104458627>
