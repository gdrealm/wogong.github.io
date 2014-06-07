---
layout: wiki
title: openwrt
create: 2014-06-07
update: 2014-06-07
---

ntpclient -s -t -h 0.openwrt.pool.ntp.org
config 'system'
        option 'hostname' 'OpenWrt'
        option 'zonename' 'Asia/Shanghai'
        option 'timezone' 'CST-8'



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

