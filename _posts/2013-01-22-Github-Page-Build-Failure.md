---
layout: post
title: "GitHub Page Build Failure"
description: ""
category: it
tags: [github, jekyll]
---

## 通用的解决方法

今日折腾了许久，更换了评论系统，由[Disqus](http://disqus.com/)转到了[多说](http://duoshuo.com/)，主要是考虑前者在国内被墙的厉害。但是在挂上VPN推送到[GitHub]()的几秒后弹出邮件提示“Page Build Failure”，详见下图：

<img src="http://24.media.tumblr.com/f162b08f8b1d9b5db4823a791ac97f99/tumblr_mgzoh1qmX21rpy6u9o1_500.png" title="mail" alt="mail" />

由于本地已经测试，可以成功build，所以倍感奇怪，网上搜索之后发现可能是Jekyll的版本与GitHub的版本不一样，可以通过`jekyll -v`查看本地安装的Jekyll版本，如果并非最新版本需要升级，当前的最新版本是`0.12.0`

    gem install jekyll --version 0.12.0

本地运行：

    jekyll --server --no-auto

根据报错检查，等到成功build之后便应该没有什么问题了。


## 我遇到的问题

Jekyll我使用的是这个主题[theme-mark-reid](https://github.com/jekyllbootstrap/theme-mark-reid)。之前一直没有问题，没想到在`jekyll 0.12.0`下遇到了bug，build时会出现如下的错误信息：

    STRFTIME() is not defined 

已经在GitHub上提交了[issue](https://github.com/jekyllbootstrap/theme-mark-reid/issues/4)，目前的解决办法是删除掉有问题的语句，损失了文章结束时间戳的功能。
