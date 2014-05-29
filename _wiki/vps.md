---
layout: wiki
title: vps
---

# VPS

## 配置VPS

1. install `git, tmux, vim, ctags, curl, sudo`

        # arch  
        `pacman -S git tmux vim ctags curl sudo`
        # ubuntu  
        `apt-get update`
        `apt-get install sudo git tmux vim ctags curl mosh zsh openssl ca-certificates`

2. add user   
   `useradd -m -g users -s /bin/zsh <username>`

3. dotfiles  
   `git clone https://github.com/wogong/dotfiles.git ~`
   `git clone git://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting`

4. 设置用户密码,添加sudo权限  
   `passwd <username> && visudo`

5. 配置vundle

        git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
        BundleInstall

6. SSH禁用密码登陆  

        vim /etc/ssh/sshd_config
        /etc/init.d/ssh restart

7. locale 
   `dpkg-reconfigure locales`
   `/etc/locale.conf`
   `/etc/locale.gen` && `sudo locale-gen` 

8. timezone

        # ubuntu  
        sudo tzconfig`，or `dpkg-reconfigure tzdata
        # debian   
        debian tzselect
        sudo cp /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime
        # arch  
        timedatectl set-timezone Asia/Shanghai
9. hostname
   `/etc/hostname`
   `sudo hostnamectl set-hostname myhostname`

## VPS 评测
1. CPU `cat /proc/cpuinfo`
2. 内存 `free -m`
3. 硬盘 `dd if=/dev/zero of=test bs=64k count=4k oflag=dsync`
   结果，大于10M，建站就没有什么影响了。好的话，能达到70M，
   烂的也有5M+，如果K，就扔了吧。  
   ` dd if=/dev/zero of=test bs=64k count=16k conv=fdatasync`
4. 入口带宽 `wget http://cachefly.cachefly.net/100mb.test`
5. 出口带宽 `wget /file/in/your/server`
6. 网络 `ping, tracert`
   - http://ping.chinaz.com 
   - http://www.webkaka.com 
   - http://ping.aizhan.com
7. 稳定性 uptime
   - dndpod
8. UnixBench
   `wget http://www.CTOHome.com/linux-vps-pack/unixbench.sh;sh ./unixbench.sh;`
   很伤VPS，普通的VPS得分能在500-800之间。

## VPS提供商比较
1. BudgetVM 推介 https://www.budgetvm.com/account/aff.php?aff=1061
   10.94$
2. BuyVM 有余额
3. Hostigation
4. Linode
5. DigitalOcean
   1. 经常有一些 promo code，等于白送钱，很不错。
   2. 目前还有几个账户，余额20$；推介
   - wogong38 $29.42 -- https://www.digitalocean.com/?refcode=4398536459b9
   - do       $10    -- https://www.digitalocean.com/?refcode=2e0ea664bd28
6. bandwagonhost --https://bandwagonhost.com/aff.php?aff=476
7. ramnode 6折 zhujiceping
8. VULTR 日本机房速度不错，类似DigitalOcean 
   http://www.vultr.com/?ref=6802768
