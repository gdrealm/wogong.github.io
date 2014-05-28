---
layout: wiki
title: dns
---

# DNS: Domain Name Server

目前使用[[DNSpod|http://dnspod.cn]], 推荐。

如何测试DNS服务器：dig

    dig @166.111.8.28 wogong.net

## 清除DNS缓存

1. Windows

        ipconfig/flushdns
        net stop/start dnscache

2. Mac

        sudo killall -HUP mDNSResponder (for Lion & Mountain Lion)

## 相关参考资料
1. List of DNS record types: http://en.wikipedia.org/wiki/List_of_DNS_record_types
2. Domain Name System (DNS) Parameters: http://www.iana.org/assignments/dns-parameters/dns-parameters.xml
3. dig: http://www.zytrax.com/books/dns/ch10/dig.html