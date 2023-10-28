---
title: gprof性能分析和可视化
---

# 生成分析信息

g++添加 `-pg` 参数，如此编译后运行程序，就会输出性能分析文件 `gmon.out` 。

# gprof

无论是Linux还是MinGW，一般自带gprof，MinGW里就是和g++同一个目录里。

使用：

```bash
gprof prog.exe gmon.out > analysis.txt
```
or
```bash
gprof prog.exe > analysis.txt
```

`prog.exe` 就是可执行文件名。

[这](https://paste.ubuntu.com/p/3S6T7xF2F3/)是一个 `analysis.txt` 的例子。可以看到有运行时间、时间占比等。

# gprof2dot
这是一个python包，用来把gprof的输出信息变成dot图

```bash
pip install gprof2dot
```
同时要安装dot并添加到`PATH`

使用：

```bash
gprof prog.exe | gprof2dot | dot -Tpng -o profile.png
```

![poly2.png](https://i.loli.net/2021/11/27/wivClo4OursnYLD.png)

一个函数的百分比表示运行用时占比，括号里的表示实际用时占比（去除所有显示的子函数后）