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
      - Douban 主动发布，标记；使用feedburner，处理豆瓣的RSS，设置。
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

# SNS 社交网络

SNS总是希望扩张扩大其用户量的，校内改为人人就是。但是圈子这个问题肯定是存在的，QQ空间就很明显。我是讨厌这些SNS社区的，倒不是信息过载，而是信息碎片化，有用的没有多少，还浪费时间，当然，把SNS当做与朋友交流的地方就OK，没必要想着在这里学到什么~

1. Qzone  
最早接触QQ是高一，算是晚的了。我对QQ空间的热情持续了多久呢？从懒得写日志，懒得看别人的空间开始。两三年而已。
以前会很爱看别人写的东西，发的状态，想象他人在干嘛，他们的生活中愉快的和不愉快的，只要简单瞅瞅。那段时间，博客这么一个东西刚出来，空间与博客齐舞，再后来，人人热起来了，直到现在的微博。中国的互联网还是很精彩的，亦步亦趋的跟着国际潮流，十几亿的人口足以让这些产品不去担忧没有用户群。现在的我，用得最多的有QQ，IM基本就是他，虽然各种和谐不稳定，各种捆绑强迫，但也认了，这一点需要感谢马化腾。这是典型的点对点交流工具，QQ群很少使用，暂且不计在内吧。类似的工具也有很多，中国市场就是一堆。不废话了，简单说自己的想法吧。
2. RENREN
人人注销啦，虽然不知道几个人可以看到，还是说下想念这片留下我四年故事的地方，酸甜苦辣，有轻狂无知，有失去有收获。最后一次，我明白一切欠下的、压抑的，必将归还、爆发。一切错误的，必将有苦果。i#wogong  
10-19
   - 查看非好友的状态：http://www.renren.com/360252396#//status/status?id=xxxxx
   - 
3. DouBan
阅读、音乐、电影
4. Weibo
daily life. 密友圈e，身边的同学大多在这里。
5. Twitter
daiyly life. 偏吐槽，技术。豆瓣信息通过 RSS 同步到这里
6. Facebook
与 Twitter 同步。偶尔看看朋友们的消息。
7. LinkedIn
职场社交。
8. 微信朋友圈
daily life. 隐私不错，多为熟人。
9. Google+
很少去了。