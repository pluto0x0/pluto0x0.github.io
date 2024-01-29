---
title: Archlinux + i3wm 从0配置指南
date: 2023-11-12 01:03:06
img_path: /_posts/
math: true
categories: Linux
tags: Linux
image:
  path: ../upload/img/2023-11-12-archlinux-with-i3wm-image-2.png
---

## Intro

之前用manjro+i3，勉强算是开箱即用，然而还是准备折腾arch。

## 安装archlinux

根据
[中文安装指南](https://wiki.archlinuxcn.org/wiki/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97)
进行，只选择了重要的步骤。

### 启动到 live 环境

首先准备安装镜像、安装介质（U盘）

### 连接互联网

这里使用wifi连接，以太网请忽略这一步。

连接wifi可以使用[iwd](https://archlinux.org/packages/?name=iwd)包的[iwctl](https://wiki.archlinuxcn.org/wiki/Iwd#iwctl)命令。

> 列出所有 WiFi 设备： [iwd]# device list
>
> 开始扫描网络: [iwd]# station *device* scan
>
> 列出所有可用的网络: [iwd]# station *device* get-networks
>
> 连接到一个网络：[iwd]# station *device* connect *SSID*

运行  `ping archlinux.org`  测试网络连接。

### 创建硬盘分区

```shell
fdisk -l # 列出所有分区
fdisk /dev/the_disk_to_be_partitioned #（要被分区的磁盘）进行分区。
```

参考[分区方案示例](https://wiki.archlinuxcn.org/wiki/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97#%E5%88%86%E5%8C%BA%E6%96%B9%E6%A1%88%E7%A4%BA%E4%BE%8B)

本次给EFI分了512M，给SWAP分了8G（8G内存），剩下给 `/` 挂载点。

### 格式化分区

[参考](https://wiki.archlinuxcn.org/wiki/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97#%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%88%86%E5%8C%BA)，注意相应的文件系统

### 挂载分区

分别挂载主分区和EFI分区到 `/mnt` 和 `/mnt/boot`  上。

注意启用swap分区。

### 开始安装系统

运行

```shell
pacman -Sy pacman-mirrorlist
```

### 配置系统

#### 生成fstab

```shell
genfstab -U /mnt >> /mnt/etc/fstab
```

#### chroot 到新安装的系统

```shell
arch-chroot /mnt
```

注意是 `arch-chroot` 命令。

#### 设置时区、区域和本地化设置

注意语言要选择英语  `en_US.UTF-8` ，中文无法显示。

#### 创建 hostname 文件、设置 root 密码

#### ！安装必要软软件包

一般来说需要安装

引导需要的包：

- `grub`
- `os-prober` , 探测其他安装的OS，显示在grub菜单中。
- `efibootmgr`

常用工具：

- `nano`  /  `vi`  /  `vim`
- `sudo`  （注意可以新建一个非root用户并且将之加入sudoers列表中，要修改列表，请用 `visudo` 命令以防sudoers列表出现问题导致系统问题）

网络连接

- `iw` ，  `iwd`  连接wifi
- 自动启动网络服务（否则DNS服务无法使用）：

```
systemctl enable systemd-networkd
systemctl enable systemd-resolved
```

字体

- 参见[wiki](https://wiki.archlinuxcn.org/wiki/%E4%B8%AD%E6%96%87%E6%9C%AC%E5%9C%B0%E5%8C%96#Fonts)， 我使用了思源简体无衬线字体。

> 此时请为图形界面新建一个非root用户！
{: .prompt-warning }

#### 安装引导

```shell
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader=Arch --recheck
grub-mkconfig -o /boot/grub/grub.cfg
```

 `grub-mkconfig`  类似其他平台的 `grub-update` 的作用。

接下来

卸载挂载点，重启

```shell
umount -R /mnt
reboot
```

此时一切顺利的话就可以引导进入新系统了。

## 配置系统

### 语言

确保  `/etc/locale.gen`{: .filepath} 中的  `zh_CN.UTF-8`  项已经被取消注释。

运行

```shell
locale-gen
```

然后在 `/etc/locale.conf`{: .filepath}写入

```shell
LANG=zh_CN.UTF-8
```

> 此时重启后输入 `locale` 命令应该可以看到 `LANG` 变量已经被设置为中文，如果不是：
{: .prompt-info }

在 `/etc/environment`{: .filepath}写入

```shell
LANG=zh_CN.UTF-8
```

### 网络连接

此时有必要的软件包，可以在命令行连接wifi了，但是如果遇到了连接问题（ `ping` 出错），请检查：

> 根据[这里](https://bbs.archlinux.org/viewtopic.php?pid=1973099#p1973099)，将以下内容写入  `/etc/iwd/main.conf`{: .filepath}。
{： .prompt-tip }

```ini
[General]
EnableNetworkConfiguration=true

[Network]
NameResolvingService=systemd
```

> 尝试启动网络服务

```shell
# 重启服务
systemctl restart systemd-networkd
systemctl restart systemd-resolved
# 自动启动
systemctl enable systemd-networkd
systemctl enable systemd-resolved
```

### 安装图形界面：Xorg和i3相关包

```shell
sudo pacman -S xorg lightdm lightdm-gtk-greeter i3-wm i3lock i3status i3blocks dmenu
```

（其中 `lightdm-gtk-greeter` ）负责登录界面

安装终端（自行选择）

```shell
sudo pacman -S alacritty
```
> 20240101更新：`~/.config/alacritty/alacritty.yml`{: .filepath} 已经弃用，使用 `alacritty migrate` 迁移到 `/home/flayed/.config/alacritty/alacritty.toml`{: .filepath}
{: .prompt-tip }

`/home/flayed/.config/alacritty/alacritty.toml`{: .filepath} :

```toml
[font]
size = 8

[font.bold]
family = "Source Code Pro"
style = "Bold"

[font.bold_italic]
family = "Source Code Pro"
style = "Bold Italic"

[font.italic]
family = "Source Code Pro"
style = "Italic"

[font.normal]
family = "Source Code Pro"
style = "Regular"

[window]
opacity = 0.75  # 窗口不透明度 
```

启动lightDM

```shell
sudo systemctl start lightdm.service
sudo systemctl enable lightdm.service
```

此时进入图形界面，选择非root用户登录

[参考](https://www.51cto.com/article/759235.html#%E5%9C%A8%20i3%20%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E4%B8%AD%E6%9B%B4%E6%94%B9%E5%A3%81%E7%BA%B8)

### 程序功能配置

#### 安装AUR包管理器

使用 `yay` 包，这里我源码编译有点问题，直接使用了二进制包 <https://aur.archlinux.org/yay-bin.git>。

#### feh，i3lock-color，主题，图标主题

[参考](https://www.51cto.com/article/759235.html#%E5%9C%A8%20i3%20%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E4%B8%AD%E6%9B%B4%E6%94%B9%E5%A3%81%E7%BA%B8)

#### 文件管理器

```shell
sudo pacman -S pcmanfm
```

设置为目录的默认打开方式

```shell
xdg-mime default pcmanfm.desktop inode/directory
```

#### 透明窗口混合器

[参考](https://www.51cto.com/article/759235.html#%E5%9C%A8%20i3%20%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E4%B8%AD%E6%9B%B4%E6%94%B9%E5%A3%81%E7%BA%B8)

### 其他配置

#### zsh, oh-my-zsh

<https://ohmyz.sh/#install>

插件：

- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)
- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)

#### 网络托盘图标

安装[networkmanager](https://archlinux.org/packages/?name=networkmanager)包

其中 `nm-applet` 用于显示托盘图标

启动服务：

```shell
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager
```

i3的config已经包含了以下内容来启动 `NetworkManager` ：

```shell
exec --no-startup-id NetworkManager
exec --no-startup-id nm-applet
```

#### 中文输入法

使用搜狗

```shell
sudo pacman -S fcitx fcitx-im fcitx-configtool
yay -S fcitx-sogoupinyin
```

i3配置中添加

```
exec_always --no-startup-id fcitx-autostart
```

此外在 `/etc/environment`{: .filepath} 添加

```shell
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
```

> 输入法有托盘图标
{: .prompt-tip }

取消输入法浮动窗口阴影

首先使用picom默认配置

```config
cp /etc/xdg/picom.conf ~/.config/picom/picom.conf
```

查找浮动窗口的类名：

```shell
xprop | grep -i class
```

```text
WM_CLASS(STRING) = "sogoupinyin-service", "sogoupinyin-service"
```

得到类名`sogoupinyin-service`

修改`~/.config/picom/picom.conf`{:.filepath}，添加一行`"class_g = 'sogoupinyin-service'"`

```
# Specify a list of conditions of windows that should have no shadow.
#
# examples:
#   shadow-exclude = "n:e:Notification";
#
# shadow-exclude = []
shadow-exclude = [
  "name = 'Notification'",
  "class_g = 'Conky'",
  "class_g ?= 'Notify-osd'",
  "class_g = 'Cairo-clock'",
  "_GTK_FRAME_EXTENTS@:c",
  "class_g = 'sogoupinyin-service'"
];
```

#### 音量托盘图标

```shell
pacman -S pulseaudio pavucontrol pasystray
```

 `pavucontrol` 控制音量

 `pasystray` 托盘图标，在i3添加自启动

i3里已经有了音量Fn的绑定。

#### 亮度

安装 `xorg-xbacklight` 或者 `brightnessctl` 包，效果基本相同。

安装 `xmodmap` 支持Fn键。

<!-- 通过  `brightnessctl i`  得到最大亮度1060， -->
在i3配置里添加

```shell
# @@backlight hotkey
bindsym XF86KbdBrightnessDown exec --no-startup-id brightnessctl s 10%-
bindsym XF86KbdBrightnessUp exec --no-startup-id brightnessctl s 10%+
bindsym XF86MonBrightnessDown exec --no-startup-id brightnessctl s 10%-
bindsym XF86MonBrightnessUp exec --no-startup-id brightnessctl s 10%+
```

其中按键的名称可以在 `xmodmap -pke` 的输出中查找。

#### 状态栏

使用  `polybar` ，以及[第三方主题](https://github.com/adi1090x/polybar-themes/)，其中音量显示、亮度显示、电池显示、托盘图标的显示都需要额外配置。

主题内支持设置壁纸的同时设置相应的主题色（包括zsh主题色）。

> 鼠标放在滑块上滚动使用。
{: .prompt-tip }

#### 触摸板

根据[参考](https://twor.me/posts/archlinux_gesture/)

安装触摸板驱动

```shell
sudo pacman -S xf86-input-libinput
```

把以下内容写入  `/etc/X11/xorg.conf.d/30-touchpad.conf`{: .filepath }

```
Section "InputClass"
    Identifier "touchpad"
    Driver "libinput"
    MatchIsTouchpad "on"
    Option "Tapping" "on"
    Option "TappingButtonMap" "lrm"
EndSection
```

> 这里 `"lrm"` 指的是1，2，3指轻触分别表示左键、右键、中键点击。
{: .prompt-tip }

接下来设置触摸板手势：

安装 `fusuma` （AUR中[ruby-fusuma](https://aur.archlinux.org/packages/ruby-fusuma)）包和插件（AUR中[ruby-fusuma-plugin-sendkey](https://aur.archlinux.org/packages/ruby-fusuma-plugin-sendkey)）用来捕获手势和发送按键。

这是我的配置 ： `~/.config/fusuma/config.yml`

```yml
swipe:
  3: 
    left: 
      sendkey: 'LeftMeta+LeftShift+Left'
    right: 
      sendkey: 'LeftMeta+LeftShift+Right'
    up: 
      sendkey: 'LeftMeta+LeftShift+Up'
    down: 
      sendkey: 'LeftMeta+LeftShift+Down'
  4: 
    up: 
      sendkey: 'LeftMeta+F'
pinch:
  in:
    sendkey: 'LeftCtrl+Minus'
  out:
    sendkey: 'LeftCtrl+Equal'

threshold:
  swipe: 0.6
  pinch: 0.2

interval:
  swipe: 0.3
  pinch: 0.3
```

其中 `3`   `4`  表示几根手指， `swipe`   `pinch`  表示 “扫” 和 “捏” 两个手势，至于按键绑定根据自己偏好，这里是用作切换窗口位置和放大/缩小。

启动服务：

```shell
sudo systemctl start fusuma
sudo systemctl enable fusuma
```

#### 功耗控制

根据[参考](https://arch.icekylin.online/guide/advanced/power-ctl.html)

安装  `TLP`  包和 ui

```shell
sudo pacman -S tlp tlp-rdw
```

```shell
yay -S tlpui
```

启动服务

```shell
sudo systemctl enable tlp.service
sudo systemctl enable NetworkManager-dispatcher.service
sudo systemctl mask systemd-rfkill.service # 屏蔽以下服务以避免冲突，确保 TLP 无线设备的开关选项可以正确运行
sudo systemctl mask systemd-rfkill.socket

sudo tlp start
```

 `tlpui`  打开UI控制台，我这里把  `CPU_MAX_PERF_ON_BAT`  设置为  `30`  提高续航，还有其他诸如降低cpu电压暂时没有搞。

#### 系统快照

根据[参考](https://aprilzz.com/archives/%E5%9C%A8arch%E4%B8%AD%E4%BD%BF%E7%94%A8timeshift%E4%BF%9D%E7%B3%BB%E7%BB%9F%E5%B9%B3%E5%AE%89)

使用 [timeshift](https://archlinux.org/packages/extra/x86_64/timeshift/)

```shell
sudo pacman -S timeshift # 安装Timeshift
sudo systemctl enable --now cronie.service # 启用Crond服务，启用该服务后Timeshift才能定期自动创建快照
```

运行  `timeshift-gtk`  启动UI，我选择了rsync备份，在1T的windows盘中分了128G的EXT4分区来备份。备份可以自动定时进行，每次仅仅占用1G左右，可以选择时时候复制用户文件。

#### 截屏

在i3配置中添加

```shell
# @@Screenshots
bindsym Print exec --no-startup-id maim "/home/$USER/Pictures/$(date)"
bindsym $mod+Print exec --no-startup-id maim --window $(xdotool getactivewindow) "/home/$USER/Pictures/$(date)"
bindsym Shift+Print exec --no-startup-id maim --select "/home/$USER/Pictures/$(date)"

# @@Clipboard Screenshots
bindsym Ctrl+Print exec --no-startup-id maim | xclip -selection clipboard -t image/png
bindsym Ctrl+$mod+Print exec --no-startup-id maim --window $(xdotool getactivewindow) | xclip -selection clipboard -t image/png
bindsym Ctrl+Shift+Print exec --no-startup-id maim --select | xclip -selection clipboard -t image/png
```

并且安装相应  `xclip` ， `xdotool` ， `maim` 包

分别作为**复制/保存 全屏/窗口/区域截图**的功能。

#### 删除i3窗口边框

在i3配置中添加

```shell
# @@remove border
default_border none
default_floating_border none
```

#### 鼠标指针

下载指针主题，在 `lxappearance` 中启用即可。
如果无法正常显示鼠标指针：

试着创建一个将 `~/.icons/default/cursors`{: .filepath}(假设为指定用户安装)指向 `.local/share/icons/cursor_theme_name/cursors`{: .filepath}的符号链接然后再次重启 X。

[参考](https://wiki.archlinuxcn.org/wiki/%E5%85%89%E6%A0%87%E4%B8%BB%E9%A2%98)

问题排查

- 如果在i3桌面上鼠标指针一直显示忙，在配置中所有`exec`加上`--no-startup-id`参数

## 软件包列表

### 编辑器

[Visual Studio Code](https://aur.archlinux.org/packages/visual-studio-code-bin)

### 网络浏览器

[Google Chrome](https://aur.archlinux.org/packages/google-chrome)

### pdf阅读器

[Okular](https://archlinux.org/packages/extra/x86_64/okular/)

### Office套件

[Onlyoffice](https://aur.archlinux.org/packages/onlyoffice-bin)

### 远程桌面

[Remmina](https://archlinux.org/packages/extra/x86_64/remmina/)

### 局域网文件分享

[Landrop](https://aur.archlinux.org/packages/landrop)

### bittorrent客户端

[Qbittorrent Enhanced Edition](https://aur.archlinux.org/packages/qbittorrent-enhanced)

### 剪贴板历史

[parcellite](https://archlinux.org/packages/extra/x86_64/parcellite/)

### 蓝牙

<https://wiki.archlinuxcn.org/wiki/%E8%93%9D%E7%89%99>

驱动和实用程序

- [bluez](https://archlinux.org/packages/extra/x86_64/bluez/)
- [bluez-utils](https://archlinux.org/packages/extra/x86_64/bluez-utils/)

```shell
sudo systemctl start bluetooth
sudo systemctl enable bluetooth
```

图形界面

- [blueman](https://archlinux.org/packages/extra/x86_64/blueman/)

在 `~/.config/i3/config`{: .filepath}:

```shell
exec_always --no-startup-id blueman-applet
```

### 自动锁定

[xidlehook](https://aur.archlinux.org/packages/xidlehook)

`~/.config/i3/config`{: .filepath}:

```shell
set $time_lock 300
exec --no-startup-id xidlehook --detect-sleep --not-when-audio --not-when-fullscreen --timer $time_lock $lock ''
```

### 桌面通知

[dunst](https://archlinux.org/packages/extra/x86_64/dunst/)

i3配置
```shell
exec_always --no-startup-id dunst
```

测试通知

```shell
$ notify-send "title" "test notification"
```

### 桌面组件

[Conky](https://archlinux.org/packages/extra/x86_64/conky/)

i3中：

```shell
exec_always --no-startup-id conky
```

配置 `~/.config/conky/conky.conf`{: .filepath}

```lua
conky.config = {
    -- Conky窗口设置
    own_window = true,
    own_window_type = 'override',  -- 使Conky显示在桌面上
    own_window_class = 'Conky',
    background = true,
    own_window_transparent = true,  -- 透明窗口
    own_window_argb_visual = true,  -- 开启真正的透明效果
    own_window_argb_value = 0,  -- 透明度设置，0是完全透明

    -- 文字设置
    use_xft = true,
    font = 'DejaVu Sans Mono:size=11',
    xftalpha = 0.8,
    alignment = 'top_right',  -- 窗口在屏幕上的位置

    -- 尺寸和颜色
    gap_x = 30,
    gap_y = 60,
    minimum_width = 200,
    default_color = 'white',

    -- 更新间隔
    update_interval = 1,

    -- 其他设置
    double_buffer = true,
    draw_shades = false,
    draw_outline = false,
    draw_borders = false,
    draw_graph_borders = false,
    override_utf8_locale = false,
    no_buffers = true,
    uppercase = false,
    cpu_avg_samples = 2,
};

conky.text = [[
${user_names} @ ${nodename}
${distribution} ${kernel}

${color grey}Net
${color}${wireless_essid wlan0} @ ${wireless_freq wlan0}
${addrs wlan0} ${wireless_ap wlan0}

${color grey}Time
${color}$time

${color grey}Up time
${color}$uptime

${color grey}CPU Usage
${color}$cpu% @${freq}Mhz
${cpugraph 50,320 000000 ffffff}

${color grey}RAM Usage
${color}${memperc}%
${memgraph 50,320 000000 ffffff}
${membar 4}
${color}${mem}${alignr}${memavail}

${color grey}File Systems
${color}/ ${fs_type /} ${fs_free_perc /}% ${fs_size /} 

$color ${fs_bar /}
${fs_used /}${alignr}${fs_free /}

${color grey}Disk IO
${color grey}read ${color}${diskio_read}   ${color grey}write ${color}${diskio_write}
${diskiograph 50,320 000000 ffffff}

${color grey}Top

${color}Process           CPU%  Mem%
${color grey}${hr}
${color}${top name 1}${top cpu 1}${top mem 1}
${top name 2}${top cpu 2}${top mem 2}
${top name 3}${top cpu 3}${top mem 3}
${top name 4}${top cpu 4}${top mem 4}
${top name 5}${top cpu 5}${top mem 5}
]];

```

see also:

<https://conky.cc/variables#diskio>

<https://conky.cc/config_settings>

### 自动休眠和合上盖子功能

`/etc/systemd/logind.conf`{:.filepath}

```ini
[login]
...
HandlePowerKey=suspend
HandleLidSwitch=suspend
IdleAction=suspend
IdleActionSec=10min
...
```

这里不同的电源模式可以[参考](https://wiki.archlinux.org/title/Power_management/Suspend_and_hibernate)，可能不是每种该模式都被硬件支持。

最后

```shell
sudo systemctl restart systemd-logind
```

### 图片查看器

[ristretto](https://archlinux.org/packages/extra/x86_64/ristretto/)

```shell
xdg-mime default org.xfce.ristretto.desktop image/png
xdg-mime default org.xfce.ristretto.desktop image/jpeg
```

### 鼠标设置

使用xinput，[参考](../manjaro-i3wm/#%E6%8C%87%E9%92%88%E7%81%B5%E6%95%8F%E5%BA%A6)

或者使用[xinput-gui](https://aur.archlinux.org/packages/xinput-gui)包。


## to-do list

- ~~剪贴板历史~~
- ~~蓝牙（blueman）~~
- 视频硬件解码
- ~~自动锁定~~
- ~~合上盖子~~
- 主题颜色
- ~~桌面组件~~
- ~~桌面通知~~
