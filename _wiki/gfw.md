---
layout: wiki
title: proxy
create: 2014-06-07
update: 2014-06-15
---

GFW 中国长城防火墙 Great Fire Wall

## 推荐方式
### 免费分享 ShadowSocks 帐号
1. Android  
下载 Shadowsocks 应用，添加配置，扫描二维码：  
![ssla](http://wogong.qiniudn.com/wikissla.png)
2. 桌面  
[配置文件](http://wogong.qiniudn.com/wikissla.json)
    - Windows
        - 32bit <http://dl.chenyufei.info/shadowsocks/shadowsocks-local-win32-1.1.1.zip>
        - 64bit <http://dl.chenyufei.info/shadowsocks/shadowsocks-local-win64-1.1.1.zip>
    - Other


### ShadowSocks
1. PC 端有靠谱的软件，配合 Chrome 的 SwithchySharp 扩展使用。
2. 移动端
   - Android Google Play 有 Shadowsocks 的应用，root后可以全局使用，智能切换，完全替代 VPN
   - iOS 也有应用，不过没有使用过。

### PowerPAC
非常方便，价格便宜，速度有待考察
https://powerpac.in
使用我的推荐链接，免费获得256M流量：http://ppac.in/reg?r=118

## 常用翻墙方式
1. [[shadowsocks]]
2. ssh
3. VPN virtual private network
4. APN
5. Hosts
6. IPv6+Hosts
7. gae: goagent

## 辅助软件
1. Privoxy HTTP 127.0.0.1:8118
2. cow: https://github.com/cyfdecyf/cow
3. squid: 王者，配置复杂
4. polipo 简洁的HTTP代理，a caching web proxy  http://www.pps.univ-paris-diderot.fr/~jch/software/polipo/  
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


          
1. 要用 dnsmasq ，在 tomato 的 dnsmasq 自定义框内添加：

## Use ChinaDNS
server=127.0.0.1#5151
no-resolv
bogus-priv
domain-needed
filterwin2k
no-hosts
neg-ttl=3600

用这个方法，tomato dns 设定里面的 dns 服务器全部无效，自定义 host 文件也无效，完全保证从 chinadns 解析，要设置自己的 dns 就去 chainadns 命令行设置；

2. 用作者的转发脚本，要用到 REDIRECT 模块，有些 tomato 版本不带，或者带了也不自启动，对于后者，解决方法是在防火墙脚本加一句：

#load iptables REDIRECT moudel
[ $(lsmod | grep "ipt_REDIRECT" | wc -l) -eq 0 ] && modprobe ipt_REDIRECT

也可以改下转发命令：

iptables -t nat -A PREROUTING -p udp --dport 53 -j DNAT --to-destination 192.168.1.1:5353

其中 192.168.1.1 是你路由器地址，自己改。

http://www.v2ex.com/t/124550?p=1
