---
layout: wiki
title: proxy
create: 2014-06-07
update: 2014-11-07
---
本指南提供科学上网服务指导。

## 相关概念
1. 防火长城（英语：Great Firewall of China，常用简称：GFW，中文也称中国国家防火墙或防火长城。），是对中国政府在其互联网边界审查系统（包括相关行政审查系统）的统称。
2. 服务器  
    一般指提供特定服务的主机，你所访问的任何网页实际上都托管在服务器上。
3. 代理服务器
    科学上网最普遍的方式是通过第三方未被封禁的境外服务器进行访问，此服务器即称为代理服务器。


## 推荐付费服务

### @cosbeta 提供的服务
* Shadowsocks + VPN +APNP
应网站要求不公布网址，目前使用其提供的shadowsocks，按年收费，价格便宜，自助服务。另有VPN，APNP等，多服务器，多协议。

### VnetLink 微林
* HTTP
非常方便，价格便宜，按流量计费，亦可包月，价格便宜。
<https://vnet.link>
需要注册请联系我索要邀请码。

### 曲径
* PAC
高端大气上档次，多平台支持，价格相比以上较为昂贵。尤其推荐其Android平台下的APP，一键无忧。
<http://getqujujing.com>

## 常用方式
1. shadowsocks
    1. PC 端有靠谱的客户端，配合 Chrome 的 SwithchyOmega 扩展使用。
    2. 移动端
       - Android Google Play 有 Shadowsocks 的应用，不需ROOT，智能切换，完全替代 VPN
       - iOS 也有应用，需要越狱。
3. HTTP or HTTPS proxy
3. VPN virtual private network
    1. PPTP/L2TP
    2. OpenVPN
    3. AnyConnect
4.ssh
5. Hosts
7. gae: goagent

## 辅助软件
1. Privoxy HTTP 127.0.0.1:8118
2. cow: https://github.com/cyfdecyf/cow
3. squid: 王者，配置复杂
4. polipo 简洁的HTTP代理，a caching web proxy  Polipo is a caching web proxy designed to be used as a personal cache or a cache shared among a few users. http://www.pps.univ-paris-diderot.fr/~jch/software/polipo/  
   - 配置文件

            authCredentials = "username:passwd" # 基本的HTTP认证
            socksParentProxy = "127.0.0.1:7070" # 设置透明代理
            socksProxyType = socks5
   - Manual http://www.pps.univ-paris-diderot.fr/~jch/software/polipo/polipo.html#Top 

## 项目
1. gfwlist
2. smarthost
3. autovpn
4. chnroutes
4. ChinaDNS
    - windows: dnsrelsy.exe -s 192.168.1.1,8.8.8.8
    - openwrt /etc/init.d/chinadns
      add -s 127.0.0.1,8.8.8.8 \
    - RP 配合以下的
          sudo src/chinadns -l ~/ChinaDNS-C-1.1.4/iplist.txt -s 192.168.1.1,208.67.222.222,8.8.8.8 -p 5151
    - 要用 dnsmasq ，dnsmasq 配置：(<http://www.v2ex.com/t/124550?p=1>)

            ## Use ChinaDNS
            server=127.0.0.1#5151
            no-resolv
            bogus-priv
            domain-needed
            filterwin2k
            no-hosts
            neg-ttl=3600

    - OpenWRT

    >opkg install ChinaDNS-C_1.x.x_ar71xx.ipk
    >/etc/init.d/chinadns start
    >(Optional) We strongly recommend you to set ChinaDNS as a upstream >DNS server for dnsmasq instead of using ChinaDNS directly:
    >
    >Run /etc/init.d/chinadns stop
    >Remove the 2 lines containing iptables in /etc/init.d/chinadns.
    >Update /etc/dnsmasq.conf to use only 127.0.0.1#5353:
    >
    >no-resolv
    >server=127.0.0.1#5353
    >Restart chinadns and dnsmasq


5. gfwlist2pac <https://github.com/clowwindy/gfwlist2pac>
gfwlist2pac -f pac -p "SOCKS5 127.0.0.1:8080; SOCKS 127.0.0.1:8080; HTTPS node-cnx.vnet.link:111; PROXY node-cnx.vnet.link:110; DIRECT;" --user-rule user_rule.txt

