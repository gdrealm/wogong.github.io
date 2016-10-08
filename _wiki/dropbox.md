---
title: dropbox
date: 2015-06-17
update: 2015-07-31 15:52:13
---

## Linux Install
<https://www.dropbox.com/install?os=lnx>

dropbox.py help

    dropbox.py help
    ropbox command-line interface
    
    ommands:
    
    ote: use dropbox help <command> to view usage for a specific command.
    
    status       get current status of the dropboxd
    help         provide help
    puburl       get public url of a file in your dropbox
    stop         stop dropboxd
    running      return whether dropbox is running
    start        start dropboxd
    filestatus   get current sync status of one or more files
    ls           list directory contents with current sync status
    autostart    automatically start dropbox at login
    exclude      ignores/excludes a directory from syncing
    lansync      enables or disables LAN sync

## note
1. 电脑使用，很多服务暂时还是只在Windows(现在基本都在Arch下了20120504)下使用吧，比如Dropbox的同步，等等诸如此类，两边同时发布的错误几率太大（相同硬盘文件）。不同PC之间同步不会有任何问题。
2. 使用技巧：同步任意文件夹。`ln -s origin_filepath dropboxpath`
3. Dropbox在国内无法自动同步的解决办法.
问题描述：Dropbox无法自动同步服务器端的变更，必须重启才能解决。  
问题原因：Dropbox使用http探测服务器端文件变化，被伟大的墙所截获  
解决办法：参照月光博客两篇文章：  
http://www.williamlong.info/archives/2585.html http://www.williamlong.info/archives/3050.html  
使用privoxy，分开http与https请求，兼顾速度与同步。
4. Dropbox的照片管理功能，相册为虚拟集合，照片为Dropbox文件夹中所有图片的集合，按照时间排序。

## 周边服务
1. ifttt: http://ifttt.com/
神器不多说，将其余服务和Dropbox相连
2. Wappwolf Automator： http://wappwolf.com/dropboxautomator
Dropbox自动化，监控Dropbox特定文件夹，对Dropbox中的文档进行操作。
比如SendtoKindle, Email, unzip, upload image, convert image...
3. Sortbox:  http://www.sortmybox.com/
自由设定规则，对Dropbox中的文件进行重排，监控SortBox文件夹，然后将文件分别整理到其他文件夹。
4. 基于Dropbox和Markdown的blog：
http://calepin.co/  源码：https://github.com/jokull/calepin; http://scriptogr.am/
