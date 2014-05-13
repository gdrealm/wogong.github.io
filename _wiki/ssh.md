---
layout: wiki
title: ssh
---

# SSH Secure Shell

## 相关命令
1. 生成密钥对 key
`ssh-keygen -t rsa -C name@domain.com`  
将www-data加入用户组,ssh密钥登陆会失效。使用VPS得到的教训。
2. `scp`

## 配置
1. `/etc/ssh/sshd_config`  
修改配置文件之后需要重启ssh服务。

        PubkeyAuthentication yes  # 公钥登录  
        PasswordAuthentication no # 禁用密码

2. `~/.ssh/config`  
配置服务器登录别名，以及使用多个证书。之后采用`ssh name`即可快速登录服务器。

        Host name  
            Hostname name.wogong.net  
            User username  
            IdentityFile ~/.ssh/id_rsa


## windows下的ssh客户端
常用的有putty, secure CRT, xshell。之前一直在使用putty，最近转移到xshell。
* putty胜在简洁，历史悠久。但是会话信息保存在注册表中（`[HKEY_CURRENT_USER\Software\SimonTatham]`
），备份转移什么的需要导出导入虽然也有[便携版本](http://portableapps.com/apps/internet/putty_portable)，但是基本也是和注册表打交道（其实就是将配置备份在文件中，每次装载程序时导入注册表），不是很方便。
* secure CRT 需要注册，没有使用过，不多做评价。
* xshell唯一让我不满意的地方是图标太丑了，其他功能都很完善。会话信息保存在`%APPDATA%\NetSarang\Xshell\Sessions`，备份相对来说比较简单。快捷键可以自定义，默认的也很方便。当然也有便携版本，会话信息保存在程序文件目录下。

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

## 高级
1. 使用端口转发 `ssh -qTfnN -D 7070 xxx@x.x.x.x -p port`
2. 
