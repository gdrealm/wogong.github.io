---
layout: wiki
title: router
date: 2015-06-17
---

## RT-N13U B1 
入手Asus RT-N13U B1，TFTP刷机总是失败，一点反应没有，
win7 64bit系统。遂搜索至台湾某网站，利用asus官网软件
刷openwrt成功。记录刷机的步骤于此：

1. 下载安装ASUS Firmware Restoration。
2. 下载对应的3rd-party Firmware，tomato、ddwrt或者openwrt。
3. 把网线插上RT-N16的LAN。
4. 先开启 Firmware Restoration，选择正确的 Firmware 后
先别上载。
5. 把RT-N16的电源都拔除后，按住Reset不放(不是WPS按
钮，很多人都搞混了)，再把电源插上，等约3-5秒会看到
RT-N16的前面板电源灯号在闪烁，此时Reset按钮一样别放
开，点选 Firmware Restoration上载。
6. 看到上载的过程有蓝色进度条出现就可以把Reset放掉，
当完成100%上传后，等个约1分钟左右让RT-N16重开机，
就可以连上192.168.1.1，账号root，密码admin。
7. 如果还是连不上，就再Reset一次，应该就可以了。

此方法适用于任何固件，包括原厂固件。上述方法应该非
常安全，若遇到死机、失败等情况重复以上步骤即可。

- update 20121216：
刷最新的openwrt之后，无法采用上述方法，不过可以直接
在网页端刷ddwrt(trx version)，具体原因不知。
- update 20130102：
在刷机时应该禁用系统其它网卡，尤其是安装虚拟机产生
的虚拟网卡，目测上次失败的原因就是因为这个。
- 今天搞定了U盘挂载的事情，需要安装一个脚本，参考文
章已经在Evernote中，有时间再整理。
- update 20130724
目前ddwrt 使用稳定。
- 

ddwrt -(FR)> openwrt   !->asus

openwrt -(web)> ddwrt
openwrt -(web)> asus

asus -(web)> ddwrt

## note
1. 如何突破电信网络对于家庭路由器使用的限制：
路由器MAC克隆不能使用和内网网卡相同的MAC地址，否则
网卡无法连接该路由。
2.

### 关于3G
我的USB 3G 网卡设备为华为e261，兼容性比较不错，配合
RT-N13U B1 使用良好。最新版的ddwrt 支持有问题，需要
手动usb_modeswitch，配置文件:
    
    DisableSwitching = 0
    EnableLogging = 0
    DefaultVendor = 0x12d1
    DefaultProduct = 0x1446
    TargetVendor = 0x12d1
    TargetProductList = "1001, 1406, 140b, 140c, 1412, 141b, 1433, 1436, 14ac, 1506"
    CheckSuccess = 20
    MessageContent = "55534243123456780000000000000011060000000000000000000000000000"
    
中国电信 3G 设置:
    Dail String：#777
    user name：ctnet@mycdma.cn
    password：vnet.mobi
    or
    Dail String：#777
    user name：card
    password：card

中国联通 3G 设置: 
    APN:3gnet 
    Access String:*99#
    User name: uninet 
    Password：空 

中国移动 3G 设置
    APN: cmnet 
    Access number 拨号号码: *99***1# 
    User name (账号) :空 
    Password (密码)  : 空
 

sun
09939097026
123456
