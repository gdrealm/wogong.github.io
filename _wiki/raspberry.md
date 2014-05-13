---
layout: wiki
title: raspberry
---

# Raspberry

## todo


## Function
1. git repository : how to sync with Github?
2. gollum

## 外设
1. usb 转串口接线 done
2. HDMI
3. HDMI2DVI
4. 无线网卡 doing
5. usb-serial PL2303 HX (rev A)

## Install

SD Card Creation

1. Download the zip file containing the dd image from one of these resources:
   Extract the zip file to your hard drive, giving you the dd image archlinux-hf-.img
2. Write this image to the target SD card. The SD card will need to be 2GB or larger.
   - Linux
     Replacing sdX with the location of the SD card, run:  
     `dd bs=1M if=/path/to/archlinux-hf-*.img of=/dev/sdX`
   - Windows
     Download and install Win32DiskImager  
     Select the archlinux-hf-.img image file, select your SD card drive letter, and click Write
3. Eject the card from your computer, insert into the Raspberry Pi, and power it on.

If your keyboard, mouse, or other USB device doesn't appear to be working properly, try using it through a POWERED USB hub. The Raspberry Pi's USB ports are limited to 140mA. This limitation has been fixed in newer boards; however, you may still run into power issues.

The default username is 'root' with a password 'root'

### Raspbian
1. 用dd把Raspbian鏡像寫到SD卡上.[1][2]
2. 插卡, 插網線, 通電.
3. SSH連上去(用戶名pi, 密碼raspberry), `sudo raspi-config`, 按需要配置一下.
4. 如果需要配置無線網卡(免驅的), 修改/etc/network/interfaces中關於wlan0的部分:
iface wlan0 inet dhcp
wpa-ssid [你的無線網絡的SSID]
wpa-psk [你的無線網絡的密碼]
, 然後重啟網卡.


官方系統鏡像: http://www.raspberrypi.org/downloads

如果dd時提示"resource busy", 在Disk Utility裏unmount SD卡的分區.

## 无线网卡
EDUP EP-N8508GS黄金版 迷你USB无线网卡 
- 京东 http://item.jd.com/509932.html
- 官方说明 http://www.szedup.com/show.aspx?id=1680
  Realtek8188CUS
- 需要确定 chipset 究竟是何。
- 卧槽，居然是硬件问题。

Default /etc/network/interfaces file as supplied in the raspbian image - do not edit

    auto lo
    
    iface lo inet loopback
    iface eth0 inet dhcp
    
    allow-hotplug wlan0
    iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface default inet dhcp

Edit the file /etc/wpa_supplicant/wpa_supplicant.conf and add the network={.....} section. Use the command sudo nano /etc/wpa_supplicant/wpa_supplicant.conf to open and edit the file. Exit the editor and save the file using keys cntl-X, Y, Enter.

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
        ssid="Your-Network-Name"
        psk="Your-Network-Password"
    }


## 参考
http://linuxtoy.org/archives/cool-ideas-for-raspberry-pi.html
