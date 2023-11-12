---
title: Couldflare Tunnel穿透远程桌面服务（RDP）
date: 2023-10-17
math: true
toc: true
categories: 网络
---

> **对于外网用户，该方案免费且网络延迟很低，适合长期使用**
> 国内可能连接状况波动较大
{: .prompt-tip }

## 0.前置条件

- 国外支付方式 （信用卡/paypal）
- 域名

## 1. 注册

https://one.dash.cloudflare.com/

选择免费（$0）Plan，使用信用卡注册，验证信用卡用时比较长。

## 2. 域名

进入 https://dash.cloudflare.com/

对于在Cloudflare注册了域名的，进入第3步。

![image](https://github.com/pluto0x0/233/assets/54168673/09d47f1a-61ca-4447-977c-c7b443c61036)

大部分没有在Cloudflare注册过域名的，使用Cloudflare免费托管DNS。

在左侧“网站”菜单

![image](https://github.com/pluto0x0/233/assets/54168673/b510515c-a917-4426-a3cf-41b0be6dec8a)

点击“添加站点”

<img width="706" alt="image" src="https://github.com/pluto0x0/233/assets/54168673/fe30b9f0-9943-460d-8843-fbacc48736c5">

输入域名后，选择免费Plan

Cloudflare会给两个Nameserver，在域名服务商那里将域名的DNS服务器改成Cloudflare的Nameserver（比如 [阿里云设置dns](https://www.alibabacloud.com/help/zh/dws/user-guide/change-dns-servers-for-a-domain-name)）

注册完成后等待1小时左右，直到Cloudflare显示完成，网站在列表中出现：

<img width="1108" alt="image" src="https://github.com/pluto0x0/233/assets/54168673/b0095b4f-b3f9-4cbe-80cb-d47f666b06d9">

## 3. 设置Tunnel

左侧菜单选择 Zero Trust > Access > Tunnel

<img width="738" alt="image" src="https://github.com/pluto0x0/233/assets/54168673/2b03cc43-617b-4b45-8895-c20aa3589310">

点击 Create a tunnel

<img width="1025" alt="image" src="https://github.com/pluto0x0/233/assets/54168673/84f21ec5-321b-45ba-b31e-797d3b8ec210">

根据提示，下载对应平台的`cloudflared`，并且执行命令来注册服务。

<img width="906" alt="image" src="https://github.com/pluto0x0/233/assets/54168673/24c956a9-e4aa-4e74-a726-03517cbe9ad8">

命令类似

```
cloudflared.exe service install eyJKLHJiohsdifhalkjij8789aflkfj9wefj9zYzYzZGQiLCJ0IjoiNjc5YWNmMzQtYzY2NS00OTQ2LTllMDgtNWVjMjk4M2I4ZDEzIiwicyI6IlpXVTJOVEZoTURBdFl6WXpNUzAwT1RObExUazRNVFF0WlRKalpXWTFNakkyT1RVMiJ9
```

Arch用户可以使用AUR中的[cloudflared](https://aur.archlinux.org/packages/cloudflared-bin)

注意客户端和服务端（Tunnel连接的两个设备）都要安装`cloudflared`。

windows中`cloudflared.exe`会注册服务自动启动，并且修改该Tunnel配置后不需要重新注册。

填写域名和服务地址：

<img width="914" alt="image" src="https://github.com/pluto0x0/233/assets/54168673/46784df7-f32c-4c38-aa5e-965a58e0fb89">

其中domain栏会出现Cloudflare“网站”或者“域注册”中已有的域名，subdomain随意。


而
```
rdp://localhost:3389
```
表示把本地RDP默认端口 `3389` 连接到Tunnel。

至此Tunnel设置完成，Tunnel列表中显示`HEALTHY`就表示已经连接并且网络良好，如图
<img width="428" alt="image" src="https://github.com/pluto0x0/233/assets/54168673/5cfc240f-6a3c-4854-b1a5-d9d817340d15">

## 4. 连接Tunnel

根据[文档](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/use-cases/rdp/#2-connect-as-a-user)
在欲连接的设备上执行

```
cloudflared access rdp --hostname rdp.example.com --url rdp://localhost:3389
```

即将Tunnel（`rdp.example.com`）映射到本地`3389`端口，当然如果是windows则`3389`可能被占用，可以使用其他端口。

用RDP客户端连接到`localhost:[端口]`即可。
我在Arch上使用的是[remmina](https://wiki.archlinux.org/title/Remmina)客户端，功能强大、使用体验优秀，推荐。


---
## ref

https://sspai.com/post/79278

https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/use-cases/rdp/#2-connect-as-a-user


