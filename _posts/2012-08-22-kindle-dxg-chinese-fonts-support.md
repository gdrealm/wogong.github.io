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


=======
---
layout: post
title: "kindle dxg添加中文支持及更改字体,升级kindle3.2.1"
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

系统字体目录: `/usr/java/lib/fonts`
链接命令: `ln -s /us/documents/fonts /usr/java/lib/fonts`

以上操作注意备份。

4.重启。以后更改字体直接在文件路径下替换字体文件即可（重启生效）。


## 升级kindle 3.2.1


1. 为什么升级？
	- 更好的web浏览器。但是对于现在3G在中国大陆限制上网（只能amazon，wikipedia），这种改进没有多大的作用。
	- 加深功能。对于灰度扫描的PDF文件，阅读体验改进明显。
	- 其他尚待发现

2. 升级过程

感谢[[http://yifan.lu/p/kindleupdater/|Yifan Lu]]的工作，升级方法与相关文件均是来自Yifan Lu的文章。

- 准备工作
   - 推荐将Kinle DXG里面的书籍转移至别处，卸载一切汉化或者其他插件。如果出错，可以查看readme文件，里面提供了出错提示的查询与解释。
   - DXG的系统版本为2.5.8，其他版本不保证成功。

	1.将Kindle DXG越狱 (已越狱可跳过此步)
		连接电脑，把update_jailbreak_0.7.N_dxg_install.bin拷到kindle硬盘根目录下。断开电脑连接，进入menu->Settings->update your kindle, Kindle开始越狱(需时约5分钟)，重启后重新连接电脑。

	2.制作DXG 2.5.8系统的镜像 (备份自身的系统)
		把update_dxg-2.5.8-prepare_kindle.bin拷到kindle硬盘根目录下。断开电脑连接，仍然是进入update your kindle, Kindle开始备份2.5.8的系统(需时约45-60分钟)，重启后重新连接电脑。将硬盘下output目录拷贝到它处妥善保存。以下是我在备份时候的状态信息，可能有误差，仅供参考：
		- 16:46 开始制作2.5.8系统备份镜像 
		- VCreating image...
		- 16:57 Compressing image...
		- 17:23 Generating update package...
		- 17:34 GeneratiGenerating update...
		- 17:41 GeneratiGeneraCleaning up...
		- 17:46 GFlashing recovery kernel...
		- 17:47 完成

	3.升级Kindle 3.2.1系统
		把update_kindle_3.2.1.bin和tts-files.tar拷到kindle硬盘根目录下。断开电脑连接，依旧是进入update your kindle,Kindle开始升级至3.2.1，需时约30-45分钟。首次重启需时较长，大约需要10-15分钟左右。然后去查看setting下的kindle版本，应该就已经是3.2.1了。

相关文件下载(地址取自网络，不对其版权问题负责，请下载者慎重考虑)
[3.2.1镜像文件](http://dl.vmall.com/c0nw3a6bnd)

含文件
- tts-files.tar  
- update_dxg-2.5.8-prepare_kindle.bin
- update_jailbreak_0.7.N_dxg_install.bin
- update_kindle_3.2.1.bin

[2.5.8备份文件](http://dl.vmall.com/c0iuax42ah)


3. 注意事项

	- 因为某些原因，Amazon限制了free 3G在中国大陆的使用，如果你是2012年8月之前注册的，那么请不要升级，如果你需要无限制的3G功能的话。限制3G为，你无法使用kindle的3G网络登陆除Amazon和Wikipedia之外的网站。
	- 升级时间漫长，请一定保持耐心以及kindle的电量充满。
	- Yifan Lu提供的文件中含有详细的说明，相关问题请仔细查看readme文件。


上述升级过程摘自[麦兜电纸书论坛](http://bbs.mydoo.cn/thread-32419-1-1.html)
向Yifan Lu以及其他人员致谢。

## 升级3.2.1之后如何使用usbnetwork

我使用升级前的升级包更新总是失败，使用`;debugOn`无法进入debug模式，也就无法打开usbnetwork。其实usbnetwork已经安装成功，只是无法进入。通过安装[launchpad](http://www.mobileread.com/forums/showthread.php?t=97636)可以解决这个问题。

安装完成后，修改`launchpad.ini`文件，增加`N = !/test/bin/usbnetwork`,保存，重启。快速安`shift+n`可以在存储模式与网卡模式之间切换，进入usbnetwork之后按照之前的修改即可，注意3.2.1与2.5.8字体文件的不同，3.2.1增加了对中文字体的支持。

