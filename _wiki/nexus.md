---
layout: wiki
title: nexus
create: 2013-01-01
update: 2014-12-23
---

Google 四儿子

## note
0. UNLOCK
解锁会清除机器数据，所以，买来就解锁吧。

1.ROOT
   - <http://autoroot.chainfire.eu/>
   - http://forum.xda-developers.com/showthread.php?t=2025274

2. 首先进入操作系统的拨号“Dialer”界面，输入*#*#4636#*#*即可快速进入Android的工程测试模式。

3. 打开位置报告与Google Now => [LocationReportEnabler](https://github.com/GhostFlying/LocationReportEnabler) need root

4. 进入bootload 模式：
     - adb reboot bootloader
     - 关机情况下，同时按电源键+音量减键

5. 解锁 fastboot oem unlock


## 线刷OTA或官方镜像
- 前提是安装好驱动与adb tools
- Factory Images for Nexus Devices: https://developers.google.com/android/nexus/images
-  nexus4 <https://developers.google.com/android/nexus/images#occamlrx22c>

### 一般情况
1. 进入bootload模式 fastboot reboot-bootloader
2. 选择recovery mode
3. adb sideload ota.zip
4. OK

### status 7 error
1. 线刷上一版本官方镜像部分文件

    fastboot flash recovery recovery.img
    fastboot flash boot boot.img
    fastboot flash system system.img
    fastboot reboot

2. 重复一般情况步骤

### 直接线刷最新版本镜像
1. 下载镜像
2. 解压执行官方脚本（也可以手动解压一步一步安装）
3. 保留数据的话记得去除  `-w`


