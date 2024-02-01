---
title: Manjaro + i3wm 使用总结 [Archived]
date: 2023-05-04
categories: Linux
tags: Linux
math: true
---


# Manjaro + i3wm 使用总结

Manjaro + i3wm是社区版，下载 `.iso` 镜像安装即可。

## 安装

安装介质中的简体中文有显示问题。先使用英文。

如果使用中文安装，用户目录下的`Desktop` / `Downloads` 等目录名称会变成中文。

## 使用

### 使用镜像源

```shell
sudo pacman-mirrors -i -c China -m rank
```
[参考](https://blog.csdn.net/qq_38883889/article/details/116722348)



### 更新系统

```shell
sudo pacman -Syyu
```
[pacman用法](#pacman用法)  

### 设置时区

列出所有时区
```shell
timedatectl list-timezones
```

设置时区
```shell
timedatectl set-timezone Asia/Shanghai
```



[参考](https://zhuanlan.zhihu.com/p/422288980)

### 安装基础工具

```shell
sudo pacman -Sy git base-devel
```

`base-devel` 是常用编译和链接工具，类似Ubuntu中的 `build-essential`。

### 安装 `yay`（Arch 用户软件仓库，AUR）

```shell
sudo pacman -Sy yay
```

### 设置中文

- `$mod + d` 打开`dmenu`, 打开`manjaro-settings-manager`
- locale sttings? （本地化设定）-> 添加中文（`zh_CN.UTF-8`）

中文可能会显示为空白，需要安装字体

### 解决桌面 `conky` 乱码（待定）

```shell
sudo vim /usr/share/conky/conky_maia
```

进行字体设置的替换
```shell
# vim中
：%s/Bitstream Vera/anti/
```

### 安装中文字体

选择一种中文字体安装

文泉驿
```shell
sudo pacman -S wqy-bitmapfont wqy-microhei wqy-microhei-lite wqy-zenhei
```

思源字体
```shell
sudo pacman -S noto-fonts-cjk adobe-source-han-sans-cn-fonts adobe-source-han-serif-cn-fonts
```

其他
```shell
sudo pacman -S ttf-roboto noto-fonts ttf-dejavu
```

### 安装google chrome

```shell
yay -Sy google-chorome-stable
```

修改 `~/.config/mimeapps.list` , 将默认浏览器改为 `google-chrome-stable.desktop`。

### 安装clash

采用`clash-for-windows`的Linux版

```shell
yay -Sy clash-for-windows-bin
```

加入i3自启动： 

`~/.i3/config` 添加

```shell
exec_always --no-startup-id cfw
```


使用 `cfw` 命令打开。

### 安装vscode

```shell
yay -Sy visual-studio-code-bin
```

### 触摸板设置

配置文件 `/usr/share/X11/xorg.conf.d/40-libinput.conf`。

在包含 `touchpad` 的 `Section` 中

```shell
Option "NaturalScrolling" "true"
Option "TappingDragLock" "true"
```

`NaturalScrolling` 调整滚动方向。

[设置指针灵敏度$\rightarrow$](#指针灵敏度)

[参考](https://blog.csdn.net/weixin_45104776/article/details/107349627)


### 安装中文输入法

```shell
pacman -S fcitx fcitx-im fcitx-configtool
yay -S fcitx-sogoupinyin
```

加入i3自启动：

`~/.i3/config` 添加

```shell
exec_always --no-startup-id fcitx-autostart
```


### 文件管理器

名称
```shell
pcmanfm
```

[参考](https://forum.manjaro.org/t/open-directory-on-file-manager/113488
)

### `feh`设置壁纸

```shell
sudo pacman -S feh
```

加入i3自启动：

`~/.i3/config` 添加

```shell
exec_always --no-startup-id feh --randomize --bg-fill ~/Pictures/*
```

[参考](https://blog.csdn.net/weixin_43372529/article/details/106712115)

## 其他软件的安装

### svn

```shell
sudo pacman -S subversion
```

### remmina 远程桌面连接

```shell
sudo pacman -S remmina
```

对于 RDP 支持，还要安装可选的 `freerdp`。

```shell
sudo pacman -S freerdp
```
可以设置sooth font和window drag等提高画面质量或者速度。

## 进一步美化和其他项目

https://zhuanlan.zhihu.com/p/600673025

https://godliuyang.wang/2019/08/24/manjaro-i3wm-huan-jing-pei-zhi-pian/

### 安装终端模拟器

安装 `alacritty`

```shell
sudo pacman -Sy alacritty
```

编辑 `~/.config/alacritty/alacritty.yml`（需要创建文件）

```shell
# 原来tabspaces是8
tabspaces: 4
# 字体使用Soure Code Pro
family: Source Code Pro
# 不透明度：
#background_opacity: 0.6
window:
  opacity: 0.75
```

设置默认终端：

`~/.i3/config`：将`$mod+Return`的选项改为`alacritty`。

```shell
# start a terminal
#bindsym $mod+Return exec terminal
bindsym $mod+Return exec alacritty
```

## 指针灵敏度

### 查看xinput指针设备


```shell
$ xinput list
```

```plaintext
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ MOSART Semi. 2.4G RF Keyboard & Mouse Consumer Control	id=10	[slave  pointer  (2)]
⎜   ↳ MOSART Semi. 2.4G RF Keyboard & Mouse   	id=12	[slave  pointer  (2)]
⎜   ↳ Synaptics TM3289-021                    	id=14	[slave  pointer  (2)]
⎜   ↳ TPPS/2 Elan TrackPoint                  	id=15	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Power Button                            	id=6	[slave  keyboard (3)]
    ↳ Video Bus                               	id=7	[slave  keyboard (3)]
    ↳ Sleep Button                            	id=8	[slave  keyboard (3)]
    ↳ MOSART Semi. 2.4G RF Keyboard & Mouse   	id=9	[slave  keyboard (3)]
    ↳ MOSART Semi. 2.4G RF Keyboard & Mouse System Control	id=11	[slave  keyboard (3)]
    ↳ Integrated Camera: Integrated C         	id=13	[slave  keyboard (3)]
    ↳ AT Translated Set 2 keyboard            	id=16	[slave  keyboard (3)]
    ↳ ThinkPad Extra Buttons                  	id=17	[slave  keyboard (3)]
    ↳ MOSART Semi. 2.4G RF Keyboard & Mouse Consumer Control	id=18	[slave  keyboard (3)]
```

找到设备（这里是`id=12`）

查看设备的properties

```shell
$ xinput list-props 12
```

```plaintext
Device 'MOSART Semi. 2.4G RF Keyboard & Mouse':
	Device Enabled (189):	1
	Coordinate Transformation Matrix (191):	1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000
	libinput Natural Scrolling Enabled (318):	0
	libinput Natural Scrolling Enabled Default (319):	0
	libinput Scroll Methods Available (323):	0, 0, 1
	libinput Scroll Method Enabled (324):	0, 0, 0
	libinput Scroll Method Enabled Default (325):	0, 0, 0
	libinput Button Scrolling Button (326):	2
	libinput Button Scrolling Button Default (327):	2
	libinput Button Scrolling Button Lock Enabled (328):	0
	libinput Button Scrolling Button Lock Enabled Default (329):	0
	libinput Middle Emulation Enabled (330):	0
	libinput Middle Emulation Enabled Default (331):	0
	libinput Accel Speed (332):	0.000000
	libinput Accel Speed Default (333):	0.000000
	libinput Accel Profiles Available (334):	1, 1
	libinput Accel Profile Enabled (335):	1, 0
	libinput Accel Profile Enabled Default (336):	1, 0
	libinput Left Handed Enabled (337):	0
	libinput Left Handed Enabled Default (338):	0
	libinput Send Events Modes Available (303):	1, 0
	libinput Send Events Mode Enabled (304):	0, 0
	libinput Send Events Mode Enabled Default (305):	0, 0
	Device Node (306):	"/dev/input/event7"
	Device Product ID (307):	14648, 4146
	libinput Drag Lock Buttons (320):	<no items>
	libinput Horizontal Scroll Enabled (321):	1
	libinput Scrolling Pixel Distance (339):	15
	libinput Scrolling Pixel Distance Default (340):	15
	libinput High Resolution Wheel Scroll Enabled (322):	1
```

设置灵敏度（加速度）

```shell
$ xinput set-prop 12 "libinput Accel Speed" -0.7 
```

这里的加速度值范围在 $[-1,1]$

## 设置默认file manager

问题：打开目录时（比如chrome）默认使用vscode

```shell
xdg-mime default pcmanfm.desktop inode/directory
```
将相应的`mime`格式的默认应用设置成`pcmanfm`或者其他。

## Todo

硬件解码

~~cider~~

---

## 附录

### pacman用法

```shell
sudo pacman -S #安装软件
sudo pacman -Sy #获取最新打软件情况，如果已经是最新了，直接会提示已经更新到最新了。
sudo pacman -Syy #强行更新你的应用的软件库（源）
sudo pacman -Su #更新所有软件
sudo pacman -Syu #更新软件源并更新你的软件
sudo pacman -Syyu #强行更新一遍，再更新软件
```

多个（相似的）包：：

```shell
pacman -S plasma-{desktop,mediacenter,nm}
pacman -S plasma-{workspace{,-wallpapers},pa}
```

[参考](https://wiki.archlinuxcn.org/zh-hans/Pacman)

[参考](https://blog.csdn.net/qq_41601836/article/details/106515744)

### i3 快捷键

操作 | 快捷键
--- | ---
打开终端 | `mod+enter`
打开菜单 | `mod+d`
横向排列窗口 | `mod+h`
纵向排列窗口 | `mod+v`
将某个窗口全屏 | `mod+f`
模式选择 | `mod+e`默认（水平竖直）<br> `mod+s`层叠 <br> `mod+w`标签形式显示
选择窗口是浮动的还是平铺式 | `mod+shift+space`
退出窗口 | `mod+shift+q`
重启i3 | `mod+shift+r`
关闭i3 | `mod+shift+e`
在两个窗口中移动 | `mod+`方向/`jkl`;
打开工作区 | `mod+num`
将当前窗口移动到某工作区 | `mod+shift+num`

[参考](https://www.cnblogs.com/tongyan/archive/2012/10/04/2711550.html)
