---
layout: wiki
title: dns
create: 1970-01-01
update: 2014-07-24
---
DNS: Domain Name Server

1. 如何测试DNS服务器：dig

    dig @166.111.8.28 wogong.net

2. dns cache remove

    # Windows
    ipconfig/flushdns
    net stop/start dnscache
    # MAC
    sudo killall -HUP mDNSResponder (for Lion & Mountain Lion)

## Tool
### dnsmasq
1. `/etc/dnsmasq.conf`

    conf-dir=/etc/dnsmasq.d

2. `/etc/dnsmasq.d/gfw.conf`

    #Google and Youtube
    server=/.google.com/127.0.0.1#1053
    server=/.google.com.hk/127.0.0.1#1053
    server=/.gstatic.com/127.0.0.1#1053
    server=/.ggpht.com/127.0.0.1#1053
    server=/.googleusercontent.com/127.0.0.1#1053
    server=/.appspot.com/127.0.0.1#1053
    server=/.googlecode.com/127.0.0.1#1053
    server=/.googleapis.com/127.0.0.1#1053
    server=/.gmail.com/127.0.0.1#1053
    server=/.google-analytics.com/127.0.0.1#1053
    server=/.youtube.com/127.0.0.1#1053
    server=/.googlevideo.com/127.0.0.1#1053
    server=/.youtube-nocookie.com/127.0.0.1#1053
    server=/.ytimg.com/127.0.0.1#1053
    server=/.blogspot.com/127.0.0.1#1053
    server=/.blogger.com/127.0.0.1#1053
    
    #FaceBook
    server=/.facebook.com/127.0.0.1#1053
    server=/.thefacebook.com/127.0.0.1#1053
    server=/.facebook.net/127.0.0.1#1053
    server=/.fbcdn.net/127.0.0.1#1053
    server=/.akamaihd.net/127.0.0.1#1053
    
    #Twitter
    server=/.twitter.com/127.0.0.1#1053
    server=/.t.co/127.0.0.1#1053
    server=/.bitly.com/127.0.0.1#1053
    server=/.twimg.com/127.0.0.1#1053
    server=/.tinypic.com/127.0.0.1#1053
    server=/.yfrog.com/127.0.0.1#1053


### pdnsd
1. `/etc/pdnsd.conf`

    # 这一段全局配置需要修改：
    
    global {
        # debug = on;          
        perm_cache=1024;
        cache_dir="/var/pdnsd";
        run_as="nobody";
        server_port = 1053;    # ！！！使用 1053 作为 dns 端口, 默认是 53，一定要修改否则会跟默认 dnsmasq 冲突
        server_ip = 127.0.0.1;  # 我们只需要处理本机转发的 DNS 查询，所以不需要更改
        status_ctl = on;
        query_method=tcp_only; # ！！！最重要的配置, 只使用 tcp 查询上级 dns
        min_ttl=15m;
        max_ttl=1w;
        timeout=10;
    }
    
    #……
    
    # 自行增加下面这一段，pdnsd 默认是没有提供上游 DNS 服务器的（默认配置文件中用各种注释方式把自带的……）：
    
    server {
        label= "googledns";           # 这个 label 随便写
        ip = 8.8.8.8; # 这里为上级 dns 的 ip 地址，要求必须支持 TCP 查询，相关说明见后文注解
        root_server = on;        # 设置为 on。
        uptest = none;           # 不去检测 dns 是否无效.
    }
            # …… 后面不需要修改的就不贴出来了。

## 相关参考资料
1. List of DNS record types: http://en.wikipedia.org/wiki/List_of_DNS_record_types
2. Domain Name System (DNS) Parameters: http://www.iana.org/assignments/dns-parameters/dns-parameters.xml
3. dig: http://www.zytrax.com/books/dns/ch10/dig.html

