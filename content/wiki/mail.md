---
title: mail
date: 2015-06-17
modified: 2015-09-09 00:35:52
---


Fastmail 使用 Gmail 账户身份，个人邮件先不设置了。


## 邮件服务器设置

=== MX记录 ===

规范的MX记录应当由主域解析出一个主机名（如mta.jefflei.com），再由此主机名解析出一个或多个IP地址（如 211.99.189.87和211.99.189.88），而不能直接由主域解析出一个IP地址，直接由MX记录解析出IP会被一些MTA认为是垃圾邮件。而且，主域解析出的主机名不应当同主域名相同。

    host -t mx wogong.net
    dig -t mx wogong.net

=== PTR记录 ===

域名反向解析(RDNS)是一种常见反垃圾邮件的功能，现在要需要检查IP反向解析(PTR)记录的邮件服务器越来越多，尤其是国外的邮件服务器（例如：AOL），很多时候被对方拒绝被退信，都是因为没有反向解析造成的。 国内的 sina 邮件系统有这个要求，如果没有反向解析的ip发信到 sina.com, 可能会返还以下的错误代码：
错误代码：450 4.7.1 Client host rejected: cannot find your hostname [IP ]
错误原因：对方服务器未设置反向解析

什么是域名反向解析？

其实作过DNS服务器的朋友一定会知道DNS服务器里有两个区域，即“正向查找区域”和“反向查找区域”，反向查找区域即是这里所说的IP反向解析，它的作用就是通过查询IP地址的PTR记录来得到该IP地址指向的域名，当然，要成功得到域名就必需要有该IP地址的PTR记录。 

如何做反向解析？

找你的上网线路(固定IP)提供商(ISP)，比如：中国电信，中国联通，中国移动等。不是找域名注册商，需要找提供IP给你的部门，托管服务器的一般联系机房管理员。 一般省级电信运营商可以做。 

如何查询反向解析记录？

使用nslookup命令来查询PRT记录，如：
  nslookup -qt=prt 202.108.3.184
这个IP是 sina 的邮件主机，查询结果是：
    184.3.108.202.in-addr.arpa name = mail3-184.sinamail.sina.com.cn. 

如果IP没有反向解析，一般返回：
    ** server can't find 65.20.211.58.in-addr.arpa: NXDOMAIN 

反向解析需要收费吗？

这个根据当地的ISP而定，有免费的，也有收费的，而且费用不一。一般是按年或是按月的收费方式。

Winmail 邮件系统里有多个域名，使用的是同一个IP，我需要为每一个域建一个PTR吗？

一般只需要针对主域（EHLO域）进行反向解析就可以了。理论上一个IP可以做多条 PTR 记录的。

做那个Ip的反向解析？

做出口的公网Ip。由于线路原因有多个出口Ip的，几个Ip都要做反向解析。

反向解析指向什么？

假如你的主域名是 abc.com, 一般指向 mail.abc.com, 必须保证 mail.abc.com 有正向的 A 记录指向（在域名注册商系统里做）。
你可以将 Winmail 里 "SMTP 设置" 的 "HELO/EHLO、主机名" 设置成 mail.abc.com，这样比较规范。

动态IP可以做反解解析吗？

不能。 

做了IP反向解析（RDNS）就能够解决所有邮件外发退信的问题吗？

这个是规范性设置，会改善外发退信问题。退信原因很多，做了反向解析也无法保证解决所有的外发退信问题。 
    

=== DKIM设置 ===

1. 简介
DomainKeys Identified Mail，其主要的原理通俗的说，就是在发送邮件的时候通过私钥在邮件头写一段加密信息，然后公钥放到DNS服务器上，邮件的接收方通过邮件头的加密信息来和DNS上的公钥比对来判定邮件来源是否合法。

2. 配置

 * 安装软件包 opendkim

 *  生成公钥私钥对：opendkim-genkey -r -d mail.wogong.net

 * 添加DNS记录：

- 主机记录：default._domainkey.mail.wogong.net
- 记录类型：txt
- 值："v=DKIM1,p=....."(来自default.txt)

 * opendkim.conf文件

opendkim.conf:
	
	\# Log to syslog
    Syslog                  yes
    \# Required to use local socket with MTAs that access the socket as a non-
    \# privileged user (e.g. Postfix)
    UMask                   002
    \# Sign for example.com with key in /etc/mail/dkim.key using
    \# selector '2007' (e.g. 2007._domainkey.example.com)
    \# 避免signature问题
    Domain                  *
    \# 放置私钥的位置
    KeyFile                 /var/db/dkim/default.private
    Selector                default
    Canonicalization        relaxed/simple
    X-Header yes  
    Socket inet:9999@localhost


 * /etc/postfix/main.cf添加以下配置
    smtpd_milters= inet:localhost:9999
    milter_default_action = accept
    milter_protocol = 2
    non_smtpd_milters = inet:localhost:9999

 *  重启opendkim和postfix

sudo vim dkim/trusted 添加允许签名的地址

sudo service opendkim restart

sudo postfix reload

=== 验证 ===

1. Gmail: 查看邮件原始信息

2. 工具网站

然后验证吧：[http://dkimcore.org/tools/](http://dkimcore.org/tools/)

Check a published DKIM Core Key：

* Selector：default
* Domain name：mail.quanlei.com

接着再发邮件到gmail和hotmail中查看dkim是否有签名。

=== 参考链接 ===

1. https://help.ubuntu.com/community/Postfix/DKIM
2. http://lists.opendkim.org/archive/opendkim/users/2010/03/0162.html
3. http://stevejenkins.com/blog/2010/09/how-to-get-dkim-domainkeys-identified-mail-working-on-centos-5-5-and-postfix-using-opendkim/

== SPF设置 ==

=== 简介 ===
SPF是指Sender Policy Framework，是为了防范垃圾邮件而提出来的一种DNS记录类型，SPF是一种TXT类型的记录。SPF记录的本质，就是向收件人宣告：本域名的邮件从清单上所列IP发出的都是合法邮件，并非冒充的垃圾邮件。

=== 查看SPF ===

1. windows 
    nslookup -type=txt wogong.net

2. linux
    dig -t txt wogong.net

=== 记录解析 ===

我们看这条SPF:

	yourdomain.com "v=spf1 a mx mx:mail.jefflei.com ip4:202.96.88.88 ~all"

这条SPF记录具体的说明了允许发送 @yourdomain.com 的IP地址是：

a （这个a是指 yourdomain.com 解析出来的IP地址，若没有配置应取消）

mx （yourdomain.com 对应的mx，即 mail.yourdomain.com的A记录所对应的ip）

mx:mail.jefflei.com （如果没有配置过mail.jefflei.com这条MX记录也应取消）

ip4:202.96.88.88 （直接就是 202.152.186.85 这个IP地址）

其他还有些语法如下：

* "-" Fail, 表示没有其他任何匹配发生
* "~" 代表软失败，通常用于测试中
* "?" 代表忽略

如果外发的ip不止一个，那么必须要包含多个

	v=spf1 ip4:202.96.88.88 ip4:202.96.88.87 ~all

=== 测试 ===

1.Gmail等邮箱

设置好DNS中的SPF记录后，发送邮件给自己的gmail，然后查看邮件的源文件，应该能看到类似的邮件头，其中有pass表示设置成功。

    Received-SPF: pass (google.com: domain of test@jefflei.com designates 202.96.88.87 as permitted sender) client-ip=202.96.88.87;
2. 测试网站

http://www.kitterman.com/spf/validate.html

=== 参考资料 ===

1. http://www.openspf.org/SPF_Record_Syntax
2. http://www.openspf.org/Specifications



== Spam ==


在自建邮件服务器之前，先检查下你所要使用的IP的信用度如何？如果你的IP已经在垃圾邮件联盟的黑名单里面，那么建议别用了，因为被当做垃圾邮件的概率会非常高。
可以点下面的链接查看：
http://cbl.abuseat.org/lookup.cgi
http://www.spamhaus.org/query/bl?ip=8.8.8.8
http://anti-spam.org.cn/


1. Hotmail
错误信息：
http://mail.live.com/mail/troubleshooting.aspx#errors

申诉：

2. Gmail
群发邮件发件人指南
https://support.google.com/mail/answer/81126


== 参考文章 ==

1. [Ubuntu下安装Postfix，配置DKIM，SPR，SMTP服务](http://www.quanlei.com/2012/06/3148.html)
2. [如何做邮件服务器的IP反向解析](http://dagai.net/archives/1076)
----

## extmail
使用extmail已经两年了，一直挺稳定，但最近经常页面打不开，用其他客户端收邮件没问题，查了LOG发现报错如下：

Thu Jun 24 09:14:54 2010] [error] [client 192.168.3.34] (104)Connection reset by peer: FastCGI: comm with server "/usr/bin/dispatch.fcgi" aborted: read failed [Thu Jun 24 09:14:54 2010] [error] [client 192.168.3.34] FastCGI: incomplete headers (0 bytes) received from server "/usr/bin/dispatch.fcgi"

之后/var/www/extsuite/extmail/dispatch-init restart 到是可以了，但是隔一段时间，还是会出现上述故障 请问有解决的办法吗？总不能每次都手动重启吧！ 说明一下，之前没有改任何配置
