---
layout: post
title: "通过isatap接入ipv6"
description: ""
category: it
tags: [ipv6, isatap]
---
{% include JB/setup %}

为什么通过isatap方式接入？

在没有ipv6的环境中，可以通过isatap服务器接入ipv6；在例如清华这种连个ipv6需要认证（经常bug）的地方，isatap接入可以避开认证。

### Linux
    $ sudo ip tunnel add sit1 mode sit remote 59.66.4.50 local yourip
    $ sudo ifconfig sit1 up
    $ sudo ifconfig sit1 add 2001:da8:200:900e:0:5efe:yourip/64
    $ sudo ip route add ::/0 via 2001:da8:200:900e::1 metric 1
note：replace “yourip” with your IP like 166.111.111.111

- 北京邮电大学 isatap.bupt.edu.cn
- 清华大学 isatap.tsinghua.edu.cn和59.66.4.50
- 华中科技大学 isatap.hust.edu.cn
- 台湾 tb.ipv6.apol.com.tw
- 上海交通大学 isatap.sjtu.edu.cn

脚本文件sit：（加上执行权限`chmod +x sit`）
    #!/bin/bash
    local_ip=101.36.22.24
    sudo ip tunnel add sit1 mode sit remote 59.66.4.50 local $local_ip
    sudo ifconfig sit1 up
    sudo ifconfig sit1 add 2001:da8:200:900e:0:5efe:$local_ip/64
    sudo ip route add ::/0 via 2001:da8:200:900e::1 metric 1
对于经常更换网络环境，或者采用DHCP动态分配IP的情况，可以采用以下自动获取本机IP的脚本：[下载地址](https://docs.google.com/open?id=0BwpUrJ713Y8MYzc2NjE0YWQtMGNmYi00OTYwLTg0MTEtM2VkYjYzNDdmMWQ0)
    #!/bin/bash
    arg=`ifconfig eth0 |grep "inet addr"| cut -f 2 -d ":"|cut -f 1 -d " "`
    local_ip=$arg
    sudo ip tunnel add sit2 mode sit remote 59.66.4.50 local $local_ip
    sudo ifconfig sit2 up
    sudo ifconfig sit2 add 2001:da8:200:900e:0:5efe:$local_ip/64
    sudo ip route add ::/0 via 2001:da8:200:900e::1 metric 1
note:
1. 上述自动获取IP脚本,[参考链接](http://hi.baidu.com/%B3%C2%B5%C2%C7%BFdeqiang/blog/item/68f28fa409ca29fd9152eec8.html)。
2. 上述脚本在系统更新后可能会失效，请自行检测。

*更新：*

- 由于Fedora15之后，网卡的命名规则发生了改变，对于含有多块网卡的电脑来说，上述代码中的sit0可能会出问题，比如我的无线网卡为sit0，另外一块网卡，命名为p5p1(不懂怎么得出的)，所以如果要使用上述代码，得将sit0改为p5p1，否则错误如下

		Command line is not complete. Try option "help"
	    sit1: unknown interface: 没有那个设备
		getaddrinfo: 2001:da8:200:900e:0:5efe:: -2
	    2001:da8:200:900e:0:5efe:: 未知的主机
	    RTNETLINK answers: No route to host

- 改变网络环境时，需要更改设置。可以这样做：

	    ifconfig down sit2

	再重新运行脚本建立隧道。

- 2011-12-17更新：今天不知为甚，即使执行了down的命令，还是会提示错误：

		add tunnel sit0 failed: No buffer space available

	表示十分费解。难道要重启么？当然重启是可以的，不过这不是太弱了么！！what a stupid method!!

- 2011-12-19更新：显然对于我这种有线无线网络环境经常改变的人来说基本会天天碰到这个问题，重启了几次之后实在不能忍受了。ipconfig -a可以看见我设置的隧道都在，sit1，sit2，sit0（这个不是我设置的，默认就有），我猜想删除这些记录就可以了，but我不知道命令。今天无意google发现这个命令：`ip tunnel`

		sit0: ipv6/ip  remote any  local any  ttl 64  nopmtudisc 6rd-prefix 2002::/16
		sit2: ipv6/ip  remote 59.66.4.50  local 101.5.124.000  ttl inherit  6rd-prefix 2002::/16
		sit1: ipv6/ip  remote 59.66.4.50  local 59.66.162.100  ttl inherit  6rd-prefix 2002::/16 
	note：上述IP地址已经调整过

	显然我的IP地址改变之后这些不能使用了，利用ip tunnel del sit*删除无用命令。重新建立隧道，问题解决！小小满足感，thanks the forum where I learned the ip tunnel[address](http://forums.gentoo.org/viewtopic-t-883527-view-next.html?sid=3b87b8e168f6f9e472195c51b6c73841)。
	再多说几句，其实现在Tsinghua的无线网是可以直接登录Ipv6的，只是这速度有点汗颜，600+的ping google，隧道才40+。所以还是继续isatap吧。
  
- sit* 星号数字自定，当然不能等于0了。 


### Windows（win7）

[命令文件](https://docs.google.com/leaf?id=0BwpUrJ713Y8MNGU3MTE4N2UtYWYzNS00ZDdiLWJkMjItM2FlODRkYWEzMTIx&hl=en_US),来自北邮人论坛，只是改为清华的IP。
以下命令全部以管理员身份运行。
或者直接一句命令：
    netsh interface ipv6 isatap set router 59.66.4.50
如果是xp系统的话，需要安装ipv6：
    netsh interface ipv6 install
windows下的比较麻烦，不知为甚偶尔会出问题。需要勾掉本地连接中网络配置中的ipv6协议。

- 2012-01-01更新：win7下经常出现的麻烦是注销或者休眠之后一般isatap都会失效，重启可以解决问题。应该和linux下的问题差不多，但是windows 的命令实在了解不多，无从下手。今天遇见同样的问题，大概看了下关于netsh命令。居然尝试成功了，但是依旧不知原因。记录如下，留待以后验证：
使用如下命令禁用并重启isatap：

		netsh interface isatap set state disabled
		netsh interface isatap set state default
	重新设置isatap。

- 关于netsh：

	- [参考1](http://msdn\.microsoft\.com/zh\-tw/cc740203\(WS\.10\).aspx)
	- [参考2](http://apps.hi.baidu.com/share/detail/44274899)


