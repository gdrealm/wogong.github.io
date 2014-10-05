---
layout: wiki
title: openwrt
create: 2014-06-07
update: 2014-09-24
---

/etc/config/wireless --> open wireless

1. 时区设置 /etc/config/system

    ntpclient -s -t -h 0.openwrt.pool.ntp.org  不是自带的。
    config 'system'
            option 'hostname' 'OpenWrt'
            option 'zonename' 'Asia/Shanghai'
            option 'timezone' 'CST-8'

2. 3G
    opkg install chat--
    opkg install comgt--
    opkg install kmod-nls-base
    opkg install kmod-scsi-core
    opkg install libusb--
    opkg install kmod-usb-acm
    opkg install kmod-usb-core
    opkg install kmod-usb-serial-option--
    opkg install kmod-usb-serial-wwan--
    opkg install usb-modeswitch--
    opkg install usb-modeswitch-data
    opkg install kmod-usb-storage

3. reset
方法很简单，先进入failsafe模式，开机，等着一个工作灯亮的时候立即按下rest键2秒，然后就开始拼命闪烁，很好现在进入安全模式了。telnet 192.168.1.1
    - 忘记密码 passwd
    - 恢复出厂设置 `firstboot`

4. backup
http://wiki.openwrt.org/doc/howto/generic.backup
Backup your configuration： `cd /etc; tar cvz config > openwrt.tar.gz`

5. luci
http://wiki.openwrt.org/doc/howto/luci.essentials

    opkg update && opkg install luci
    /etc/init.d/uhttpd start/enable

## sample config
1. default wireless

    config wifi-device  radio0
            option type     mac80211
            option channel  11
            option hwmode   11g
            option path     'platform/ar933x_wmac'
            option htmode   HT20
            # REMOVE THIS LINE TO ENABLE WIFI:
            option disabled 0

    config wifi-iface
            option device   radio0
            option network  lan
            option mode     ap
            option ssid     wogong
            option encryption psk2
            option key        passwd

2. repeater
    - /etc/config/network

        config interface 'wwan'
            option proto 'dhcp'

        config openwrt-wwan 'hostname'
    
    - /etc/config/firewall

        config zone
        option name 'wan'
        option input 'REJECT'
        option output 'ACCEPT'
        option forward 'REJECT'
        option masq '1'
        option mtu_fix '1'
        option network 'wan wwan'

    - /etc/config/firewall

        config wifi-iface
                option device 'radio0'
                option ssid 'wan ssid'
                option encryption 'psk2+aes'
                option key 'passwd'
                option network 'wwan'
                option mode 'sta'

        config wifi-iface
                option device   radio0
                option network  lan
                option mode     ap
                option ssid     repeater ssid
                option encryption psk2
                option key        passwd


## DNS
1. FreeRouter 方式
2. ChinaDNS-C Github
-s 127.0.0.1,8.8.8.8




经验
root@OpenWrt:~# sysupgrade /tmp/openwrt-ar71xx-generic-tl-mr11u-v1-squashfs-sysupgrade_6.09.bin
Saving config files...
Sending TERM to remaining processes ... crond dnsmasq ser2net ntpd syslogd klogd hotplug2 ubusd netifd 
Sending KILL to remaining processes ... 
Switching to ramdisk...
Performing system upgrade...
Unlocking firmware ...
 
Writing from <stdin> to firmware ...  [w]
Appending jffs2 data from /tmp/sysupgrade.tgz to firmware...TRX header not found
Error fixing up TRX header
 
Upgrade completed
Rebooting system...
刷机过程
用telnet进入，passwd修改默认密码比如damndamn，然后路由器会自动ssh模式，此时telnet会开始无效，以后ssh登录路由器的时候带上id（ssh root@192.168.1.1，否则是不会以当前用户id进入的，mac里会这样）。
下载WINSCP
用scp协议连接到路由器，（有个麻烦对话框可以关闭查找用户组），然后上传文件到tmp。
用winscp里的打开终端，sysupgrade /tmp/openwrt-ar71xx-generic-tl-wr703n-v1-squashfs-sysupgrade.bin
直接开始刷固件。
若干秒后，刷机完成。