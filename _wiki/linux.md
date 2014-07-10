---
layout: wiki
title: linux
---

# linux

我使用过的发行版，按照时间顺序依次为：Ubuntu, Fedora, Archlinux, Debian。
使用时间最久远、我最喜欢的是Archlinux。
目前使用最多的是Archlinux & Ubuntu。

## note
1. ubuntu  `cat /etc/issue`
2. ntp `ntpdate ntp.tuna.tsinghua.edu.cn`  3.cn.pool.ntp.org
   配置文件`/etc/ntp.conf`
   hwclock -w ?
3. 更改默认shell `chsh -s /bin/bash`
4. 切换到systemd出现错误，原因在于fstab文件挂载了
vmware分享文件夹，官方wiki中说明。
5. ack-grep
ubuntu下ack居然是另外一个东西，解决：
`sudo ln -sf /usr/bin/ack-grep /usr/local/bin/ack`
基本配置文件：fast_cgi
添加php插件后需要重启：
        service nginx restart
        service php5-fpm restart
6. 测试。
 
## 常用命令
1. 用户管理
   - `useradd, userdel, usermod, passwd`
   - `groupadd, groupdel, groupmod`
   - 更改用户名 `usermod -l new_user_name old_user_name`
   - 用户信息文件 `/etc/passwd`
   - 踢出已登录用户 `pkill -KILL -t pts/0`
     可以采用`w`查看当前登录用户详细信息
3. rsyslog 日志系统
4. pacman

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
5. 文件系统  
   `fdisk, mkfs.ext3, mount df, du`
6. 任务管理
   `ps aux, top`
7. 挂载分区
   1. Linux下挂载windows分区 我现在是windows7与Fedora16双系统，在Fedora中可以看到windows下的磁盘，但是每次使用都得类似于移动设备载入一般，而且名称是复杂无规律的字符串，非常不方便操作。今天偶然看到挂载分区的技巧，记录如下： 1.为C盘也就是/dev/sda1挂载一个目录，为/mnt/winC，步骤如下， mkdir /mnt/winC mount -t ntfs -o nls=utf8,umask=000 /dev/sda1 /mnt/winC 可以通过df -lh查看是否已经挂载成功。
   2. 若是希望开机自动实现上述挂载，可以这么做： 在/etc/fstab文件加入一行：/dev/sda1 /mnt/winC ntfs umask=000,nls=utf8 若是fat32分区，这样：/dev/sda2 /mnt/winD vfat umask=0,iocharset=utf8 0 0
   3. 可以这样设置快捷方式到桌面： ln -s /mnt/winC ~root/Desktop/winC
8. 日志系统
arch和ubuntu的文档都是很详细的，需要时再进一步看吧
https://wiki.archlinux.org/index.php/Rsyslog
   - 修改rsyslog文件，将/etc/rsyslog.d/50-default.conf
   - 重启rsyslog服务service rsyslog restart
   - 查看日志： 
              more /var/log/filename
              tail -f /var/log/filename

## Software
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
9. [[shadowsocks]]
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




## Linux常用命令

- 查看系统已有字体：fc-list

- 查看电池电量信息：acpi

- cd系列
    cd -  后退
    cd ..  上一层目录
    cd .  这个真心没用，本层目录

- 更改路径：
  # 暂时使用
亦即重启或注销后就失效了。
使用 PATH=$PATH:目录:目录... 直接赋值。如 PATH=$PATH:/sbin。
	# 长期使用
在全局文件 /etc/profile 中或用户自定义文件 ~/.bash_profile 中添加上述命令即可！bash_rc?



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
查看复制打印?
[root@krlcgcms01 mytest]# useradd --help  
Usage: useradd [options] LOGIN  
  
Options:  
 -b, --base-dir BASE_DIR       设置基本路径作为用户的登录目录  
 -c, --comment COMMENT         对用户的注释  
 -d, --home-dir HOME_DIR       设置用户的登录目录  
 -D, --defaults                改变设置  
 -e, --expiredate EXPIRE_DATE  设置用户的有效期  
 -f, --inactive INACTIVE       用户过期后，让密码无效  
 -g, --gid GROUP               使用户只属于某个组  
 -G, --groups GROUPS           使用户加入某个组  
 -h, --help                    帮助  
 -k, --skel SKEL_DIR           指定其他的skel目录  
 -K, --key KEY=VALUE           覆盖 /etc/login.defs 配置文件  
 -m, --create-home             自动创建登录目录  
 -l,                           不把用户加入到lastlog文件中  
 -M,                           不自动创建登录目录  
 -r,                           建立系统账号  
 -o, --non-unique              允许用户拥有相同的UID  
 -p, --password PASSWORD       为新用户使用加密密码  
 -s, --shell SHELL             登录时候的shell  
 -u, --uid UID                 为新用户指定一个UID  
 -Z, --selinux-user SEUSER     use a specific SEUSER for the SELinux user mapping  

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

 * sudo chmod u+s `which ping`


----
CategoryApp


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
