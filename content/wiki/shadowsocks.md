---
title: shadowsocks
date: 2015-01-10
modified: 2015-06-18 08:07:12
---

由 @clowwindy 开发的轻量级服务器中转包传输工具。

## 项目
1. [shadowsocks](https://github.com/shadowsocks/shadowsocks)
    
    # debian
    apt-get install python-pip
    pip install shadowsocks
    # arch
    sudo pacman -S python2-pip
    sudo pip2 install shadowsocks

    sudo ssserver -c jp.json -d start --log-file /home/wogong/log/ssjp.log
    sudo ssserver -d stop

2. shadowsocks-libv  
   http://v2ex.com/t/68872
   目前 dd-wrt 上使用静态编译版本，使用良好。地址 http://dl.chenyufei.info/shadowsocks/
   raspberry pi 上使用需要自己按照 README 提示编译。

    sudo apt-get install build-essential autoconf libtool libssl-dev
    ./configure && make
    sudo make install
