---
math: true
title: C++lambda表达式的简单应用

---

<https://www.cnblogs.com/DswCnblog/p/5629165.html>

```cpp
// 规定返回值类型
sort(a + 1, a + 1 + n, [](int x, int y) -> bool { return x > y; });
// 自动推断返回值类型
sort(a + 1, a + 1 + n, [](int x, int y) { return x > y; });
```


## 类型

`std::function` 是lambda表达式的类型。

例如，`std::funtion<int(int,int)>` 就是一个接受两个`int`类型参数，返回值为`int`的函数。

当然，定义lambda对象时候，可以直接使用`auto`：
```cpp
auto add = [](int a, int b) {
    return a + b;
};
```

## 捕获外部参数的不同方法

### 值捕获
```cpp
auto f = [a] { cout << a << endl; }; 
```
### 引用捕获
```cpp
auto f = [&a] { cout << a << endl; }; 
```
### 隐式捕获
隐式值捕获
```cpp
auto f = [=] { cout << a << endl; }; 
```
隐式引用捕获
```cpp
auto f = [&] { cout << a << endl; }; 
```

## Reference
<https://www.cnblogs.com/DswCnblog/p/5629165.html>
