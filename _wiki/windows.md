---
layout: wiki
title: windows
create: 2014-06-21
update: 2015-01-11
---
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
8. 服务管理 services.msc mscocnfig
9. tasklist /mvc
0. taskmgr
10. 计划任务 Schedule tasks 用于自动备份 C 盘文件还是很方便的。
11. CMD 自带命令： help
12. Windows en   
    中文 需要更改 语音设置 否则一些中文软件会出现乱码
    lpksetup 手动安装下载的语言包
12. Appdata 文件夹内部文件位置可以更改，包括 Local LocalLow Roaming
13. 最近将日常使用的用户更改为标准账户，用了Windows系统五年多了，到今天才开始理解Windows的用户权限控制。以前总是吐槽微软，这次可以吐槽自己了。
14. 开启了Windows的 file history 功能，同步到局域网的 raspberry
15. 在CMD下输入netstat -anp tcp可以查看当前主机tcp开放了哪些端口

## Reinstall
1. 软件
  - Office 记得取消安装一些奇葩的组件
  - 小狼毫 用户资料夹采用mklink解决
  - 7zip
  - 浏览器 Chrome
  - Drive 需要翻墙环境
  - iTunes
  - zotero
  - 字体 Monoca
  - git
  - picasa
  - eudict 程序文件需要备份

能绿色一一定绿色

鼠标触控板设置


2. 浏览器 Chrome
   - swithysharp数据导出

3. 安装完毕，做什么？
   - 更改个人文件默认位置，windows库
   - 安装软件:输入法，office，迅雷，TC，Dropbox，Evernote
4. 数据
   - $HOME 目录 配置文件， vim


## Softwares
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
6. Universal-USB-Installer-1.9.5.2.exe 制作启动U盘
V7. babun  \*nix like console


http://windows.microsoft.com/zh-cn/windows/windows-update-error-80070003

重装系统 更改 HOME


WINDOWS 中交换 CONTROL 键和 CAPS LOCK 键


在开始的搜索框或者运行框输入regedit ，打开注册表管理器。
转到  HKEY_LOCAL_MACHINE -> System -> CurrentControlSet -> Control -> KeyBoard Layout
在此文件夹“新建” ， “二进制值”
修改新建的名字为：Scancode Map
在其上点右键，选择修改二进制数据，输入如下数据。第一列不用输入。所以不好复制，手输吧。
0000 00 00 00 00 00 00 00 00
0008 03 00 00 00 1d 00 3a 00
0010 3a 00 1d 00 00 00 00 00
0018

0000 00 00 00 00 00 00 00 00
0008 02 00 00 00 1d 00 3a 00
0010 00 00 00 00

好了 现在重启电脑 应该一切生效了 只用改这一处两个键就交换了

出处： http://www.kodiva.com/post/swapping-caps-lock-and-control-keys

## Windows 8.1 安装密钥
专业版安装密匙：XHQ8N-C3MCJ-RQXB6-WCHYG-C9WKB 
普通版安装密匙：334NH-RXG76-64THK-C7CKG-D3VPT