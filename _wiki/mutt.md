---
layout: wiki
title: mutt
date: 2015-06-17
modified: 2015-10-20 14:25:24
---

## note
如果我说mutt像文件管理器，不知道会不会有人喷，233333

当年看王垠的wiki，感觉mutt是如此的蛋疼，所以一直没有需求。因为gmail的网页版做的已经十分完美了。

现在再次接触mutt的原因是在管理mail server时有大量的邮件需要管理，查看。顺便看了下mutt，才发现mutt其实就是一个邮件文件管理器。
安装好了发送邮件接收邮件的软件之后使用基本十分简单，中文支持的问题貌似也不是太恶心。但是在ubuntu10.10上的中文总是显示有问题，12.04上的就OK

配置文件什么的只要设置下邮箱位置就OK，网上也有一堆，我的github上也放了，但是以后应该不会更新了。

## 配置文件

    # 默认信箱目录
    set folder="/home/wogong/mails/"
    # 已读的信箱
    # set mbox="+incoming"
    # 进入mutt后默认使用的信箱，可以考虑和$HOME/.procmailrc设置的默认信箱相同
    set spoolfile="+mail"
    # 草稿箱
    set postponed="+postponed"
    # 已发送的信箱
    set record="+outgoing"

## 参考
[Mutt中文手册](http://xhc.me/wp-content/uploads/mutt/manual_1.5.19_zh.html#tuning-search)
