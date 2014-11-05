---
layout: wiki
title: proxy
create: 2014-06-07
update: 2014-10-21
---
GFW 中国长城防火墙 Great Fire Wall

## 推荐方式
### 个人免费分享 ShadowSocks 帐号
1. Android  
下载 Shadowsocks 应用，添加配置，扫描二维码：  
![ssla](http://wogong-file.b0.upaiyun.com/ssla.png)
2. 桌面  
[配置文件](http://wogong-file.b0.upaiyun.com/ssla.json)
    - Windows
        - 32bit <http://dl.chenyufei.info/shadowsocks/shadowsocks-local-win32-1.1.1.zip>
        - 64bit <http://dl.chenyufei.info/shadowsocks/shadowsocks-local-win64-1.1.1.zip>
    - Other


### @cosbeta 提供的服务
* Shadowsocks + VPN +APNP
应网站要求不公布网址，目前使用其提供的shadowsocks，按年收费，价格便宜，自助服务。另有VPN，APNP等，多服务器，多协议。

### VnetLink 微林
* PAC + HTTP + AnyConnect
非常方便，价格便宜，按流量计费，亦可包月，价格便宜。
<https://vnet.link>
需要注册请联系我索要邀请码。
wogong2 MFM
wogong0 HYS
wogong4 尚有剩余流量
wogong1 0
wogong3 0
wogong5 0

日本  全局[全球用户]    node-jp.vnet.link:465
北美  全局[全球用户]    node-los.vnet.link:465
中国  全局[全球用户]    node-cnx.vnet.link:465
香港  全局[全球用户]    node-hk.vnet.link:465
日本  智能[中国用户]    node-jp.vnet.link:999
北美  智能[中国用户]    node-los.vnet.link:999
香港  智能[中国用户]    node-hk.vnet.link:999

### 曲径
* PAC
高端大气上档次，多平台支持，价格相比以上较为昂贵。尤其推荐其Android平台下的APP，一键无忧。
<http://getqujujing.com>

## 常用翻墙原理
1. shadowsocks
    1. PC 端有靠谱的软件，配合 Chrome 的 SwithchySharp 扩展使用。
    2. 移动端
       - Android Google Play 有 Shadowsocks 的应用，root后可以全局使用，智能切换，完全替代 VPN
       - iOS 也有应用，不过没有使用过。
2. ssh
3. VPN virtual private network
    1. PPTP/L2TP
    2. OpenVPN
    3. AnyConnect
4. APN
5. Hosts
6. IPv6+Hosts
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
5. 

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

