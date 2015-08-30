---
layout: post
title: "树莓派上使用迅雷远程下载"
description: "树莓派上使用迅雷远程下载"
tags: [raspberry, thunder, xunlei]
---

### 设备信息

    %cat /proc/cpuinfo 
    processor       : 0
    model name      : ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS        : 2.00
    Features        : swp half thumb fastmult vfp edsp java tls 
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xb76
    CPU revision    : 7
    
    Hardware        : BCM2708
    Revision        : 000e
    Serial          : 000000005740d64d

    %uname -a
    Linux rpi 3.10.19+ #600 PREEMPT Sat Nov 16 20:34:43 GMT 2013 armv6l GNU/Linux

### Xware 版本
`Xware1.0.5_armel_v5te_glibc.zip`

下载地址：[http://g.xunlei.com/thread-208-1-1.html](http://g.xunlei.com/thread-208-1-1.html)

### 步骤
1. 官方论坛教程  
[http://g.xunlei.com/forum.php?mod=viewthread&tid=30&extra=page%3D1%26filter%3Dtypeid%26typeid%3D3](http://g.xunlei.com/forum.php?mod=viewthread&tid=30&extra=page%3D1%26filter%3Dtypeid%26typeid%3D3)

2. 简单步骤  
下载上述的可执行文件，直接运行，得到激活码按照提示绑定即可。

远程下载地址：
[http://yuancheng.xunlei.com](http://yuancheng.xunlei.com) 

### 备注及可能遇到的问题
1. 提示“无磁盘”，无法下载  
没有挂载磁盘。迅雷是检测挂载的磁盘来作为下载的目录。所以要保证几个事情，一是迅雷要具有写入权限；
二是必须要有挂载的磁盘，而且这个磁盘必须不是挂载到根目录的。通过以下命令实现。

        sudo mkdir /mnt/thunder    #建立一个文件夹
        sudo chomd 0777  /mnt/thunder   #更改文件夹的权限
        sudo mount –bind   /home/name/thunder  /mnt/thunder       #家目录下的 thunder 是实际目录， /mnt/xunlei是挂载到的目录

2. 重启

        ./portal -s
        ./portal

3. 查看运行状态  
接下来看到迅雷运行成功之后，在其他设备上，或者有图形界面的系统也可以在raspberry上，
登陆这个网页`http://raspberry's IP:9000/getsysinfo`  
比如我的raspberry地址是192.168.1.120，我就登陆http://192.168.1.120:9000/getsysinfo
然后会看到这个:
>[ 0, 1, 1, 0, "7DHS94", 1, "201_2.1.3.121", "shdixang", 1 ]

其中有用的几项为：

- 第一项：0表示返回结果成功
- 第二项：1表示检测网络正常，0表示检测网络异常
- 第四项：1表示已绑定成功，0表示未绑定
- 第五项：未绑定的情况下，为绑定的需要的激活码
- 第六项：1表示磁盘挂载检测成功，0表示磁盘挂载检测失败

### 参考
1. 官方论坛：[http://g.xunlei.com/forum-51-1.html](http://g.xunlei.com/forum-51-1.html)  
2. [http://forum.cubietech.com/forum.php?mod=viewthread&tid=1669](http://forum.cubietech.com/forum.php?mod=viewthread&tid=1669)
