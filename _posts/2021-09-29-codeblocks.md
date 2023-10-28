---
title: Code::Blocks 快速上手
tags: ['工具']
categories: 工具
toc:  true
math: true
---

## Overall

codeblocks支持单文件编译运行，但是必须再project内才能使用debug

一个project内的源文件会合并编译，所以一般一个文件一个工程。

## 环境

### 编译

先安装minGW

安装codeblocks时可以直接选择。

## 编译/运行

### 快捷键

Function|Shortcut Key
---|---
构建|Ctrl + F9
编译当前文件|Ctrl + Shift + F9
运行|Ctrl + F10
构建并运行|F9
重新构建|Ctrl + F11

from <https://www.jianshu.com/p/4080e78fda4b>


## 调试（settings->debugger）

### 调试参数

![image.png](https://i.loli.net/2021/09/29/pi3lXBPncZQjtkN.png)

## 快捷键

Function|Shortcut Key
---|---
开始调试|F8
继续调试|Ctrl + F7
Step over a code block|F7
Step into a code block|Shift + F7
Step out of a code block|Ctrl + Shift + F7
添加/取消断点|F5
运行到下一个断点|F4
上一个错误|Alt + F1
下一个错误|Alt + F2

from <https://www.jianshu.com/p/4080e78fda4b>

### 调试界面

监视变量使用Watches窗口

![image.png](https://i.loli.net/2021/09/29/ABQ6xEPvY7KUwST.png)

拖动Watches窗口可以固定在左下。

将这个当前布局保存在View->Perspectives->GDB/CDB Debugger Default视图中，以后每次调试就会出现Watches窗口。

同理，可以将显示编译信息的log窗口保存在default视图中。

![image.png](https://i.loli.net/2021/09/29/gV1RiNmsDEPQckx.png)

### 其他

gdb的max-value-size默认为65536，即超过次长度的数组都不能显示。

解决方法：Settinggs->Debugger

![image.png](https://i.loli.net/2021/09/29/aHu8IQnG3EU9BVf.png)

相当于每次调试之前执行`gdb set max-value-size unlimited`来取消限制。

## 编辑器（settings->editor）

### 字体

![cb1.png](https://i.loli.net/2021/09/29/Q6vWYazXmM3nkIq.png)

### 格式化样式

![cb2.png](https://i.loli.net/2021/09/29/8Y1HbZkgVS9Uvjq.png)

### 快捷键

![image.png](https://i.loli.net/2021/09/29/fbASjzUgw4CLiIF.png)

## 其它

### 更改默认代码文件

更改`C:\Program Files\CodeBlocks\share\CodeBlocks\templates\wizard\console\cpp\main.cpp`，每次新建工程的`main.cpp`即是设置的模板。
