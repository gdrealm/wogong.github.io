---
layout: post
title: "在VMware中安装archlinux"
description: ""
category: it
tags: [archlinux, vmware]
---
{% include JB/setup %}

最近安装windows8，手贱格了Arch的分区，导致我远离了Arch的世界，虽然Win8用着感觉还挺不错的，但是终究没有Linux的shell好用，决定需要安装个虚拟机，装个Arch随便用用。加上64bit的windows使我的小Y史无前例的达到的4G的内存，装个Arch应该没有多大问题。

前几天在实习还没结束时也尝试安装了，但是因为Arch的安装方式最近改变，不再提供install scripts了。导致我在不熟悉的情况下弄砸了，旧版的arch安装包也因为glibc update遇到冲突，直接导致无法安装任何软件包，只能放弃。

这次使用VMware，一步一步按照[wiki](https://wiki.archlinux.org/index.php/Installing_Arch_Linux_in_VMware)的步骤，基本没有什么问题，只是在安装vm-tools时遇到了小问题，按照wiki安装open-vm-tools，但是启动服务时出现问题：
    rc.d start open-vm-tools
提出如下错误：
    :: Starting Open Virtual Machine Tools                      [BUSY]
	FATAL: Module vmblock not found.							[FAIL]
安装一个包即可解决问题：
	sudo pacman -S open-vm-tools-modules

挂载Windows共享文件：
    sudo mount -t vmhgfs .host:/sharename /mnt/hgfs
如果希望卡机自动挂载，在/etc/fstab文件加上：
    .host:/sharename	/mnt/hgfs vmhgfs fmask=0133,dmask=0022 0 0

接下来就是恢复自己的工作环境了。感谢Github，感谢Dropbox。

