---
layout: post
title: "kindle dxg添加中文支持及更改字体"
description: "kindle折腾备忘"
category: it
tags: [kindle]
---
{% include JB/setup %}

## 汉化方法
kindle dxg更换字体最普遍的方法来自国外的mobileread论坛的[这篇帖子](http://www.mobileread.com/forums/showthread.php?t=88004)。简而言之，是采用安装包的方式自动破解、更换字体。这里不再详述，目前网上能够搜到的大部分汉化皆是这种方法。多看论坛采用的也是类似的方法。

## 我遇到的问题？
dxg刚刚拿到手时，也是按照mobileread中的方法，但是数次尝试中文依旧无法显示（显示方框）。因为不知这种方法的原理，只能查看安装脚本的代码。虽然不能十分清楚，但是发现其是建立链接，将系统目录链接到用户文件目录下，更改字体。既然自动安装无法成功，那便采用手动的形式。自己建立链接，更改字体。

## 一种简单直观的方法
mobileread论坛中方法对于普通用户来说可以称为黑箱操作，参考kindle4更换字体的方法，利用usbnetwork登录kindle修改系统字体，达到添加中文支持功能，及更改字体的目的。

1.越狱（jail break）
采用mobileread论坛中提供的升级文件（上述帖子附件中）
    kindle-jailbreak-0.10.N.zip (112.6 KB, 5684 views)
（注：文件可能已更新，建议采用最新版升级文件越狱）

2.添加usbnetwork支持
越狱之后添加usbnetwork。usbnetwork是采用usb将kindle与PC连接，建立局域网。添加usbnetwork的作用之一在于可以在PC上通过ssh或者telnet操作kindle系统文件。
mobileread论坛同样提供了方便的升级文件：
    kindle-usbnetwork-0.39.N.zip (10.84 MB, 1377 views）

在search中输入`;debugon` 开启debug模式,查看是否开启成功请输入`help`，会弹出帮助窗口。开启debug后输入 `usbnetwork 按确定。此时usb连接pc将不会出现存储连接提示，kindle的显示也不会有变化（电池显示充电）。

3.通过ssh或者telnet连接kindle，找到字体文件夹，建立链接到文件目录，通过字体替换的方式改变字体。至于为什么不直接替换系统路径下的字体，原因有二，其一，直接操纵系统文件危险性较高，其二，dxg的系统路径空间有限，替换较大的字体文件时可能会遇到空间不够的问题。

4.重启。以后更改字体直接在文件路径下替换字体文件即可（重启生效）。


