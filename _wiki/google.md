---
layout: wiki
title: google
create: 2014-08-28
update: 2014-08-28
---



- 提供单词读音的API,获取Google Translate发音的方法：

Google的发音是通过http请求实现，实现方法如下：
    http://translate.google.com/translate_tts?tl=en&q=text
此链接将返回"text"发音的MP3文件。根据这一功能，至少可以开发出在线发音的单词查询软件。

- 关于Google Voice的注册：
虽然现在开放注册，但是只有在美国加拿大地区才能注册Voice Number，这点需要注意。只要使用美国的IP登陆voice主页，便会看到获取voice number的选项。之后注册最大的困难是美国的电话认证。之前我放弃的原因也就是因为这个，但是没想到网络上居然提供这种服务，虚拟的VoIp电话，实在是令我惊讶，联系到昨天发现的另外一个网站，提供各国虚拟人物身份的网站，资料俱全，包括信用卡号，社保卡号，真是无所不能的网络。

- 关于同步Twitter到Google+：
Google+开放这么长时间，还是没有开放API的意思，这是Google的战略所在，后来的社交网站的确应该考虑到这个方面，如果开放了API，现在Google+上可能就是一堆bot了，but，最讨厌的就是这个but了，Google总是要开放的吧？这个拭目以待。<br />
正是由于不开放API，导致了同步的困难大大提高，但也不是没有办法的，之前在ifttt上看到过几个这样的recipe，不过都大同小异，主要是利用Gogole Voice的SMS功能发布，由于刚刚解决了Google Voice的注册问题，所以顺便搞定了这个同步的事情。虽然有点对不起Google+，但是Google应该不会介意吧？哈哈<br />
预祝Google+成功啦，本人都不怎么fb的！

- gtalk
我只能说，ifttt配合gtalk简直碉堡了！尤其是在我发现freetalk这种神器之后。哈哈哈哈哈，赶紧复习。。呜呜，折腾好久了。。

- site
Google工具的使用，包括：
* Google Analitic
* Google Webmaster Tool
* Google Adsense
and so on...

- gae
gae搭建gtap访问twitter
1.gae使用见主页。

2.gtap项目地址：http://code.google.com/p/gtap/。

3.创建twitter api
点击“register an app”就到了创建新应用的页面“Register an Application”要填写的内容如下：
Application Name:<这里填写的内容将来会作为“via 小狗狗”来显示，英文汉字符号都可以>
Description:<描述>
Application Website:<这里填写的地址是“小狗狗”的链接。>
Organization:<随便写，不重要，我用字母写的>
Application Type:<选择Browser即可>
Callback URL:<地址随便,但是必须写>
Default Access type:<这里选择Read & Write即可>
Application Icon:<上传个图片吧，会个性点，当然是给自己看的，别人看到了没好处>
4.设置客户端。

= windows系统设置gmail取代outlook =
允许用户安装 Microsoft Windows 桌面访问点，从而快速访问 Google 文档、Google 日历和 Gmail（已预先配置为可供域中的帐户使用）。这些应用将在一个简化的谷歌浏览器窗口中启动。此更新还允许用户将 Gmail 设置为自己的默认电子邮件程序。
请点击[[http://dl.google.com/tag/s/ap=wogong.net/googlewebapps/en/googleappsstandalonesetuptagged.exe|此处]]下载这些功能。


= 文字格式 =
通过一些符号组合可以为信息文本加入如粗体、斜体、删除线等格式。这是个从 Gtalk 开始就被传来传去的技巧，但还是很多人在问，具体方法如下：
粗体：在文字的两边加\*，即 *粗体*
斜体：在文字的两边加\_，即 _斜体_
删除线：在文字的两边加-，即 -删除线-
需要注意的是：删除线对于中文支持不好，纯中文是无法显示出删除线的，可以在中文字间添加空格；另外，这些符号也需要在半角英文状态下打出。
http://lucifr.com/2011/07/03/some-things-you-dont-know-about-google-plus/


请求移除敏感信息: https://www.google.com/webmasters/tools/removals?hl=en

## gmail
1. 高级搜搜功能：http://support.google.com/mail/bin/answer.py?hl=zh-Hans&hlrm=en&answer=7190
2. 如何使用邮件过滤器？ http://wiki.tuna.tsinghua.edu.cn/GmailFilterHowto
3. 邮件备注：转发给自己。

## calendar
1. 一些可以订阅的有趣的日历
   https://www.google.com/calendar/render?settings=10


## youtube
* download <http://www.clipconverter.cc/>

## drive

proxycap+ss+hosts/chinadns
