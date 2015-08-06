title: debian
date: 2014-05-18
modified: 2015-07-30 22:40:20

## note
2. apt-get
    mirror: /etc/apt/sources.list
    apt-get update
    apt-get upgrade
    apt-get insatall name
    apt-get remove name

4. dpkg
dpkg -i local.deb
dpkg -S command 查看command属于哪个软件包。

apt-get update &&apt-get -f install 

1. dpkg: package manager for Debian
* 安装： dpkg -i package
* 卸载： dpkg -r package
* 卸载并删除配置文件: dpkg -P |–purge package
* 如果安装一个包时。说依赖某些库。 可以先 apt-get install somelib…
* 查看软件包安装内容 :dpkg -L package
* 查看文件由哪个软件包提供: dpkg -S filename
* 另外 dpkg还有 dselect和aptitude 两个frontend.
2. apt
* 安装: apt-get install packs
* apt-get update : 更新源
* apt-get upgrade: 升级系统。
* apt-get dist-upgrade: 智能升级。安装新软件包,删除废弃的软件包
* apt-get -f install ： -f == –fix broken 修复依赖
* apt-get autoremove: 自动删除无用的软件
* apt-get remove packages :删除软件
* apt-get remove package –purge 删除包并清除配置文件
* 清除所以删除包的残余配置文件: dpkg -l |grep ^rc|awk '{print $2}’ |tr ["/n"] [" "]|sudo xargs dpkg -P
* 安装软件时候包的临时存放目录 : /var/cache/apt/archives
* 清除该目录: apt-get clean
* 清除该目录的旧版本的软件缓存: apt-get autoclean
* 查询软件some的依赖包： apt-cache depends some
* 查询软件some被哪些包依赖: apt-get rdepends some
* 搜索软件: apt-cache search name|regexp
* 查看软件包的作用：apt-cache show package
* 查看一个软件的编译依赖库: apt-cache showsrc packagename|grep Build-Depends
* 下载软件的源代码 : apt-get source packagename (注: sources.list 中应该有 deb-src 源)
* 安装软件包源码的同时, 安装其编译环境 :apt-get build-dep packagename (有deb-src源)
* 如何将本地光盘加入安装源列表: apt-cdrom add
重点：如果我需要的gcc是gcc-4.3的但是现在装的是gcc-4.4
可以通过sudo aptitude install gcc来降低版本
APT-get是一条linux命令，适用于deb包管理式的操作系统，主要用于自动从互联网的软件仓库中搜索、安装、升级、卸载软件或操作系统。
apt-get命令一般需要root权限执行，所以一般跟着sudo命令
例sudo apt-get xxxx

APT包管理的大多数信息查询功能都可以由apt-cache命令实现,通过apt-cache命令配合不同的子命令和参数的使用,可以实现查找,显示软件包信息及包依赖关系等功能.

显示数据源中的包的统计信息
apt-cache stats命令用于显示当前系统所使用的Debian数据源的统计信息,用户可以使用该命令查看数据源的相关统计信息.

按关键字查找软件包
apt-cache search 命令可以按关键字查找软件包,通常用于查询的关键字会使用软件包的名字或软件包的一部分.
例如:apt-cache search vim

显示软件包的详细信息
通过apt-cache search 命令查询到与关键字相关联的软件包后,可以使用apt-cache show命令显示指定软件包的详细信息.
例如:apt-cache show vim

查询软件包的依赖关系
通过apt包管理工具可以有效的解决软件包的安装,卸载过程中的包依赖关系问题,而当用户需要了解某个软件包依赖于其他哪些包时,可以使用apt-cache depends来查询包依赖关系.
例如:apt-cache depends vim


查询软件包反向依赖关系
apt-cache rdepend命令用于查询指定软件包的反向依赖关系,即那些其他的软件包需要依赖指定的软件包做为安装和运行的必须条件.                                                                                               

apt-get update
在修改/etc/apt/sources.list或/etc/apt/preferences之後运行该命令。此外您需要定期运行这一命令以确保您的软件包列表是最新的。
apt-get install packagename
安装一个新软件包（参见下文的aptitude）
apt-get remove packagename
卸载一个已安装的软件包（保留配置文档）
apt-get --purge remove packagename
卸载一个已安装的软件包（删除配置文档）
dpkg --force-all --purge packagename
有些软件很难卸载，而且还阻止了别的软件的应用，就能够用这个，但是有点冒险。                            apt-get autoclean apt
会把已装或已卸的软件都备份在硬盘上，所以假如需要空间的话，能够让这个命令来删除您已删掉的软件
apt-get clean
这个命令会把安装的软件的备份也删除，但是这样不会影响软件的使用。
apt-get upgrade
更新任何已安装的软件包
apt-get dist-upgrade
将系统升级到新版本
apt-cache search string
在软件包列表中搜索字符串
dpkg -l package-name-pattern
列出任何和模式相匹配的软件包。假如您不知道软件包的全名，您能够使用“*package-name-pattern*”。
aptitude
周详查看已安装或可用的软件包。和apt-get类似，aptitude能够通过命令行方式调用，但仅限于某些命令——最常见的有安装和卸载命令。由于aptitude比apt-get了解更多信息，能够说他更适合用来进行安装和卸载。
apt-cache showpkg pkgs
显示软件包信息。
apt-cache dumpavail
打印可用软件包列表。
apt-cache show pkgs
显示软件包记录，类似于dpkg –print-avail。
apt-cache pkgnames
打印软件包列表中任何软件包的名称。
dpkg -S file
这个文档属于哪个已安装软件包。
dpkg -L package
列出软件包中的任何文档。
apt-file search filename
查找包含特定文档的软件包（不一定是已安装的），这些文档的文档名中含有指定的字符串。apt-file是个单独的软件包。您必须先使用apt-get install来安装他，然後运行apt-file update。假如apt-file search filename输出的内容太多，您能够尝试使用apt-file search filename | grep -w filename（只显示指定字符串作为完整的单词出现在其中的那些文档名）或类似方法，例如：apt-file search filename | grep /bin/（只显示位于诸如/bin或/usr/bin这些文档夹中的文档，假如您要查找的是某个特定的执行文档的话，这样做是有帮助的）。
＊ apt-get autoclean
定期运行这个命令来清除那些已卸载的软件包的.deb文档。通过这种方式，您能够释放大量的磁盘空间。假如您的需求十分迫切，能够使用apt-get clean以释放更多空间。这个命令会将已安装软件包裹的.deb文档一并删除。大多数情况下您不会再用到这些.debs文档，因此假如您为磁盘空间不足而感到焦头烂额，这个办法也许值得一试。



3. Configuring Locales

The Easy Way

Install debconf (i.e. run apt-get update then apt-get install debconf, as root)
Run dpkg-reconfigure locales as root
The Hard Way

Edit /etc/locale.gen as root. If /etc/locale.gen does not exist, create it. An example /etc/locale.gen is below.
Run /usr/sbin/locale-gen as root
A sample /etc/locale.gen

    > # This file lists locales that you wish to have built. You can find a list
    > # of valid supported locales at /usr/share/i18n/SUPPORTED. Other
    > # combinations are possible, but may not be well tested. If you change
    > # this file, you need to rerun locale-gen.
    > #
    > # XXX GENERATED XXX
    > #
    > # NOTE!!! If you change this file by hand, and want to continue
    > # maintaining manually, remove the above line. Otherwise, use the command
    > # "dpkg-reconfigure locales" to manipulate this file. You can manually
    > # change this file without affecting the use of debconf, however, since it
    > # does read in your changes.
    > 
    > en_US.UTF-8 UTF-8
    > 
