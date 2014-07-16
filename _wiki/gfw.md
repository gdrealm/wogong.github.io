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
![ssla](http://wogong.qiniudn.com/ssla.png)
2. 桌面  
[配置文件](http://wogong.qiniudn.com/ssla.json)
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
