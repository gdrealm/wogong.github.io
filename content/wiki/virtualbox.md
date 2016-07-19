---
title: virtualbox
date: 2016-07-18
---

## virtualbox on Ubuntu

1. Command

后台启动VirtualBox虚拟机
　　不太习惯Linux的使用，但也很喜欢使用Linux命令操作方式和Linxu上的开发或者折腾。所以一直使用虚拟机，在Windows下用SSH连接Linux。但Virtualbox启动总会有界面出现，感觉老别扭。在网上搜了一下还真找到方法，其实Virtualbox是提供了后台启动的。只是不是默认的。

复制代码
查看有哪些虚拟机
VBoxManage list vms
 
查看虚拟的详细信息
VBoxManage list vms --long
 
查看运行着的虚拟机
VBoxManage list runningvms
 
开启虚拟机在后台运行
VBoxManage startvm <vm_name> -type headless
 
开启虚拟机并开启远程桌面连接的支持
VBoxManage startvm <vm_name> -type vrdp
 
改变虚拟机的远程连接端口,用于多个vbox虚拟机同时运行
VBoxManage controlvm <vm_name> vrdpprot <ports>
 
关闭虚拟机
VBoxManage controlvm <vm_name> acpipowerbutton
 
强制关闭虚拟机
VBoxManage controlvm <vm_name> poweroff

2. SSH

The best way to login to a guest Linux VirtualBox VM is port forwarding. By default, you should have one interface already which is using NAT. Then go to the Network settings and click the Port Forwarding button. Add a new Rule:

Host port 3022, guest port 22, name ssh, other left blank.
or from command line

VBoxManage modifyvm myserver --natpf1 "ssh,tcp,,3022,,22"
where 'myserver' is the name of the created VM. Check the added rules:

VBoxManage showvminfo myserver | grep 'Rule'
That's all! Please be sure you don't forget to install an SSH server:

sudo apt-get install openssh-server
To SSH into the guest VM, write:

ssh -p 3022 user@127.0.0.1
Where user is your username within the VM.


http://stackoverflow.com/questions/5906441/how-to-ssh-to-a-virtualbox-guest-externally-through-a-host
