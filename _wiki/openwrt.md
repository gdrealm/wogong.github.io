---
layout: wiki
title: openwrt
create: 2014-06-07
update: 2014-06-11
---

1. 时区设置
    ntpclient -s -t -h 0.openwrt.pool.ntp.org
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
