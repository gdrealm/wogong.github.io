---
layout: wiki
title: elife
create: 2014-06-19
update: 2014-07-19
---

## site
4. www.wogong.net  
   jekyll，托管于github。update: VPS
1. case of images  
   Tumblr: <wogong.tumblr.com> nearly not update now for network reason.
1. ~~reader.wogong.net~~  
   源站 selfoss.wogong.net，采用orca CDN 分发。可以支持https，但是https与CDN冲突，目前舍弃https。
2. ~~twitter.wogong.net~~  
   dnspod 的显性URL 转发，利用Google Drive 进行托管，自动更新
3. ~~wiki.wogong.net~~  
   gollum，仓库在github。  
   采用nginx配置的反向代理。la.wogong.net:4567（默认值）
   已经取消，现在利用 pandoc 转化为静态文件托管在 github
   update: Jekyll Collection on VPS
5. ~~farbox~~
   一堆实验站点。
6. ~~stdyun~~
   免费静态空间。
7. ~~kindle.wogong.net~~  
   cops, 目前停用。

## VPS

   1. PT ipv6 download --  transmission
   2. Jekyll blog -- ruby,rvm,jekyll,nginx
   3. Download -- offline dir
   4. vagex -- php

1. la
      - la.wogong.net:9091 Transmission
      - dl.wogong.net Download Dir
2. ar
      - vagex 3 IP (ss proxy)

## proxy
1. vpnso (@cosbeta) ss
2. <pcnt.in>  <https://pcnt.in/mypac?id=118>
3. EDU Tsinghua  
    * VPN 只可以浏览校内资源
    * eproxy2 可以下载各种文献

## input
1. 现实
   书籍、讲座、课堂、聊天、新闻联播
2. 网络
      - RSS - feedly + press
      - 豆瓣, 知乎, V2EX
      - qzone, weibo, wechat
      - BBS
      - youtube youku bili
3. 其他
   各种资料、视频

## output
1. wiki
2. blog
3. Social Networks (need back up, you know, never trust any commercial companies)
4. Photos 来自手机，touch，他人所拍；统一文件夹整理，上传flickr存档，少许朋友圈分享

## sync & backup
1. PC
      - Documents + Music + Pictures 定期备份至移动硬盘 rsync
      - BTSync 备份 (MAIN)
      - Dropbox 本地IM记录
      - TrueCript 储存本地敏感资料，照片，文档
      - User Dir: vim/snippet
      - 
2. 网络信息
      - weibo 主动发布，豆瓣同步，多看阅读分享  ；
              通过 ifttt 至 Evernote，含 coco
      - Twitter 主动发布（尽量减少，慢慢转移至weibo），豆瓣同步，kindle分享；  
                自动归档至 Google Drive
      - Facebook Twitter分享，kindle分享；   
                 很少主动发布信息，多为自动同步，基本不需备份
      - Douban 主动发布，标记；  
               通过 ifttt 至 Evernote 
      - Mail Gmail(backup to outlook)
      - LastPass 
      - KEY change periodically
3. Mobile
      - SMS SMS backup+ to Gmail ; SMS to Text to csv file
      - 随手记 定期备份至SD
      - call log SMS backup+ to Gmail and Google Calendar
      - Apps Ti backup

## cloud
快盘：分享文件
vdisk：分享文件
百度网盘：共享速度快
115：分享文件
dbank：各种分享文件，速度不错
Google drive：kindle书籍仓库+往期课程文件+各种备份文件+GMail attachments

## download

1. -> VPS : ar & la
then to Internet cafe download to local disk.
3. Baidu Pan & 115

## security
0. lastpass
   - 1password 数据存储在本地，有手机客户端
   - lastpass 数据存储在服务器
   - Keepass
   - Enpass
1. Google Authenticator
    - Dropbox
    - Microsoft
    - Evernote
    - Github
    - Google
    - Lastpass
2. Truecrypt

## finance
随手记

android 自动导出到 SD

记账原则：
1. 旅行什么的按照项目记账
2. 代付借贷什么的按照实际来
