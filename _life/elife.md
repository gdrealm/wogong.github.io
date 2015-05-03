## information repo
1. gmail
2. google drive
2. evernote
3. pinboard
4. instapaper
4. wiki+blog+personal

## site
1. www.wogong.net  jekyll，托管于github
2. twitter.wogong.net URL 转发，利用Google Drive 进行托管，自动更新
3. read.wogong.net FarBox
4. log.wogong.net FarBox
5. [vps name].wogong.net 下载

## VPS
1. se 2015-07-18 ramnode 128M 80G 15$
    - se.wogong.net:9091 Transmission
    - vagex: php php5-curl
    - ss
2. ss 2016-02-04
    - cron: vagex;v2ex_daily
    - bingrewards
    - vagex
    - ss
    - chengzhen.me
3. sf digitalocean
    - ss

## proxy
1. vpnso (@cosbeta) ss+vpn+apnp
2. <vnet.link> AC+PAC
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
4. Photos

## sync & backup
1. PC
      - Documents + Music + Pictures 定期备份至移动硬盘 rsync
      - BTSync 备份 (MAIN)
      - Dropbox 本地IM记录
      - TrueCript 储存本地敏感资料，照片，文档
      - User Dir: vim/snippet
2. 网络信息
      - weibo 主动发布，豆瓣同步，多看阅读分享 ；
              通过 ifttt 至 Evernote，含 coco
      - Twitter 主动发布（尽量减少，慢慢转移至weibo），豆瓣同步，kindle分享；  
                自动归档至 Google Drive
      - Facebook Twitter分享，kindle分享；
                 很少主动发布信息，多为自动同步，基本不需备份
      - Douban 主动发布，标记；使用feedburner，处理豆瓣的RSS，设置。
               通过 ifttt 至 Evernote
      - Mail Gmail(backup to outlook, not any more 2014-10-18)
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
1. VPS : ar & la
2. thunder offline ivan member
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
3. AppleID 2-step verification


## Domain & DNS
wogong.net godaddy dnsimple
chengzhen.me namecheap dnsimple

dnsimple
  - wogong.net
  - chengzhen.me

## CDN
1. upyun
主机：v1.ftp.upyun.com (电信) v2.ftp.upyun.com (联通网通) v3.ftp.upyun.com (移动铁通) v0.ftp.upyun.com (自动判断
用户：操作员的用户名/空间名（需要两个同时填写）wogong/wogong-file
密码：操作员的密码
端口：21
文件传输协议：FTP
编码方式（字符集）：统一使用 UTF-8
 wogong-file.b0.upaiyun.com
 wogong-image.b0.upaiyun.com

2. qiniu
- Questions you should ask to yourself
1. What if you lose your phone/PC or any digital devices?
2. What about change a phone number？
