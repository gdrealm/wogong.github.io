# WOGONG

## site
1. ~~[reader.wogong.net](reader.wogong.net)~~  
   源站 selfoss.wogong.net，采用orca CDN 分发。可以支持https，但是https与CDN冲突，目前舍弃https。
2. [twitter.wogong.net](twitter.wogong.net)  
   dnspod 的显性URL 转发，利用Google Drive 进行托管，自动更新
3. [wiki.wogong.net](wiki.wogong.net)  
   gollum，仓库在github。  
   采用nginx配置的反向代理。la.wogong.net:4567（默认值）
   已经取消，现在利用 pandoc 转化为静态文件托管在 github
4. www.wogong.net  
   jekyll，托管于github。
5. ~~farbox~~
   一堆实验站点。
6. ~~stdyun~~
   免费静态空间。
7. ~~kindle.wogong.net~~  
   cops, 目前停用。

## VPS
   1. la
      - la.wogong.net:9091 Transmission
      - dl.wogong.net Download Dir
   2. arizona
      - wiki.wogonog.net `wiki` 301 to `wogong.net`
      - vagex 3 IP (ss proxy)
## Proxy
    1. vpnso (@cosbeta) ss
    2. powerpac.in


## input
   1. 现实
   书籍、讲座、课堂、聊天、新闻联播
   2. 网络
      - RSS - feedly + press
      - 豆瓣, 知乎, V2EX
      - qzone, weibo, weixin
      - BBS
      - youku bili
   3. 其他
   各种资料、视频

## output
   1. wiki
   2. blog
   3. Social Networks (need back up, you know, never trust any commercial companys)
   4. Photos 来自手机，touch，他人所拍；统一文件夹整理，上传flickr存档，少许朋友圈分享


## Sync & Backup
   1. PC
      - Documents + Music + Pictures 定期备份至移动硬盘
      - BTSync 备份

   2. 网络信息
      - weibo 主动发布，豆瓣同步，多看阅读分享  ；
              通过 ifttt 至 Evernote，含 coco
      - Twitter 主动发布（尽量减少，慢慢转移至weibo），豆瓣同步，kindle分享；  
                自动归档至 Google Drive
      - Facebook Twitter分享，kindle分享；   
                 很少主动发布信息，多为自动同步，基本不需备份
      - Douban 主动发布，标记；  
               通过 ifttt 至 Evernote, 含 coco (印象笔记)
   3. Mobile
      - SMS SMS backup+ to Gmail ; SMS to Text to csv file
      - 随手记 定期备份至SD
      - call log SMS backup+ to Gmail and Google Calendar
      - Apps Ti backup


## Security
1. 云：Dropbox
   同步即时通讯聊天记录等
2. 本地：[[rsync]]
   定期同步 Pictures, Music, Books 到移动硬盘。
3. TrueCript
   储存本地敏感资料，照片，文档
4. Lastpass
   密码管理，一站式
5. 密钥
   定期更换密钥对



## Temp OR outdated

移动设备：

目前的想法是手机+平板
鉴于严重依赖google且本人暂时并无归顺apple的的想法和经济实力
且jobs之后的apple一系列行为等等原因，还是选用android。
平板可以考虑nexus7.7，手机可以考虑nexus5


cloud
dropbox：在用课程资料文件+各种备份小文件+calibre书库
目前主要采用dropbox和百度网盘。


快盘：分享文件
vdisk：新浪分享文件
百度网盘：共享速度快
115：新浪分享文件
dbank：各种分享文件，速度不错
Google drive：kindle书籍仓库+往期课程文件+各种备份文件

Blog
vimwiki结合github发布
evernote作为资源收集，wiki整理发布
真心可以使用EN写博客，输出为html格式，发布到github上！
现在使用jekyll啦，感觉很不错


MAIL
gmail主力邮箱，收取其他所有邮件
hotmail备份邮箱，备份所有邮件；难道没有发现自己发送的邮件按照目前这种方式没有办法备份么？应该可以设置过滤器转发吧，但是这又这个必要么。思考思考
主用wogong38账号，不再更改。辅助chengzhen1991和i@wogong.net




weibo：移动端收藏，或者通过发邮件选择evernote保存到en中。
（可以考虑如果云同步，获得邀请之后）

twitter：favorate，自动同步到en

facebook
人人：检查人人的收藏，保证挑出有价值的于EN备份





PS：
很多事情可以听听知乎的建议，当然之前一定要Google


代理：
清华的alef，校园网，ipv6
homezz的ssh，美国，ipv6
google的gae，美国，ipv6


不需要自动化操作evernote的标签或者笔记本，通过ifttt，每次从gr中收集到的东西应该手动整理消化

电影书籍音乐之类应该配合豆瓣

instapaper liked 自动发送到evernote
想要全文收集instapaper的方法，很简单，强制全文RSS，将链接转化为网页，但是这样的问题是臃肿了订阅！！！
怎么解决呢？手动？？还是以后统计instapaper 的来源，使得其与gr的重合度更高？

再考虑吧

outlook邮箱接收各种邮箱备份！分类规则方便日后查找。大容量就是好


知乎以及quora的每周精选 保存到Evernote
gr星标文章通过邮件保存到这里

