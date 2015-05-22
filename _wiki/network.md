---
layout: wiki
title: network
create: 2014-06-13
update: 2014-06-13
---

## Commands
1. ifconfig
2. arp IP -- MAC
3. ping



## NOTE
0. arch wiki
   https://wiki.archlinux.org/index.php/Network

1. 带宽
   425Kbps，此处的b即是Byte。1Byte=8bit，加上其它开销，10Kb的宽带流量可大致获得1KB每秒的下载速度，所以下载速度为425KB/秒时带宽约为4.25Mbps。

2. 子网掩码

   255.0.0.0 = /8
   255.255.0.0 = /16
   255.255.255.0 = /24
   
   /29是限制最后32-29=3bit，就是1到7。
   192.168.1.0/29  192.168.1.1-192.168.1.7 
   
4. CDN
国内的规模较大的CDN基本都需要备案，小规模的虽然有，
但是稳定性及性能方面显然值得怀疑，所以，死了国内CDN
的心吧。

## softwares
1. inSSIDer 2.0  
   通过inSSIDer搜索无线热点，我们可以看到每个热点的MAC地址、网络名称（SSID）、无线信号强度、使用的信道、加密方式、最大无线传输速率和网络类型等主要信息，非常的全面。此外，在这些基本信息的下方，我们还可以查看每个时间段每个无线热点的信号强度和稳定性（纵坐标：信号强度，横坐标：时间段），其中纵坐标越高，表明信号强度越强，而横坐标越平滑，则表明无线信号越稳定。
   - 2.4GHz频段信道使用情况
查看2.4GHz频段信道使用情况，这是inSSIDer非常有亮点的一个功能（纵坐标：信号强度，横坐标：14信道）。在这里我们不仅可以看到每个无线热点所占用的无线信道，还能看到该热点的信号强度。此时，信号强度强，占用信道不拥挤的无线热点就是你的最佳选择。
   - 5GHz频段信道使用情况
查看5GHz频段信道使用情况，这是inSSIDer为广大用户提前准备的前卫功能，显示效果与2.4GHz频段相同。相信在双频段无线网络普及时，inSSIDer将同样为你带来最佳选择。
   - 附加功能
除了常见上述功能，inSSIDer还提供了新闻报道，网络过滤，GPS等附加功能，感兴趣的用户可以自己尝试。 通过inSSIDer软件，你将轻松选择无线信号强、网络稳定、信道不拥挤的最佳无线网络热点，赶快去试试吧。


* archlinux wireless

wireless,Archlinux

- Broadcom官网驱动下载地址:http://www.broadcom.com/support/802.11/linux_sta.php

- linux3.2以上需要补丁，如下操作

To get your wireless adapter working again:
Download this patch: bc_wl_abiupdate.patch
        patch -p0 src/wl/sys/wl_linux.c < bc_wl_abiupdate.patch
        sudo make; sudo make install; sudo depmod; sudo modprobe wl

- Arch每次更新内核总是需要重新编译网卡的，这次也不例外，可是居然出现了这样的错误：
        “make[1]: *** No rule to make target `(need'.  Stop. ”
深感不解，Google无果，对比此次和以往操作的差异，在于make的目录名由`wifi`变为`wifi(need copy)`,看来就是这个`(`导致了错误，更改，OK。


