---
layout: wiki
title: vmware
date: 2014-09-09
update: 2014-09-09 21:15:47
---

1. 合并 vmdk 文件
vmware-vdiskmanager.exe -r /f/Vmware/arch/Arch.vmdk -t 0 VM.vmdk

执行结果：

    $ vmware-vdiskmanager.exe -r /f/Vmware/arch/Arch.vmdk -t 0 VM.vmdk
      Creating disk 'VM.vmdk'
      Convert: 100% done.
    Virtual disk conversion successful.

2. 问题描述：当用 VMware Workstation 打开后缀vmx 文件时，出现 "This virtual machine appears to be in use."的提示信息框！
分析：
   - VMX文件是虚拟机的参数文件.
   - VMDK文件是虚拟机的磁盘文件。
   - 其它有文件均虚拟机启动后生成临时文件，正常退出后虚拟机会自动删除这些文件，当虚拟机运行为了防止第二次打开会先判断这些文件是否存在。由于断电后，虚拟机没有正常关闭而没有删除这些文件，所以会出现上述问题。
解决：
   - 找到当前在虚拟系统目录中（也就是后缀是vmx 文件的目录），找到后缀.lck文件夹删除


   sudo mount -t vmhgfs .host:/wind /mnt/D

3. 制作启动U盘时，为了方便测试，可以将U盘当作硬盘添加到虚拟机，bios设置从硬盘启动。
