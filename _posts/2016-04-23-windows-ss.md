---
title: Windows 使用 Shadowsocks 科学上网
author: wogong
date: 2016-04-23
---

本文介绍 Shadowsocks 协议在 Windows 平台的使用。

## 下载最新版 Shadowsocks
- 官方下载 [https://github.com/shadowsocks/shadowsocks-windows/releases][1] （需要代理）

## 配置说明
### 1. 配置服务器信息
可使用以下三种方式之一配置服务器信息。

1.1 手动配置

![手动配置服务器信息][image-1]\\

1.2 扫描二维码

右键点击 Shadowsocks 程序的系统托盘图标，如图示依次点击 服务器（Servers）-\>扫描屏幕上的二维码（Scan QRCode from Screen），获取服务器信息。

![扫描二维码获取服务器信息][image-2]\\

1.3 配置文件

将配置文件 gui-config.json 与 Shadowsocks.exe 放置于同一目录即可。

### 2. 配置代理
2.1 PAC

首先从 GFWlist 更新本地 PAC，然后配置为使用本地 PAC。

2.2 配置系统代理模式

`使用 PAC` 表示依据 PAC 文件确定哪些网址经过代理服务器，哪些网址直接连接（保证速度）。`全局模式`表示所有网址均经过代理服务器。

![配置代理模式][image-3]\\


2.3 打开系统代理

![打开系统代理][image-4]\\

至此，完成必要配置。打开 IE 浏览器，点击 Google [https://www.google.com][2] 测试代理是否成功。

### 注意事项
1. 本配置适用于任何浏览器，但是建议使用 IE 进行测试，Chrome 或者其他浏览器可能会因为配置了代理方面的插件导致失败。
2. 如果遇到无法使用的情况，建议配置系统代理模式为全局模式进行测试。
3. 更具体的调试信息可以右键查看日志。

[1]:	https://github.com/shadowsocks/shadowsocks-windows/releases
[2]:	https://www.google.com

[image-1]: https://dl.dropboxusercontent.com/s/zvc0xab4t7w8d4z/windows_ss_1.jpg
[image-2]: https://dl.dropboxusercontent.com/s/guj0ynl36tzfmzv/windows_ss_2.jpg
[image-3]: https://dl.dropboxusercontent.com/s/2gvjimp0ra4xdd8/windows_ss_3.jpg
[image-4]: https://dl.dropboxusercontent.com/s/gmnax4uxluezz7y/windows_ss_4.jpg
