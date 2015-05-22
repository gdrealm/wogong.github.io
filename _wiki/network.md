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
0. curl ip.gs/ip.cn/ip.tl
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

## arp
ARP协议用在局域网(LAN)内部。借用ARP协议，设备可以知道同一局域网内的IP-MAC对应关系。当我们访问一个本地IP地址时，设备根据该对应关系，与对应的MAC地址通信。通过ARP工具，我们可以知道局域网内的通信是否正常。

      arp -a //显示本地存储的IP-MAC对应关系
      sudo arping -I eth0 192.168.1.1 //经eth0接口，发送ARP请求，查询IP为192.168.1.1设备的MAC地址
      sudo arp-scan -l //查询整个局域网内的所有IP地址的对应MAC地址
      sudo tcpdump -i en0 arp //监听en0接口的arp协议通信
 

##

路由局域网通过路由器，接入广域的互联网。互联网上的通信往往要经过多个路由器接力。途中路由器的故障，可能导致互联网访问异常。
netstat -nr
显示路由表。从路由表中，可以找到网关(Gateway)。网关是通向更加广域网络的出口。
 
traceroute 74.125.128.99
追踪到达IP目的地的全程路由。
  traceroute -I 74.125.128.99
  通过ICMP协议，追踪路由。ICMP协议经常会被禁用，所以会返回"*"的字符串。
  sudo traceroute -T -p 80 74.125.128.99
  通过TCP协议，经80端口，追踪路由。TCP协议的默认端口80很少会被禁用。

网络监听tcpdump是一款网络抓包工具。它可以监听网络接口不同层的通信，并过滤出特定的内容，比如特定协议、特定端口等等。我们上面已经使用tcpdump监听了ARP协议通信。这里我们来看更多的监听方式。
sudo tcpdump -i en0
监听en0接口的所有通信
  sudo tcpdump -A -i en0 
  用ASCII显示en0接口的通信内容
  sudo tcpdump -i en0 'port 8080'
  显示en0接口的8080端口的通信
  sudo tcpdump -i eth1 src 192.168.1.200
  显示eth1接口，来自192.168.1.200的通信
  sudo tcpdump -i eth1 dst 192.168.1.101 and port 80
  显示eth1接口80端口，目的地为192.168.1.101的通信
  sudo tcpdump -w record.pcap -i lo0
  将lo0接口的通信存入文件record.pcap

运行Tcpdump监听POP邮箱密码：tcpdump -X -i br-br0 port 110



## pv

测试ssh连接速度和带宽

安装pv：
sudo apt-get install pv
下行：
$ ssh est@my_host 'cat /dev/zero' | pv > /dev/null
144kB 0:00:05 [ 121kB/s] [ <=> ]
上行：
$ yes | pv | ssh est@my_host "cat > /dev/null"
2.06MB 0:00:05 [1.96MB/s] [ <=> ]
测试本机IO能力：
$ pv /dev/zero > /dev/null
75.3GB 0:00:09 [8.56GB/s] [ <=> ]
其他技巧：
http://blog.urfix.com/9-tricks-pv-pipe-viewer/
 
pv allows a user to see the progress of data through a pipeline, by giving information such as time elapsed, percentage completed (with progress bar), current throughput rate, total data transferred, and ETA.
Here’s a nice list of cool ways you can use pv
1) SIMULATE TYPING
echo "You can simulate on-screen typing just like in the movies" | pv -qL 10
This will output the characters at 10 per second.
2) MONITOR PROGRESS OF A COMMANDpv access.log | gzip > access.log.gz

Pipe viewer is a terminal-based tool for monitoring the progress of data through a pipeline. It can be inserted into any normal pipeline between two processes to give a visual indication of how quickly data is passing through, how long it has taken, how near to completion it is, and an estimate of how long it will be until completion.
3) LIVE SSH NETWORK THROUGHPUT TESTyes | pv | ssh $host "cat > /dev/null"

connects to host via ssh and displays the live transfer speed, directing all transferred data to /dev/null
4) COPY WORKING DIRECTORY AND COMPRESS IT ON-THE-FLY WHILE SHOWING PROGRESStar -cf - . | pv -s $(du -sb . | awk '{print $1}') | gzip > out.tgz

What happens here is we tell tar to create “-c” an archive of all files in current dir “.” (recursively) and output the data to stdout “-f -”. Next we specify the size “-s” to pv of all files in current dir. The “du -sb . | awk ?{print $1}?” returns number of bytes in current dir, and it gets fed as “-s” parameter to pv. Next we gzip the whole content and output the result to out.tgz file. This way “pv” knows how much data is still left to be processed and shows us that it will take yet another 4 mins 49 secs to finish.
5) COPY A FILE USING PV AND WATCH ITS PROGRESSpv sourcefile > destfile
pv allows a user to see the progress of data through a pipeline, by giving information such as time elapsed, percentage completed (with progress bar), current throughput rate, total data transferred, and ETA. (man pv)
6) ANOTHER LIVE SSH NETWORK THROUGHPUT TESTpv /dev/zero|ssh $host 'cat > /dev/null'
connects to host via ssh and displays the live transfer speed, directing all transferred data to /dev/null
7) DD WITH PROGRESS BAR AND STATISTICS
sudo dd if=/dev/sdc bs=4096 | pv -s 2G | sudo dd bs=4096 of=~/USB_BLACK_BACKUP.IMG
This command utilizes ‘pv’ to show dd’s progress.
Notes on use with dd:
– dd block size (bs=…) is a widely debated command-line switch and should usually be between 1024 and 4096. You won’t see much performance improvements beyond 4096, but regardless of the block size, dd will transfer every bit of data.
– pv’s switch, ‘-s’ should be as close to the size of the data source as possible.
– dd’s out file, ‘of=…’ can be anything as the data within that file are the same regardless of the filename / extension.
8) [RE]VERIFY A DISC WITH VERY FRIENDLY OUTPUTdd if=/dev/cdrom | pv -s 700m | md5sum | tee test.md5
[re]verify those burned CD’s early and often – better safe than sorry -
at a bare minimum you need the good old `dd` and `md5sum` commands,
but why not throw in a super “user-friendly” progress gauge with the `pv` command -
adjust the “-s” “size” argument to your needs – 700 MB in this case,
and capture that checksum in a “test.md5″ file with `tee` – just in-case for near-future reference.
*uber-bonus* ability – positively identify those unlabeled mystery discs -
for extra credit, what disc was used for this sample output?
9) TIME HOW FAST THE COMPUTER READS FROM /DEV/ZEROpv /dev/zero > /dev/null
my stats 217GB 0:00:38 [4,36GB/s]


## softwares
pingviewinfo
winMTR