---
layout: wiki
title: vps
update: 2014-07-06
update: 2015-02-04
---

## 配置VPS

1. install `git tmux vim ctags curl sudo zsh`

        # arch  
        `pacman -S git tmux vim ctags curl sudo`
        # ubuntu  
        `apt-get update`
        `apt-get install sudo git tmux vim ctags curl mosh zsh openssl ca-certificates keychain`

2. add user   
   `useradd -m -g users -s /bin/zsh wogong`

4. 设置用户密码,添加sudo权限  
   `passwd <username> && visudo`

6. SSH禁用密码登陆  

        vim /etc/ssh/sshd_config
        /etc/init.d/ssh restart

3. dotfiles  
   `git clone https://github.com/wogong/dotfiles.git ~`  
   `git clone git://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting`

5. 配置vundle

        git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
        BundleInstall

7. locale 
   `dpkg-reconfigure locales`
   `/etc/locale.conf`
   `/etc/locale.gen` && `sudo locale-gen` 

8. timezone

        # ubuntu  
        sudo tzconfig`，or `dpkg-reconfigure tzdata
        # debian   
        tzselect
        sudo cp /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime
        sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
        # arch  
        timedatectl set-timezone Asia/Shanghai
9. hostname
   `/etc/hostname`
   `sudo hostnamectl set-hostname myhostname`

## VPS 评测
1. CPU  
    - `cat /proc/cpuinfo`
    - `openssl speed md5` 这样的方法快速地看一台机器的 CPU 性能，只要看最后一个数字就够了。好性能的标准是 50 万以上。

2. 内存 `free -m`
3. 硬盘 `dd if=/dev/zero of=test bs=64k count=4k oflag=dsync`
   结果，大于10M，建站就没有什么影响了。好的话，能达到70M，
   烂的也有5M+，如果K，就扔了吧。  
   ` dd if=/dev/zero of=test bs=64k count=16k conv=fdatasync`
4. 入口带宽 `wget http://cachefly.cachefly.net/100mb.test`
5. 出口带宽 `wget /file/in/your/server`
6. 网络 `ping, tracert`
   - <http://ping.chinaz.com> 
   - <http://www.webkaka.com> 
   - <http://ping.aizhan.com>
7. 稳定性 uptime
   - dndpod
8. UnixBench
   `wget http://www.CTOHome.com/linux-vps-pack/unixbench.sh;sh ./unixbench.sh;`
   很伤VPS，普通的VPS得分能在500-800之间。

## VPS提供商比较
1. BudgetVM  
    推介 <https://www.budgetvm.com/account/aff.php?aff=1061>

2. BuyVM 有余额 13$
    <https://my.frantech.ca/aff.php?aff=1332>
    he.net 的网络，不错

3. Hostigation

4. Linode  
    Referrals Code: 9bd81fd03ec9f3917cb2db12d6843d1ee2d30892
    Referrals <https://www.linode.com/?r=9bd81fd03ec9f3917cb2db12d6843d1ee2d30892>

5. DigitalOcean  
   1. 经常有一些 promo code，等于白送钱，很不错。等到近期VPS到期换DO
   2. 目前还有几个账户，余额20$；推介
       - wogong38 $129.42 -- <https://www.digitalocean.com/?refcode=4398536459b9>
   3. 测试IP：
       - 旧金山(San Francisco)：speedtest-sfo1.digitalocean.com   http://speedtest-sfo1.digitalocean.com/100mb.test     
       - 纽约(New York)：speedtest-ny1.digitalocean.com   http://speedtest-ny1.digitalocean.com/100mb.test     
       - 荷兰阿姆斯特丹(Amsterdam)：speedtest-ams1.digitalocean.com  http://speedtest-ams1.digitalocean.com/100mb.test

6. bandwagonhost --<https://bandwagonhost.com/aff.php?aff=476>

7. ramnode  
    6折 zhujiceping
    - test file
        - <http://test.sea.ramnode.com/100MB.test> 
        - <http://test.atl.ramnode.com/100MB.test>
        - <http://test.nl.ramnode.com/100MB.test>

8. VULTR  10$ 余额  
   日本机房速度不错，类似DigitalOcean 
   <http://www.vultr.com/?ref=6802768>
   - test <https://www.vultr.com/locations/>

9. VPSTO
   @showfom 推出的廉价VPS，主要用于科学上网
   <https://portal.vpsto.com/aff.php?aff=045>