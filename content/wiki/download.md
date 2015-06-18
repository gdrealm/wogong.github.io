---
title: download
date: 2015-06-18 19:55:09
modified: 2015-06-18 19:55:09
category: 
tags: 
slug: 
authors: wogong
summary: 
---

## 迅雷离线

## 百度云
1. aria2
2. [bypy](https://github.com/houtianze/bypy)
    
    git clone url
    # in arch, change python to python2
    sudo ln -s /home/wogong/bypy/bypy.py /usr/bin

    更详细的了解某一个命令：
    bypy.py help <command> 

    显示在云盘（程序的）根目录下文件列表：
    bypy.py list

    把当前目录同步到云盘：
    bypy.py syncup
    bypy.py upload
    
    把云盘内容同步到本地来：
    bypy.py syncdown
    bypy.py downdir /

    运行时添加-v参数，会显示进度详情。
    运行时添加-d，会显示一些调试信息。
    运行时添加-ddd，还会会显示HTTP通讯信息（警告：非常多）

## VPS


