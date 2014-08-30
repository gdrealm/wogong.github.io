---
layout: wiki
title: ssh
create: 2014-06-29
update: 2014-08-29
---

Secure Shell

1. 生成密钥对 key
`ssh-keygen -t rsa -C name@domain.com`  
将www-data加入用户组,ssh密钥登陆会失效。使用VPS得到的教训。
2. `scp`
3. 本地7070端口代理，使用端口转发 `ssh -qTfnN -D 7070 xxx@x.x.x.x -p port`


# ssh-agent
You might need to start ssh-agent before you run the ssh-add command:

    eval `ssh-agent -s`
    ssh-add
    ssh-add -L
    ssh-add -D move all identity

## 配置
1. `/etc/ssh/sshd_config`  
修改配置文件之后需要重启ssh服务。

        Port 22 # ubuntu 下使用非22端口貌似会出问题
        PubkeyAuthentication yes  # 公钥登录  
        PasswordAuthentication no # 禁用密码

2. `~/.ssh/config`  
sample config: `/etc/ssh/ssh_config`  
配置服务器登录别名，以及使用多个证书。之后采用`ssh name`即可快速登录服务器。

        Host name  
            Hostname name.wogong.net  
            Port 22
            User username  
            IdentityFile ~/.ssh/id_rsa


## windows下的ssh客户端
常用的有putty, secure CRT, xshell。之前一直在使用putty，最近转移到xshell。
* putty胜在简洁，历史悠久。但是会话信息保存在注册表中（`[HKEY_CURRENT_USER\Software\SimonTatham]`
），备份转移什么的需要导出导入虽然也有[便携版本](http://portableapps.com/apps/internet/putty_portable)，但是基本也是和注册表打交道（其实就是将配置备份在文件中，每次装载程序时导入注册表），不是很方便。
* secure CRT 需要注册，没有使用过，不多做评价。
* xshell
  - 唯一让我不满意的地方是图标太丑了，其他功能都很完善。会话信息保存在`%APPDATA%\NetSarang\Xshell\Sessions`，备份相对来说比较简单。
  - 快捷键可以自定义，默认的也很方便。当然也有便携版本，会话信息保存在程序文件目录下。更改设置
  - xagent 启用后再次打开需要先关闭xagent，否则找不到证书也无法导入。


## 差网速条件下解决方案
1. 开启ssh客户端（如putty）内建的Local Echo和Local Line Editing支持。
本地编辑好一句话以后再发送到服务器端执行。
不过这样的话你就无法使用命令行提供的特殊功能（比如自动完成等）
，也没法使用终端下的编辑器了。
2. mosh  
   参考资料：
   - https://library.linode.com/networking/mosh
   - http://mosh.mit.edu/

mosh 出现 locale 错误，从客户端和服务端两个方面检查。
