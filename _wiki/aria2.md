---
layout: wiki
title: aria2
date: 2015-03-17
---

## Note
1. Windows 下使用 VBS 建立开机启动脚本 http://bbs.kafan.cn/thread-1686205-1-1.html

Successfully connected to Aria2 through remote RPC, however the connection is still insecure. For complete security try adding an authorization secret token while starting Aria2 (through the flag --rpc-secret)

aria2c --all-proxy=http://proxy:8080 http://host/file

aria2c --http-auth-challenge=true http://username:passwd@dl.wogong.net/MIT/MITRES2_002S10linear_lec01_300k.mp4

http://www.archive.org/download/MITRES2_002S10nonlinear/MITRES2_002S10nonlinear_lec01_300k.mp4

You can avoid this error by specifying CA certificate file using --ca-certificate option. If you are using Debian/Ubuntu, first install ca-certificates and give --ca-certificate=/etc/ssl/certs/ca-certificates.crt to aria2c. This is the proper and secure way.
There is another insecure way to avoid this error. Just give --check-certificate=false to aria2c.
This is easier than previous one, but it is insecure because it does not verify remote server.


aria2c -i list.txt

## project
1. [BaiduExporter](https://github.com/acgotaku/BaiduExporter)
2. [YAAW](https://github.com/binux/yaaw)
