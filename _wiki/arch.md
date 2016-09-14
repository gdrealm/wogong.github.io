---
title: arch
date: 2014-07-18
modified: 2015-07-12 19:23:27
---

Install Arch Linux on Vultr instance using custom ISO

[1] <https://wiki.archlinux.org/index.php/Installation_guide>
[2] <https://www.vultr.com/docs/installing-arch-linux-on-a-vultr-server>
[3] <http://bao3.org/14518870323173.html>

## note
1. screen backlight: xbackloght -set 10

2. 交换CapsLock和Ctrl	http://www.emacswiki.org/emacs/MovingTheCtrlKey#toc6

3. ibus-rime pacman -S ibus-rime
同步也是很简单的事情。以后添加到Dropbox同步。
IBus has been started! If you cannot use IBus, add the following lines to your $HOME/.bashrc; then relog into your desktop.

    export GTK_IM_MODULE=ibus
    export XMODIFIERS=@im=ibus
    export QT_IM_MODULE=ibus

4. Xterm
- http://tuhaihe.com/2013/10/16/xterm-discover.html
- https://wiki.archlinux.org/index.php/Xterm

5. Time

    sudo pacman -S openntpd
    sudo systemctl start openntpd
    sudo systemctl enable openntpd

6. sda  <https://wiki.archlinux.org/index.php/NTFS-3G_%28%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%29>

7. CPU 
实时调整CPU频率
<https://wiki.archlinux.org/index.php/CPU_Frequency_Scaling_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)>

8. 温度

    sudo pacman -S lm_sensors
    sensors

9. 待机

    sudo pm-suspend

10. I3
- <https://wiki.archlinux.org/index.php/i3_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#.E4.BE.BF.E7.AC.BA.E6.9C.AC>
- <http://i3wm.org/docs/userguide.html#_using_workspaces>

11. wallpaper <https://wiki.archlinux.org/index.php/Feh>

12. Using i3status I believe you can change your configuration slightly so that it get's the CPU's core temperature directly from the /sys by providing a path to it's value. So change your rule to something like this:

## pacman

## systemd
1. timer
官方文档：<https://wiki.archlinux.org/index.php/Systemd/Timers>
参考链接：
    - <http://joelhy.github.io/2015/06/18/backup-database-using-systemd-timer/>
    - <https://cfarm.blog.aznc.cc/%E4%BD%BF%E7%94%A8-systemd-timer-%E4%BB%A3%E6%9B%BF-crontab/>
