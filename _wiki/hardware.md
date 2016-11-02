---
layout: wiki
title: hardware
date: 2014-06-29
---

## note
1. 电脑显示接口
   - VGA;
   - mini DP; 
   - HDMI
   - RCA 标准视频输入接口（RCA，也称AV 接口）
     标准视频输入接口（RCA），也称AV 接口，通常都是成对的白色的音频接口和黄色的视频接口，它通常采用RCA(俗称莲花头)进行连接，使用时只需要将带莲花头的标准AV 线缆与相应接口连接起来即可。  
     AV接口实现了音频和视频的分离传输，这就避免了因为音/视频混合干扰而导致的图像质量下降，但由于AV 接口传输的仍然是一种亮度/色度(Y/C)混合的视频信号，仍然需要显示设备对其进行亮/ 色分离和色度解码才能成像，这种先混合再分离的过程必然会造成色彩信号的损失，色度信号和亮度信号也会有很大的机会相互干扰从而影响最终输出的图像质量。AV还具有一定生命力，但由于它本身Y/C混合这一不可克服的缺点因此无法在一些追求视觉极限的场合中使用。

### bluetooth
1. 蓝牙耳机同时连接PC 与手机。
2. PC 连接手机，PC 键盘成为蓝牙键盘。
3. Windows 系统休眠后蓝牙连接失败，进入假死状态。需要重启蓝牙进程。
stack?
4.

### NIC
ThinkPad X230 可选网卡
1. Intel Centrino Wireless-N 2200 (2x2 BGN)
2. Intel Centrino Advanced-N 6205 AGN

### DISK
- fat32
    不支持单个文件4G （过时）

- ntfs
    现在超过4GB的U盘格式化时默认是NTFS分区，但是这种格式是很伤U盘的，因为NTFS分区是采用“日志式”的文件系统，需要记录详细的读写操作，肯定会比较伤闪盘芯片，因为要不断读写。（过时）

- exfat 
    比NTFS简单，比FAT32大，VISTA本身就支持，现在推出xp更新包exFAT只是一个折中的方案，只为U盘而生。（全称Extended File Allocation Table File System，扩展FAT，即扩展文件分配表）是Microsoft在Windows Embeded 5.0以上（包括Windows CE 5.0、6.0、Windows Mobile5、6、6.1）中引入的一种适合于闪存的文件系统，为了解决FAT32等不支持4G及其更大的文件而推出。对于闪存，NTFS文件系统不适合使用，exFAT更为适用。但是兼容性是个问题，一些电视、盒子可能不支持。
