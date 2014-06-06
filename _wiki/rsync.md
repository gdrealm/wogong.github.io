---
layout: wiki
title: rsync
---

#rsync

## 常用命令

1. sync dir
`rsync -avz --delete source/ dest:/`

## Windows 下配置 rsync

Rsync是一款不错的文件免费同步软件，可以镜像保存整个目录树和文件系统，同时保持原来文件的权限、时间、软硬链接。第一次同步时 rsync 会复制全部内容，下次只传输修改过的文件部分。传输数据过程中可以实行压缩及解压缩操作，减少带宽流量。支持scp、ssh及直接socket方式连接,支持匿名传输。支持Linux,Window平台。写本文的时候，window版最新版为4.0.5版

官网：http://rsync.samba.org/

Linux版下载：http://rsync.samba.org/download.html

Windows版下载：https://www.itefix.no/i2/cwrsync-get 选(Free Edition 免费版)

默认路径 Program files/ICW

客户端：cwRsync 4.0.5 Installer

服务端：cwRsyncServer 4.0.5 Installer

复制链接文件。达到备份目的
rsync -L --port=28950 -vzrtopg --progress --delete 127.0.0.1::backupdir /cygdrive/h/BACKUPDIR

rsync -L --chmod u+rwx --port=28950 -avr --progress --delete -stat 127.0.0.1::music /cygdrive/g/BACKUPDIR/Music




一、安装配置 Rsync 服务端

Window版服务端：

1. 点击服务端安装程序进行安装，安装过程中提示输入服务端程序以服务运行时的用户名，密码。可以自定义，也可以用默认的用户名密码设置。

2. 安装完成之后，进入程序安装目录根目录，打开配置文件（如：C:\Program Files\ICW\rsyncd.conf ），进入配置。

use chroot = false
strict modes = false
lock file = rsyncd.lock 
hosts allow = 192.168.1.21
max connections = 5
port = 28950
pid = 0
uid = 0

log file = /cygdrive/f/RsyncLog/rsyncd.log

# Module definitions
# Remember cygwin naming conventions : c:\work becomes /cygdrive/c/work

[data_backup]
path = /cygdrive/f/dataBackup
auth users = dbbackuper
secrets file = /cygdrive/e/Setting/Rsync/rsync_db.ps
read only = no
list = no
transfer logging = yes

以上Windows目录的写法，应该按照POSIX风格来写，默认配置文件的写法cygwin貌似不工作，而要写成cygdrive，如D:/data，要写成/cygdrive/d/data。


以上配置只允许192.168.1.21访问，这里按需修改。

strict modes = false 不验证用户密码,

pid = 0,uid = 0指定匿名访问。

auth users ： 指访问data_backup的用户名

secrets file ： data_backup用户名对应的密码文件。

 

3. 新建密码文件：E:\Setting\Rsync\rsync_db.ps 。如：

root:root

admin:12345

密码文件格式：用户名:密码，一行一个，有的系统不支持长密码，另个密码文件的权限对其它用户组是不可读的，设置错了可能不工作。在Windows下，密码文件的访问权限一定要设置正确，不然用户验证的时候通不过。应将密码文件E:\Setting\Rsync\rsync_db.ps的权限加入Rsycn服务运行服务的用户名 cwRsyncServer 的读取权限 及 设置其为该文件为所有者。



 

4. 在服务管理器中，找到服务 RsyncServer 服务，并启动服务。

5. 如果开启了防火墙，则防火墙规则中要添加Tcp端口 28950 允许通信。



6. 服务验证，打开dos命令框，输入telnet 192.168.1.20 28950 （如果没有安装telnet服务端与客户端，请在控制面板->添加删除程序->打开关闭windows功能中找到Telnet客户端和服务端，勾选进行安装）。如果telnet能成功连接，出现@RSYNCD: 30.0 等类似文字，则说明服务启动正常。



 

二、安装配置 Rsync 客户端

1. 安装Rsync客户端程序，直至安装完成。

2. 测试服务器Rsync的连通性。在Rsync客户端所在计算机telnet Rsync服务端所在计算的相应地址和端口 

telnet 192.168.1.20 28950
出现@RSYNCD: 30.0 等类似文字，则说明客户端连接服务端正常。



 

3. 打开Dos命令窗口，进到Rsync客户端安装目录的bin目录下，如：C:\Program Files\cwRsync\bin\。输入以下命令，开始进行同步:

cd C:\Program Files\cwRsync\bin\
rsync --port=28950 -vzrtopg --progress --delete 192.168.1.20::data_backup /cygwin/f/dataBackup --password-file=/cygdrive/e/Setting/Rsync/rsync_db.ps 
 

参数说明：

--port=28950 # 端口
-vzrtopg --progress # 显示同步过程详细信息
--delete # 从客户端目录中删除与服务端目录中不同的数据，保证两边数据完全一致
/cygwin/f/dataBackup # Window下目录F:\dataBackup
data_backup # 服务端配置文件rsyncd.conf文件中定义的模块名称
192.168.1.20 # Rsync服务端IP地址
设置该命令文件的用户需要添加密码文件的读取权限及加其为文件所有者。如下：



 

 4. 添加系统计划定期执行

 新建命令执行文件C:\Program Files\cwRsync\bin\SyncDB_NoAuth.cmd。将以下命令保存到该文件中：

rsync --port=28950 -vzrtopg --progress --delete 192.168.1.20::data_backup /cygwin/f/dataBackup --password-file=/cygdrive/e/Setting/Rsync/rsync_db.ps 
 

在Window中添加任务计划，不同的系统，操作有点不一样。

windows xp/Server 2003 : 开始->设置->控制面板->任务计划->打开添加任务计划->下一步

windows 7/Server 2008 : 开始-> 控制面板 -> 管理工具 -> 任务计划

 

 

 

 

三、配置项解析

 

 

四、安装配置中常见问题

 

错误1: rsync: read error: Connection reset by peer (104) 
rsync error: error in rsync protocol data stream (code 12) at io.c(794) [receive r=3.0.2] 
解决：很大可能是服务器端没有开启 rsync 服务。开启服务。


错误2：@ERROR: chdir failed 
rsync error: error starting client-server protocol (code 5) at main.c(1495) [receiver=3.0.2] 
解决：服务器端同步目录没有权限，cwrsync默认用户是Svcwrsync。为同步目录添加用户Svcwrsync权限。


错误3：@ERROR: failed to open lock file 
rsync error: error starting client-server protocol (code 5) at main.c(1495) [receiver=3.0.2] 
解决：配置文件 rsync.conf中添加 lock file = rsyncd.lock 即可解决。

 

错误4： rsync: could not open password file "/cygwin/e/Setting/Rsync/rsync_db.pwd": No such file or directory (2)

解决：密码文件的目录一定要存在，而且要用POSIX风格的写法：/cygdrive/e/Setting/Rsync/rsync_db.pwd

 

错误5：@ERROR: auth failed on module data_backup rsync error: error starting client-server protocol (code 5) at main.c(1506) [Receiver=3.0.7]

解决：密码错误，输入正确的密码即可。用户名和密码如果都正确，可能是远程rsync服务器的帐户密码文件的权限必须为600。

 

错误6： password file must not be other-accessible

解决：这是因为rsyncd.pwd rsyncd.sec的权限不对，应该设置为600。如：chmod 600 rsyncd.pwd, Windows下应将密码文件的所有者改成程序运行的用户。

 

错误7：@ERROR: invalid uid nobody . rsync error: error starting client-server protocol (code 5) at main.c(1506) [Receiver=3.0.7]
解决：在rsyncd.conf文件中添加下面两行即可
uid = 0
gid = 0 

 

问题8： @ERROR: chroot failed
rsync error: error starting client-server protocol (code 5) at main.c(1522) [receiver=3.0.3]
原因：服务器端的目录不存在或无权限。创建目录并修正权限可解决问题。

 

问题9：@ERROR: Unknown module ‘tee_nonexists’
rsync error: error starting client-server protocol (code 5) at main.c(1522) [receiver=3.0.3]
原因：服务器不存在指定模块。提供正确的模块名或在服务器端修改成你要的模块以解决问题。

 

问题10：rsync: failed to connect to 218.107.243.2: No route to host (113)
rsync error: error in socket IO (code 10) at clientserver.c(104) [receiver=2.6.9]
原因：对方没开机、防火墙阻挡、通过的网络上有防火墙阻挡，都有可能。关闭防火墙，其实就是把tcp udp的873或者指定的rsync端口打开。

 

问题11：rsync error: error starting client-server protocol (code 5) at main.c(1524) [Receiver=3.0.7]
原因：/etc/rsyncd.conf配置文件内容有错误。请正确核对配置文件。

 

问题12：rsync: chown "" failed: Invalid argument (22)
原因：权限无法复制。去掉同步权限的参数即可。(这种情况多见于Linux向Windows的时候)

 

问题13：@ERROR: daemon security issue -- contact admin
rsync error: error starting client-server protocol (code 5) at main.c(1530) [sender=3.0.6]
原因：同步的目录里面有软连接文件，需要服务器端的/etc/rsyncd.conf打开use chroot = yes。掠过软连接文件。



问题14：rsync: read error: Connection reset by peer (104)
rsync error: error in rsync protocol data stream (code 12) at io.c(794) [receiver=3.0.2]
解决：很大可能是服务器端没有开启 rsync 服务，开启服务。

 
