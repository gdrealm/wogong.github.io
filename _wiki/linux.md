---
title: linux
date: 2014-07-18
update: 2015-07-10
---

我使用过的发行版，按照时间顺序依次为：Ubuntu, Fedora, Archlinux, Debian。使用时间最久远、最喜欢的是Archlinux。目前使用最多的是Archlinux & Debian。

## note

1. ubuntu  `cat /etc/issue`
2. ntp sudo apt-get install ntpdate `ntpdate ntp.tuna.tsinghua.edu.cn`  3.cn.pool.ntp.org
   配置文件`/etc/ntp.conf`
   hwclock -w ?
3. 更改默认shell `chsh -s /bin/bash`
4. 切换到systemd出现错误，原因在于fstab文件挂载了vmware分享文件夹，官方wiki中说明。
5. ack-grep
    ubuntu下ack居然是另外一个东西，解决：
    `sudo ln -sf /usr/bin/ack-grep /usr/local/bin/ack`
    基本配置文件：fast_cgi
    添加php插件后需要重启：
        service nginx restart
        service php5-fpm restart
6. split 分割文件，cat合并文件
7. `du -sh * | sort -n`
8. 最近修改文件find / -size +1000000c -mtime -1
9. 查看 32/64 位 `getconf LONG_BIT`

## Ubuntu

1. 键盘布局

    在Ubuntu系统终端中执行：
    sudo vim /etc/default/keyboard
    修改下面这一行：（改变capslock为ctrl）
    XKBOPTIONS="ctrl:nocaps"

2. apt-get

        apt-get update
        apt-get install
        apt-cache search
        apt-cache show
        apt-get autoremove

3. PPA 文件路径 `/etc/apt/sources.list.d`

## 常用命令

1. 用户管理
   - `useradd, userdel, usermod, passwd`
   - `groupadd, groupdel, groupmod`
   - 更改用户名 `usermod -l new_user_name old_user_name`
   - 用户信息文件 `/etc/passwd`
   - 踢出已登录用户 `pkill -KILL -t pts/0`
   - 可以采用`w`查看当前登录用户详细信息
2. rsyslog 日志系统
3. pacman

        #强制更新包目录
        pacman -Syy
        ;
        #删除单个软件包，保留其全部已经安装的依赖关系 
        pacman -R package_name
        ;
        #删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系：
        pacman -Rs package_name
        ;
        要删除软件包和所有依赖这个软件包的程序:(警告: 此操作是递归的，请小心检查，可能会一次删除大量的软件包。) 
        pacman -Rsc package_name
        ;
        要删除软件包，但是不删除依赖这个软件包的其他程序：
        pacman -Rdd package_name
        ;
        pacman 删除某些程序时会备份重要配置文件，在其后面加上*.pacsave扩展名。-n 选项可以删除这些文件：
        pacman -Rn package_name
        pacman -Rsn package_name
        pacman -Rcusn kdelibs #完全卸载KDE
        ;
        pacman 使用 -Q 参数查询本地软件包数据库。
        pacman -Q --help
        ;
        使用 -S 参数来查询远程同步的数据库。
        pacman -S --help
        ;
        pacman 可以在包数据库中查询软件包，查询位置包含了软件包的名字和描述。
        pacman -Ss package
        ;
        要查询已安装的软件包：
        pacman -Qs package
        ;
        显示软件包的详尽的信息：
        pacman -Si package
        ;
        查询本地安装包的详细信息：
        pacman -Qi package
        ;
        使用两个 -i 将同时显示备份文件和修改状态：
        pacman -Qii package_name
        ;
        要获取已安装软件包所包含文件的(very useful when you can't find the configuration files)
        pacman -Ql package
        ;
        pacman -U name.pkg.tar.bz2

        pacman -Qe

4. 文件系统 `fdisk, mkfs.ext3, mount df, du`
5. 任务管理 `ps aux, top`
6. 挂载分区
   1. Linux下挂载windows分区 我现在是windows7与Fedora16双系统，在Fedora中可以看到windows下的磁盘，但是每次使用都得类似于移动设备载入一般，而且名称是复杂无规律的字符串，非常不方便操作。今天偶然看到挂载分区的技巧，记录如下： 1.为C盘也就是/dev/sda1挂载一个目录，为/mnt/winC，步骤如下， mkdir /mnt/winC mount -t ntfs -o nls=utf8,umask=000 /dev/sda1 /mnt/winC 可以通过df -lh查看是否已经挂载成功。
   2. 若是希望开机自动实现上述挂载，可以这么做： 在/etc/fstab文件加入一行：/dev/sda1 /mnt/winC ntfs umask=000,nls=utf8 若是fat32分区，这样：/dev/sda2 /mnt/winD vfat umask=0,iocharset=utf8 0 0
   3. 可以这样设置快捷方式到桌面： ln -s /mnt/winC ~root/Desktop/winC

7. 日志系统
    arch和ubuntu的文档都是很详细的，需要时再进一步看吧
    https://wiki.archlinux.org/index.php/Rsyslog
   - 修改rsyslog文件，将/etc/rsyslog.d/50-default.conf
   - 重启rsyslog服务service rsyslog restart
   - 查看日志
              more /var/log/filename
              tail -f /var/log/filename

## package

1. ranger
    vim风格的cli文件管理器。更改默认编辑器及
    shell等等：依靠系统环境变量
2. dnsmasq
3. postfix 《Postfix 权威指南》
    删除邮件队列中全部文件：`postsuper -d ALL`
    显示邮件队列邮件：`postcat -q ID`
    `postmap hash:/etc/postfix/name` 大部分文件都需要这样做才OK
4. apache
    ubuntu手册，虚拟主机配置指南
    http://wiki.ubuntu.org.cn/Apache%E8%99%9A%E6%8B%9F%E4%B8%BB%E6%9C%BA%E6%8C%87%E5%8D%97
    简单配置网站：
        - 配置文件
        - sudo a2ensite edunuke
        - sudo a2dissite edunuke
        - sudo /etc/init.d/apache2 restart 或者 service apache2 reload/restart
5. freetalk
   console下不错的Jobber客户端。
6. irssi
   IRC console 客户端
7. vsftp
   靠谱的FTP 服务端软件。  
   `systemctl status vsftpd.service`
8. samba
10. ufw
11. iptables
12. su
问题是这样的，我有一个主机的ssh权限，用root账号ssh上去没问题，但切换成普通账号后再使用su -命令切换回root时，不论我的密码多么正确，老是提示"incorrect password"，这个问题困扰了我一天。在网上查了半天 ，终于解决了。原来是su这个命令的权限设置问题。要能使用su命令切换成根用户，需要su这个命令设置suid特殊权限位，具体方法如下：
 
    `chmod 4755 /bin/su`

13. slim
    登陆管理器  
    https://wiki.archlinux.org/index.php/SLiM登陆管理器现在已经不使用，在profile文档加入一个判断语句，执行特定用户登陆时startx
14. cpufreq
    `cpufreq-info; cpufreq-set -r -g ondemand`
15. procmail
    简易的邮件分拣系统，配置文件 .procmailrc 位于家目录下。
    procmail 配置文件简易指南  
    http://www.freebsd.org/doc/zh_CN/books/handbook/mail-procmail.html
16. tail

    tail -f 用于查看日志，follow，实时输出增加的内容
    tail -n N 输出最后N行数据

17. ack-grep
ubuntu下ack居然是另外一个东西，解决：`sudo ln -sf /usr/bin/ack-grep /usr/local/bin/ack`
18. ncdu For looking at why a disk is full, ncdu saves time over the usual commands like du -sh *.


## Linux常用命令

- 查看系统已有字体：fc-list
- 查看电池电量信息：acpi; acpi -i

- cd系列
    cd -  后退
    cd ..  上一层目录
    cd .  这个真心没用，本层目录

v看到终端输出命令

对于zip文件使用自带的unzip

- 用户和组
gpasswd -a username groupname : add user to group

一，组操作
1，创建组
groupadd  test
增加一个test组
2，修改组
groupmod -n test2  test
将test组的名子改成test2
3，删除组
groupdel test2
删除 组test2
4，查看组
a），查看当前登录用户所在的组 groups，查看apacheuser所在组groups apacheuser
b），查看所有组 cat /etc/group
c），有的linux系统没有/etc/group文件的，这个时候看下面的这个方法
cat /etc/passwd |awk -F [:] '{print $4}' |sort|uniq | getent group |awk -F [:] '{print $1}'
这里用到一个命令是getent,可以通过组ID来查找组信息,如果这个命令没有的话,那就很难查找,系统中所有的组了.
二，用户操作
1，增加用户

useradd test
passwd test
增加用户test，有一点要注意的，useradd增加一个用户后，不要忘了给他设置密码，不然不能登录的。

2，修改用户
usermod -d /home/test -G test2 test
将test用户的登录目录改成/home/test，并加入test2组，注意这里是大G。
gpasswd -a test test2 将用户test加入到test2组
gpasswd -d test test2 将用户test从test2组中移出
3，删除用户
userdel test
将test用户删除
4，查看用户
a），查看当前登录用户
[root@krlcgcms01 ~]# w
[root@krlcgcms01 ~]# who
b），查看自己的用户名
[root@krlcgcms01 ~]# whoami
c），查看单个用户信息
[root@krlcgcms01 ~]# finger apacheuser
[root@krlcgcms01 ~]# id apacheuser
d），查看用户登录记录
[root@krlcgcms01 ~]# last 查看登录成功的用户记录
[root@krlcgcms01 ~]# lastb 查看登录不成功的用户记录
e），查看所有用户
[root@krlcgcms01 ~]# cut -d : -f 1 /etc/passwd
[root@krlcgcms01 ~]# cat /etc/passwd |awk -F \: '{print $1}'


- 权限等一些很恶心的东西
学习下

 * lsof

* ping: icmp open socket: Operation not permitted

    sudo chmod u+s `which ping`

Options

-h --help

showkey prints to the standard error output its version number, a compile option and a short usage message, then exits. -s --scancodes Starts showkey in scan code dump mode. -k --keycodes Starts showkey in keycode dump mode. This is the default, when no command line options are present. -a --ascii Starts showkey in 'ascii' dump mode.


切换到systemd出现错误，原因在于fstab文件挂载了vmware分享文件夹，官方wiki中说明


memcache


启动命令 memcached -m 512 -l 127.0.0.1 -p 11211 -u root

memcache与memcached的区别。


ping -t windows下持续ping

ping -c N linux下pingN次

yes "yes" | script.sh


如果使用了如awesome、i3这样的窗口管理器，调节音量可以用下面两种方法：
1、安装kde组件kmix，然后将kmix设置为自动启动。kmix是图形界面的。
2、安装alsa-utils，然后在终端上输入命令alsamixer，就会打开一个字符界面的音量控制器。按方向键上增加音量，方向键下减少音量，按数字0－9分别会将音量调至0％－90％，按Esc退出。


不小心更改了/usr/的权限.
在执行sudo 的时候出现 sudo: must be setuid root这个提示,
网上搜了下,解决了.特记录.

ls -l  /usr/bin/sudo

chown root:root /usr/bin/sudo

chmod 4755 /usr/bin/sudo

reboot


1、输入用户管理的命令，新建用户（以test为例）：
useradd test
修改 test 用户的密码：
passwd test
2、将新用户添加到管理组：
gpasswd -a test admin
