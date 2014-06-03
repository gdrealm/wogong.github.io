---
layout: wiki
title: gfw
---

# GFW 中国长城防火墙 Great Fire Wall

提供代购 VPN Shadowsocks 服务


## 我推荐的方式
### ShadowSocks

1. PC 端有靠谱的软件，配合 Chrome 的 SwithchySharp 扩展使用。
2. 移动端
   - Android Google Play 有 Shadowsocks 的应用，root后可以全局使用，智能切换，完全替代 VPN
   - iOS 也有应用，不过没有使用过。
3. 需要试用的可以联系我，个人现在使用的方案为每月10G流量，一年40RMB

### PowerPAC
非常方便，价格便宜，速度有待考察
https://powerpac.in
使用我的推荐链接，免费获得256M流量：http://powerpac.in/reg?r=118

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
3. squid
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
4. 
