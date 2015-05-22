---
layout: wiki
title: iptable
create: 2015-05-06
update: 2015-05-06
---

 KiwiVM has blocked port 8080 in your server by adding the following iptables rule:

    iptables -I INPUT -p tcp --destination-port 8080 -j DROP
	
	


iptables简介

iptables是基于内核的防火墙，功能非常强大，iptables内置了filter，nat和mangle三张表。

filter负责过滤数据包，包括的规则链有，input，output和forward；

nat则涉及到网络地址转换，包括的规则链有，prerouting，postrouting和output；

mangle表则主要应用在修改数据包内容上，用来做流量整形的，默认的规则链有：INPUT，OUTPUT，NAT，POSTROUTING，PREROUTING；

input匹配目的IP是本机的数据包，forward匹配流经本机的数据包，prerouting用来修改目的地址用来做DNAT，postrouting用来修改源地址用来做SNAT。

iptables主要参数

-A 向规则链中添加一条规则，默认被添加到末尾

-T指定要操作的表，默认是filter

-D从规则链中删除规则，可以指定序号或者匹配的规则来删除

-R进行规则替换

-I插入一条规则，默认被插入到首部

-F清空所选的链，重启后恢复

-N新建用户自定义的规则链

-X删除用户自定义的规则链

-p用来指定协议可以是tcp，udp，icmp等也可以是数字的协议号，

-s指定源地址

-d指定目的地址

-i进入接口

-o流出接口

-j采取的动作，accept，drop，snat，dnat，masquerade

--sport源端口

--dport目的端口，端口必须和协议一起来配合使用

注意：所有链名必须大写，表明必须小写，动作必须大写，匹配必须小写


## openwrt 屏蔽指定IP

root@OpenWrt:~# iptables -A INPUT -s 192.168.2.146 -j DROP
root@OpenWrt:~# iptables -A OUTPUT -s 192.168.2.146 -j DROP
root@OpenWrt:~# iptables -I INPUT -s 192.168.2.146 -j DROP
root@OpenWrt:~# iptables -I OUTPUT -s 192.168.2.146 -j DROP
root@OpenWrt:~# iptables -I FORWARD -s 192.168.2.146 -j DROP



## temp

1、安装iptables防火墙
CentOS执行：yum install iptables
Debian/Ubuntu执行：apt-get install iptables

2、清除已有iptables规则
 

iptables -F
iptables -X
iptables -Z
3、开放指定的端口
 

#允许本地回环接口(即运行本机访问本机)
iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT
# 允许已建立的或相关连的通行
iptables -A INPUT -m state –state ESTABLISHED,RELATED -j ACCEPT
#允许所有本机向外的访问
iptables -A OUTPUT -j ACCEPT
# 允许访问22端口
iptables -A INPUT -p tcp –dport 22 -j ACCEPT
#允许访问80端口
iptables -A INPUT -p tcp –dport 80 -j ACCEPT
#允许FTP服务的21和20端口
iptables -A INPUT -p tcp –dport 21 -j ACCEPT
iptables -A INPUT -p tcp –dport 20 -j ACCEPT
#如果有其他端口的话，规则也类似，稍微修改上述语句就行
#禁止其他未允许的规则访问
iptables -A INPUT -j REJECT
iptables -A FORWARD -j REJECT
4、屏蔽IP
 

#如果只是想屏蔽IP的话3、“开放指定的端口”可以直接跳过。
#屏蔽单个IP
iptables -I INPUT -s 123.45.6.7 -j DROP
#封整个段即从123.0.0.1到123.255.255.254的命令
iptables -I INPUT -s 123.0.0.0/8 -j DROP
#封IP段即从123.45.0.1到123.45.255.254的命令
iptables -I INPUT -s 124.45.0.0/16 -j DROP
#封IP段即从123.45.6.1到123.45.6.254
iptables -I INPUT -s 123.45.6.0/24 -j DROP
5、查看已添加的iptables规则
 

iptables -L -n
 
v：显示详细信息，包括每条规则的匹配包数量和匹配字节数
x：在 v 的基础上，禁止自动单位换算（K、M）
n：只显示IP地址和端口号，不将ip解析为域名

6、删除已添加的iptables规则
 将所有iptables以序号标记显示，执行：
 

iptables -L -n –line-numbers
 
比如要删除INPUT里序号为1的规则，执行：
 

iptables -D INPUT 1
7、iptables的开机启动及规则保存
 

chkconfig –level 345 iptables on
 
CentOS上可以执行：service iptables save保存规则

linux下iptables封ip段的常见命令：
封单个IP：
 

iptables -I INPUT -s 211.1.0.0 -j DROP
封IP段：
 

iptables -I INPUT -s 211.1.0.0/16 -j DROP
iptables -I INPUT -s 211.2.0.0/16 -j DROP
iptables -I INPUT -s 211.3.0.0/16 -j DROP
封整个段：
 

iptables -I INPUT -s 211.0.0.0/8 -j DROP
封几个段：
 

iptables -I INPUT -s 61.37.80.0/24 -j DROP
iptables -I INPUT -s 61.37.81.0/24 -j DROP
解封：
 

iptables -D INPUT -s IP地址 -j REJECT
iptables -F 全清掉了
关闭： 
 

/etc/rc.d/init.d/iptables stop
 
启动： 
 

/etc/rc.d/init.d/iptables start
 
重启：
 

/etc/rc.d/init.d/iptables restart
1、重启后生效
 

开启：chkconfig iptables on
关闭：chkconfig iptables off
2、即时生效，重启后失效
 

开启：service iptables start
关闭：service iptables stop