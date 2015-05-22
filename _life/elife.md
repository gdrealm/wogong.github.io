## information repo
1. Gmail
2. google drive
2. evernote
3. pinboard
4. instapaper (new to Pinboard; likes to Pinboard)
4. wiki+blog+life+items
5. log.wogong.net
6. read.wogong.net
7. Twitter (backup in Pinboard & Twitter archive)
8. Weibo (Kindle bot to Twitter)
9. iPhone Photos (Google+ Photos)
10. Calibre Libary
11. Wechat Public Account (Dogear.cn to Feedly to Pinboard)
12. Nike+ running

## site
1. www.wogong.net  jekyll，托管于github
2. twitter.wogong.net URL 转发，利用Google Drive 进行托管，自动更新
3. read.wogong.net FarBox
4. log.wogong.net FarBox
5. [vps name].wogong.net 下载

## VPS
1. se 2015-07-18 ramnode 128M 80G 15$
    - se.wogong.net:9091 Transmission
    - aria2c+yaaw
    - ss
2. ss 2016-02-04
    - cron: vagex;v2ex_daily
    - bingrewards
    - ss
    - chengzhen.me
3. sf digitalocean
    - ss
    - 

## proxy
1. vpnso (@cosbeta) ss+vpn+apnp
2. <vnet.link> AC+PAC
3. EDU Tsinghua  
    * VPN 只可以浏览校内资源
    * eproxy2 可以下载各种文献

## input
1. 现实
   书籍、讲座、课堂、聊天、新闻
2. 网络
      - RSS - feedly + press
      - 豆瓣, 知乎, V2EX
      - qzone, weibo, wechat
      - BBS
      - youtube youku bili
3. 其他
   各种资料、视频

## sync & backup
1. PC
      - Documents + Music + Pictures 定期备份至移动硬盘 rsync
      - BTSync 备份 (MAIN)
      - Dropbox 本地IM记录
      - TrueCript 储存本地敏感资料，照片，文档
      - User Dir: vim/snippet
2. network information
      - Twitter tweets; nike+ share; ifttt-douban; ifttt-blog; ifttt-weibo(kindle highlights) ==> archive to google drive
      - Facebook nike+ share
      - Weibo kindle highlights
      - Douban favorite ==> ifttt(feedburner to RSS) to Twitter
      - Wechat moments


## security
0. keepass
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

## CDN upyun
主机：
- v1.ftp.upyun.com (电信) 
- v2.ftp.upyun.com (联通网通) 
- v3.ftp.upyun.com (移动铁通) 
- v0.ftp.upyun.com (自动判断)
- 
用户：操作员的用户名/空间名（需要两个同时填写）wogong/wogong-file
密码：操作员的密码
端口：21
文件传输协议：FTP
编码方式（字符集）：统一使用 UTF-8
 
 file.wogong.net =>wogong-file.b0.upaiyun.com
 image.wogong.net =>wogong-image.b0.upaiyun.com