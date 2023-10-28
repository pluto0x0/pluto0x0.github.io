---
title: 一些题目
math: true
tags: [构造, 数学]
categories: solution
---

记录最近的一些题目

## CF 1600E

得到一个性质：只有从头开始的连续上升子串才能被取（因为要求每次取的数是严格递增的），结尾也是一样。

于是只需要考虑前 $$p$$ 个和后 $$q$$ 个数。

- 当 $$p$$ $$q$$ 都是偶数时，显然后手必胜（每次都取先手取的数的后一个数）
- 当 $$p$$ $$q$$ 有一个奇数时，显然先手必胜（第一步取奇数侧，变成必败态）
- 当 $$p$$ $$q$$ 都为奇数时，先手必胜（取第一项大的那一侧，该侧为必败，另一侧无法取） 



```cpp
int main()
{
    // read input
    cin >> N;
    vi a(N);
    FOR(i, 0, N){
        cin >> a[i];
    }
    
    
    // find max left increasing sequence
    int p1 = 1;
    for(; p1 < N; p1++){
        if(a[p1-1] >= a[p1])
            break;
    }
 
    // find max right increasing sequece
    int p2 = 1;
    for(int pi = N - 2; pi >= 0; p2++, pi--){
        if(a[pi+1] >= a[pi])
            break;
    }
    
    // find who win
    cout << ((p1 % 2 || p2 % 2)  ? "Alice" : "Bob");
    // print result
 
}
```



## CF1594E2

首先，如果一棵大小为 $$n$$ 树内没有限制且根的父亲已经确定，那么这棵树的染色方案数就是 $$4^n$$ 。

再来考虑暴力dp，大约是 $O(2^k\times 6^2)$ ，主要瓶颈是大量没有限制的点。

考虑将每个有限制的点到根的路径上的点全部标记，再这个连通块内dp，再乘上 $$4^\text{剩下点数}$$ 就是答案。

[code](https://codeforces.com/contest/1594/submission/131288287)

## CF 1599A

巧妙的构造。

将放在天平左边记为 $$+$$ ，右边记为 $$-$$ 。

首先考虑排序，对有序数列一次添上正负。

$$ \texttt{a[] = +1, -2, +3, -4, +5, -6, +7, -8}$$

显然

 $$\vert a_1+a_2\cdots +a_n \vert < \vert a_{n+1} \vert$$ 

因此，再原序列的一个子串的基础上：

- 再子串前端（下标减小方向）添加数，子串和不变号。
- 再子串后端添加数，子串和一定变号。

换句话说，一个子串和的符号只由其中的最后一个值的符号决定。

于是对于需要构造的LR序列，只要再所有天平朝向改变的位置进行变号（向右边取一个），否则不变号（向左取）。

在此之前，先统计两种操作的数量（和一定为 $$n$$），确定初始的空序列在哪个位置。

此外还要确定 $$a_1$$ 的符号，后面才能依次变号。

```cpp
int main(){
	scanf("%d",&n);
	for (int i=0;i<n;i++) scanf("%d",&a[i]);
	sort(a,a+n);
	scanf("%s",ch);
	mi=ma=1;
	ans.push_back(1);
	for (int i=1;i<n;i++){
		if (ch[i]!=ch[i-1]){
			ma++;
			ans.push_back(ma);
		}
		else{
			mi--;
			ans.push_back(mi);
		}
	}
	for (int i=0;i<n;i++){
		printf("%d ",a[ans[i]-mi]);
		if ((ans[i]&1)==(ma&1)){
			printf("%c\n",ch[n-1]);
		}
		else{
			if (ch[n-1]=='L') printf("R\n");
			else printf("L\n");
		}
	}
}
```

# gym 100512

[Andrew Stankevich Contest 42](https://codeforces.com/gym/100512/attachments/download/2773/20122013-summer-petrozavodsk-camp-andrew-stankevich-contest-42-asc-42-en.pdf)

## D

换根lca

就是 $$1\leftrightarrow \texttt{root}$$ 的路径调个头

```cpp
int solve(int x,int y){	//get LCA of x, y
    int fx = lca(x,root), fy = lca(y,root);
    if(fx == fy) return lca(x,y);
    return dep[fx] > dep[fy] ? fx : fy;
}
```

## C

N/A

## B

暴力dp必然超时，考虑每次输的概率更大，最优策略就是每次押尽量多

# gym 100851

[ACM ICPC 2015–2016, Northeastern European Regional Contest](https://codeforces.com/gym/100851/attachments/download/3961/20152016-acmicpc-northeastern-european-regional-contest-neerc-15-en.pdf)

## B

求第 $k$ 大的“十进制表示为二进制表示的后缀”的数。

- 若 $$\overline{1A}$$ 合法，则 $$\overline{A}$$ 也合法，因为 $$10^n$$ 的二进制表示末尾必然也是 $$n$$ 个 $$0$$。

于是只要再所有 $$\le 2^n-1$$ 合法的数加上 $$2^n$$ ，留下合法的结果，就是所有$$\le 2^{n+1}$$ 合法的数。

```python
import math
inf = open('binary.in', 'r')
n = int(inf.readline())
a=[0,1]
b=[0,1]
for i in range(1,170):
    l=len(a)
    for j in range(0,l):
        if (a[j]+10**i-b[j]-2**i) % 2**(i+1)==0:
            a.append(a[j]+10**i)
            b.append(b[j]+2**i)
                     
with open("binary.out", 'w') as f:
    f.write(str(a[n]))
```

## L

二分最高点的高度。

[具体实现](https://codeforces.com/group/cTjYaoMsCo/contest/347707/submission/130946189)比较恶心。

## G

见 [完整题解](/upload/document.pdf)

# HDU某比赛

[2021中国大学生程序设计竞赛（CCPC）- 网络选拔赛（重赛）](https://acm.hdu.edu.cn/contest/problems?cid=1038)

## 1008

分类推式子。

具体见 [完整题解](/upload/2021中国大学生程序设计竞赛（CCPC）- 网络选拔赛（重赛）-题解.pdf)

## 1010

经过尝试，发现二分图需要连成一个环（显然每个点至少两条边，因此一定是最优解，并且一定能连成一个环）

字典序最小，大概就是维护并查集+贪心。

## 1011

想了很久。。

具体见 [完整题解](/upload/2021中国大学生程序设计竞赛（CCPC）- 网络选拔赛（重赛）-题解.pdf)
