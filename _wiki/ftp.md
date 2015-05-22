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

＊mirror/sync a remote ftp folder with a local folder

        #!/bin/bash
        HOST='mysite.com'
        USER='myuser'
        PASS='myuser'
        TARGETFOLDER='/new'
        SOURCEFOLDER='/home/myuser/backups'
        
        lftp -f "
        open $HOST
        user $USER $PASS
        lcd $SOURCEFOLDER
        mirror --reverse --delete --verbose $SOURCEFOLDER $TARGETFOLDER
        bye
        "


Advanced Usage
lftp offers many parameters, here i'll explain some of the most useful ones :

--reverse : Indicates that you want to update your remote folder. if you want to update your local folder then you should remove this option and also swap values of TARGETFOLDER and SOURCEFOLDER variables
--delete : It tells lftp that you want to remove all the files/folders that no longer exist on source folder
--use-cache : If you're about to sync very large number of files, this option can speed up things a lot. It does not have any effect the first time but in the next sessions it uses local cache instead of scanning the remote server
--exclude : Sometimes there are folder/files on both source and target folders that have nothing to do with the mirroring, using this option we can tell lftp to ignore this sort of files
Tips