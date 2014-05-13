---
layout: wiki
title: samba
---

# SAMBA

1. samba  
   [arch wiki](https://wiki.archlinux.org/index.php/Samba#Server_configuration)

        pacman -S samba
        systemctl enable smbd.service
        systemctl enable nmbd.service

2. Debian
   
        service samba status


- samba
smbclient //166.111.9.155/movie -U username%passwd


   [arch wiki](https://wiki.archlinux.org/index.php/Samba#Server_configuration)
   smbclient //166.111.9.155/movie -U username%passwd

        mount -t cifs -o username="administrator",password="" //192.168.1.101/name /mnt/samba
        pacman -S samba
        systemctl enable smbd.service
        systemctl enable nmbd.service

# 2. 使用 pdbedit 指令功能

       [root@www ~]# pdbedit -L [-vw]            <==單純的察看帳號資訊
       [root@www ~]# pdbedit -a|-r|-x -u 帳號    <==新增/修改/刪除帳號
       [root@www ~]# pdbedit -a -m -u 機器帳號   <==與 PDC 有關的機器碼
       選項與參數：
       -L ：列出目前在資料庫當中的帳號與 UID 等相關資訊；
       -v ：需要搭配 -L 來執行，可列出更多的訊息，包括家目錄等資料；
       -w ：需要搭配 -L 來執行，使用舊版的 smbpasswd 格式來顯示資料；
       -a ：新增一個可使用 Samba 的帳號，後面的帳號需要在 /etc/passwd 內存在者；
       -r ：修改一個帳號的相關資訊，需搭配很多特殊參數，請 man pdbedit；
       -x ：刪除一個可使用 Samba 的帳號，可先用 -L 找到帳號後再刪除；
       -m ：後面接的是機器的代碼 (machine account)，與 domain model 有關！
