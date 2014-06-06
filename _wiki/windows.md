---
layout: wiki
title: windows
---

# Windows

## note
1. 环境变量管理。Envman
2. 快速启动 `d:\Dropbox\Software\_QS\` working with adress bar in task bar.
3. program and features 取消不常用的windows 功能。
4. 如何修改网络类型？homegroup troubleshoot。
5. 休眠

        powercfg -h off 关闭休眠
        powercfg /h /size 50   调整休眠文件大小 (50为内存百分比，范围50-100)

6. mstsc 远程桌面，可以在远程挂载本地硬盘。
7. Windows更新失败，使用 sfc/scannow修复系统。
8. 服务管理 services.mvc
9. tasklist /mvc

## 系统功能
1. 计划任务 Schedule tasks
用于自动备份 C 盘文件还是很方便的。
2. Windows 命令行下复制文件夹及其子目录的命令详解
   1. 功能：拷贝一个或多个文件到指定盘上。 
   2. 类型：内部命令 
   3. 格式：COPY [源盘][路径]〈源文件名〉[目标盘][路径][目标文件名] 
   4. 使用说明： 

> 1. > （1）COPY是文件对文件的方式复制数据，复制前目标盘必须已经格式化； 
> 2. > （2）复制过程中，目标盘上相同文件名称的旧文件会被源文件取代； 
> 3. > （3）复制文件时，必须先确定目标般有足够的空间，否则会出现；insufficient的错误信息，提示磁盘空间不够； 
> 4. > （4）文件名中允许使用通配举“\*”“？”，可同时复制多个文件； 
> 5. > （5）COPY命令中源文件名必须指出，不可以省略。 
> 6. > （6）复制时，目标文件名可以与源文件名相同，称作“同名拷贝”此时目标文件名可以省略； 
> 7. > （7）复制时，目标文件名也可以与源文件名不相同，称作“异名拷贝”，此时，目标文件名不能省略； 
> 8. > （8）复制时，还可以将几个文件合并为一个文件，称为“合并拷贝”，格式如下：COPY；[源盘][路径]〈源文件名1〉〈源文件名2〉…[目标盘][路径]〈目标文件名〉； 
> 9. > （9）利用COPY命令，还可以从键盘上输入数据建立文件，格式如下：COPY CON [盘符：]


## Reinstall
1. 软件
   - 备份picasa数据库：c:\Users\chengzhen\AppData\Local\Google\Picasa2\ 
   - 备份itunes音乐库，将Windows 我的音乐位置更改至安装前的位置即可？以后再验证。
   - 备份虚拟机文件

2. 浏览器 Chrome
   - swithysharp数据导出
   - fawave数据导出

3. 安装完毕，做什么？
   - 更改个人文件默认位置，windows库
   - 安装软件:输入法，office，迅雷，TC，Dropbox，Evernote
4. 数据
   - $HOME 目录 配置文件， vim
## 神兵利器
1. Everything
文件名搜索神器;不支持全文搜索
2. unlocker
实在是很赞的一款小工具。非常适合稳健重命名移动删除等工作。
3. KeyTweak
windows下改变键盘映射工具，其他类似工具参见xbeta
http://xbeta.info/key-tweak-remap.htm
4. AutoHotKey
5. [SumatraPDF](http://blog.kowalczyk.info/software/sumatrapdf/free-pdf-reader.html)  
   Sumatra PDF is a PDF, ePub, MOBI, CHM, XPS, DjVu, CBZ, CBR reader for Windows。  
   [[Shortcuts|sumatrapdf]]






Universal-USB-Installer-1.9.5.2.exe 制作启动U盘
