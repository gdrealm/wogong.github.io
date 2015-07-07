---
title: windows
date: 2014-06-21
update: 2015-02-13
---

重装系统，卸载 机械硬盘，只保留 SSD 安装系统。之后打开 File History

添置笔记本硬盘

另外，总结下双系统卸载方法，grub rescue后重新引导windows

## NOTE
1. 环境变量管理 Envman
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
    中文 需要更改 语言设置 否则一些中文软件会出现乱码 控制面板-时间等
    lpksetup 手动安装下载的语言包
12. Appdata 文件夹内部文件位置可以更改，包括 Local LocalLow Roaming
13. 最近将日常使用的用户更改为标准账户，用了Windows系统五年多了，到今天才开始理解Windows的用户权限控制。以前总是吐槽微软，这次可以吐槽自己了。
14. 开启了Windows的 file history 功能，同步到局域网的 raspberry
15. 在CMD下输入netstat -anp tcp可以查看当前主机tcp开放了哪些端口
16. runas /noprofile /user:admin cmd
17. 系统环境变量中的 PATHEXT 项没有.EXE，在CMD下面执行命令需要加上exe后缀才能执行
18. 虚拟wifi

        1、笔记本有无线网卡且支持虚拟WIFI。 
        2、按WIN+X键，以管理员身份运行CMD回车。
        3、输入netsh wlan set hostednetwork mode=allow ssid=mywifi key=12345678 设置无线名称和链接密码，等有提示设置成功出现再关闭。 
        4、输入netsh wlan start hostednetwork 启动WIFI承载网络出现再关闭。 
        5、此时控制面板中找到网络和共享中心点击进入。 
        6、左侧点击“更改适配器设置”会弹出网络连接界面里面有本地连接 无线连接 无线连接2（Microsoft托管网络虚拟适配器这个无线连接2就是WIFI热点啦） ，右击属性，找到Internet TCP/IP协议4， 双击进入设置IP 地址为192.168.123.1 掩码255.255.255.0 关闭并确定。 
        7、找到本地连接 （用路由器网线上网的那个也就是） 同样右击属性，共享选项卡--允许其他网络用户通过次...，前面打钩，选择-家庭网络选中无线网络2（就是选WIFI热点刚刚设置那个），确定。 
        8，OK，这样基本电脑端设置就OK了，然后进行手机设置。 
        9、连接SSID mywifi 连接输入密码 12345678，连接上。 
        10、全部搞定。 
        11、如果是宽带连接不是路由器上网，把本地连接的操作的换到宽带连接（拨号那个）设置。
19. winsat disk -drive c 测试硬盘速度
20. svchost.exe点击我的电脑右键->管理->服务和应用程序->服务，找到“Background Intelligent Transfer Service”，关闭，点击右键设置属性，将启动类型设置为手动或禁用。这是微软搞的后台自动传输数据的服务。
21. sc query 查询服务 sc delete 删除服务
22 WINDOWS 中交换 CONTROL 键和 CAPS LOCK 键
<http://www.kodiva.com/post/swapping-caps-lock-and-control-keys>
转到  HKEY_LOCAL_MACHINE -> System -> CurrentControlSet -> Control -> KeyBoard Layout
在此文件夹“新建” ， “二进制值”
修改新建的名字为：Scancode Map
在其上点右键，选择修改二进制数据，输入如下数据。
- 替换
0000 00 00 00 00 00 00 00 00
0008 03 00 00 00 1d 00 3a 00
0010 3a 00 1d 00 00 00 00 00
0018
- 修改
0000 00 00 00 00 00 00 00 00
0008 02 00 00 00 1d 00 3a 00
0010 00 00 00 00

23. 运行secpol.msc命令修改本地安全策略，找到 网络列表管理器策略 改变网络类型 
24. windows 利用计划任务备份本地C盘文件
    help xcopy
25. 修复 mbr 分区
    从U盘启动Windows，进入系统后按Shift+F10，启动DOS：
    首先将C盘设置为活动分区：bootsect /nt60 ALL /mbr
    修复系统的MBR表：bootrec /fixmbr
16. 
    键值 
    文件夹
    {374DE290-123F-4565-9164-39C4925E4678}	下载
    {B4BFCC3A-DB2C-424C-BO29-7FE99A87C641}	桌面
    {1CF1260C-4DD0-4ebb-811F-33C572699FDE} 
    音乐
    {3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA} 
    图片
    {A0953C92-50DC-43bf-BE83-3742FED03C9C}	视频
    {A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}	文档
    
## Reinstall
* Caps -> Ctrl
* TC config: Portable\tc
* Office 记得取消安装一些奇葩的组件 MathType
* 小狼毫 `mklink /D c:\Users\wogong\AppData\Roaming\Rime d:\Portable\Weasel`
* eudict `mklink /D c:\Users\wogong\AppData\Roaming\Francochinois d:\Portable\Francochinois`
* zotero
* 7zip IDM DUMETER
* Chrome  
* iTunes (iPhone Backup)
* 定时备份的计划任务

1. softwares
  - 字体 Monoca
  - git
  - picasa
3. Settings
   - 更改个人文件默认位置，windows库
   - 鼠标触控板设置
   - everything 服务 开机启动
   - chrome abp 选项


## Softwares
* Everything
    文件名搜索神器;不支持全文搜索
* Yumi
    制作启动U盘
* [SumatraPDF](http://blog.kowalczyk.info/software/sumatrapdf/free-pdf-reader.html)  
    Sumatra PDF is a PDF, ePub, MOBI, CHM, XPS, DjVu, CBZ, CBR reader for Windows。  
* SMsolver 结力求解器
* Calibre
* putty
    windows下的ssh登陆软件 
* virgo

    ALT + 1..4             -> changes to desktop 1..4
    CTRL + 1..4            -> moves active window to desktop 1..4
    ALT + CTRL + SHIFT + Q -> exits the program
    ALT + CTRL + SHIFT + S -> starts/stops handling of other hotkeys

* replace pioneer
    集成的文本处理工具，非常强大。安装后可以试用21天，到期后重装即可。汗颜
* unlocker
    实在是很赞的一款小工具。非常适合稳健重命名移动删除等工作。
* AutoHotKey AHK
* Du Meter
    流量监控软件 ￥59
* Eudict
    欧陆词典 ￥99
* Internet Download Manager IDM
    下载工具 ￥89
* [Total Commander TC](/wiki/tc)
* Evernote
* Dropbox
* Ccleaner
    简单小巧，功能足够而不繁多。
* Filezilla
    FTP tools
* Windows install cleaner
      用于清除office等卸载不干净的情况，同样适应于其他msi安装方式的软件卸载
* wireshart
    抓包软件
* [Vmware](/wiki/vmware)
* KeyTweak
    windows下改变键盘映射工具，其他类似工具参见xbeta  
    <http://xbeta.info/key-tweak-remap.htm>
