---
layout: wiki
title: ftp
update: 2014-10-24
---
## Client
1. Windows Filezila Client
2. linux => lftp linux cli ftp client
	lftp -u user,passwd server
mirror
mirror --reverse

## server
1. linux
VSFTP 主要是配置文件，安装即可使用。`/etc/vsftpd.conf`
2. Windows
FileZila Server: 不错的windows ftp server， 设置什么的也比较简单。但是在windows下的防火墙设置比较坑爹，一般如果不能连接基本都是防火墙的问题，可以采用完全关闭防火墙的方法测试。

另外，如果server是在内网，即NAT环境下的话还需要考虑主动被动模式。