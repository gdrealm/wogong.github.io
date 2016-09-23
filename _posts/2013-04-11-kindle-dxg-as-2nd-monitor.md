---
layout: post
title: "使用 kindle dxg 作为第二显示器"
description: "use kindle dxg as 2nd monitor"
tags: [kindle, vnc]
---

## 背景

Amazon都放弃dxg了，新产品没有跟上来，软件版本也是很久没有动静。毕竟是商业公司，dxg注定是小众的产品，太笨重，反应太慢是避不开的问题。但是用来看A4的PDF还是不错的。将其作为第二显示器也算是一物多用，略减遗憾。

以下测试环境为 windows 7 64bit，需要的软件主要是：[TightVNC](http://www.tightvnc.com/)，[Putty](http://www.putty.org/) 。

## 步骤

1. 越狱，usbnetwork等是准备工作，可以参考我的前一篇文章：[kindle dxg添加中文支持及更改字体](http://www.wogong.net/it/2012/08/22/kindle-dxg-chinese-fonts-support/)。

2. PC端：安装TightVNC  
   配置方面主要注意的是：Windows的防火墙设置，关闭或者设置例外。取消TightVNC的认证密码；在extra标签下设置为dxg准备的分辨率：1200x824，此处设置的端口号为最终连接的端口号。

3. Kindle端：安装[kindlevncviewer](http://www.mobileread.com/forums/showthread.php?t=150434)
将下载的附件压缩包内的kindlevncviewer子文件夹解压到kindle的根目录，也就是`/mnt/us`目录。这里需要注意的是要将此目录下的两个共享库文件复制到系统库文件下`/lib`，分别是`libjpeg.so.8`和`libvncclient.so.0`。按道理来说应该会先搜索当前目录，但是我在运行的时候会提示找不到共享库文件，所以复制到系统库文件下。这样操作之后是OK的。

4. 在kindle上执行如下命令：`./kindlevncviewer -config ./config.lua 192.168.2.1:5901`
不出意外的话就OK了。但是出意外的情况会有很多，你可以根据mobileread论坛上的讨论获得线索，或者直接看github上的代码。相关资料后附。

5.NOTE:
如果出现这样的错误：

    com.lab126.powerd failed to set value for property prevent ScreenSaver

一般来说是你的VNC Server出问题了，请检查防火墙，端口，认证等设置，主要是TightVNC Server的配置。

另外，参考`[4]`是另外一种方式，通过浏览器渲染，有兴趣的也可以看一看，个人觉得有点蛋疼。

其他问题欢迎留言讨论。:)

附张折腾成功的照片

![dxg as screen](http://wogong-image.b0.upaiyun.com/dxg_as_screen.jpg)

## 参考

[1] [mobileread thread](http://www.mobileread.com/forums/showthread.php?t=150434)  
[2] [Github Source Code](https://github.com/hwhw/kindlevncviewer)  
[3] [http://blog.csdn.net/sjtuyunlei/article/details/7671608](http://blog.csdn.net/sjtuyunlei/article/details/7671608)   
[4] [http://www.mobileread.com/forums/showthread.php?t=148581](http://www.mobileread.com/forums/showthread.php?t=148581)
