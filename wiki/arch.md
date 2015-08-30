title: arch
date: 2014-07-18
modified: 2015-07-12 19:23:27

1. screen backlight: xbackloght -set 10

2. 交换CapsLock和Ctrl	http://www.emacswiki.org/emacs/MovingTheCtrlKey#toc6

3. ibus-rime pacman -S ibus-rime
同步也是很简单的事情。以后添加到Dropbox同步。
IBus has been started! If you cannot use IBus, add the following lines to your $HOME/.bashrc; then relog into your desktop.
  export GTK_IM_MODULE=ibus
  export XMODIFIERS=@im=ibus
  export QT_IM_MODULE=ibus

4. Xterm
http://tuhaihe.com/2013/10/16/xterm-discover.html
https://wiki.archlinux.org/index.php/Xterm

5. Time
sudo pacman -S openntpd
sudo systemctl start openntpd
sudo systemctl enable openntpd

6. sda 
https://wiki.archlinux.org/index.php/NTFS-3G_%28%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%29
sda1 boot
sda2 F
sda3 ？
sda4 Arch
sda5 D
sda6 E

7. CPU 
实时调整CPU频率
https://wiki.archlinux.org/index.php/CPU_Frequency_Scaling_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

8. 温度
sudo pacman -S lm_sensors
sensors

9. 待机
sudo pm-suspend

10. I3
https://wiki.archlinux.org/index.php/i3_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#.E4.BE.BF.E7.AC.BA.E6.9C.AC
http://i3wm.org/docs/userguide.html#_using_workspaces

11.  wallpaper https://wiki.archlinux.org/index.php/Feh

i3status
Using i3status I believe you can change your configuration slightly so that it get's the CPU's core temperature directly from the /sys by providing a path to it's value. So change your rule to something like this:

order += "cpu_temperature 1"
# and more if you like...
# order += "cpu_temperature 2"

#...   
cpu_temperature 1 {
        format = "T: %degrees °C"
        path = "/sys/devices/platform/coretemp.0/temp1_input"
}

# cpu_temperature 2 {
#        format = "T: %degrees °C"
#        path = "/sys/devices/platform/coretemp.0/temp2_input"
# }
Here are 4 other ways to get your temp:
/proc
$ cat /proc/acpi/thermal_zone/THM0/temperature
temperature:             72 C
acpi
$ acpi -t
Thermal 0: ok, 64.0 degrees C
From the acpi man page:

   -t |  --thermal
             show thermal information
/sys
$ cat /sys/bus/acpi/devices/LNXTHERM\:01/thermal_zone/temp 
70000
lm_sensors
If you install the lmsensors package like so:

Fedora/CentOS/RHEL:

$ sudo yum install lm_sensors
Debian/Ubuntu:

$ sudo apt-get install lm-sensors
Detect your hardware:

$ sudo sensors-detect
You can also install the modules manually, for example:

$ sudo modprobe coretemp
$ modprobe i2c-i801
NOTE: The sensor-detect should detect your specific hardware, so you might need to modprobe <my driver> instead for the 2nd command above.

On my system I have the following i2c modules loaded:

$ lsmod | grep i2c
i2c_i801               11088  0 
i2c_algo_bit            5205  1 i915
i2c_core               27212  5 i2c_i801,i915,drm_kms_helper,drm,i2c_algo_bit
Now run the sensors app to query the resulting temperatures:

$ sudo sensors
acpitz-virtual-0
Adapter: Virtual device
temp1:        +68.0°C  (crit = +100.0°C)

thinkpad-isa-0000
Adapter: ISA adapter
fan1:        3831 RPM
temp1:        +68.0°C  
temp2:         +0.0°C  
temp3:         +0.0°C  
temp4:         +0.0°C  
temp5:         +0.0°C  
temp6:         +0.0°C  
temp7:         +0.0°C  
temp8:         +0.0°C  

coretemp-isa-0000
Adapter: ISA adapter
Core 0:       +56.0°C  (high = +95.0°C, crit = +105.0°C)

coretemp-isa-0002
Adapter: ISA adapter
Core 2:       +57.0°C  (high = +95.0°C, crit = +105.0°C)



0. X230 arch wiki 触控板 小红点
https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_X230#TrackPoint_scrolling_.28wheel_emulation.29
https://wiki.archlinux.org/index.php/TrackPoint

0. 51nb 指导
http://forum.51nb.com/thread-1357766-1-1.html
bigegle
https://bigeagle.me/2014/06/archlinux-install-for-beginners/


i3status
Using i3status I believe you can change your configuration slightly so that it get's the CPU's core temperature directly from the /sys by providing a path to it's value. So change your rule to something like this:

order += "cpu_temperature 1"
# and more if you like...
# order += "cpu_temperature 2"

#...   
cpu_temperature 1 {
        format = "T: %degrees °C"
        path = "/sys/devices/platform/coretemp.0/temp1_input"
}

# cpu_temperature 2 {
#        format = "T: %degrees °C"
#        path = "/sys/devices/platform/coretemp.0/temp2_input"
# }
Here are 4 other ways to get your temp:
/proc
$ cat /proc/acpi/thermal_zone/THM0/temperature
temperature:             72 C
acpi
$ acpi -t
Thermal 0: ok, 64.0 degrees C
From the acpi man page:

   -t |  --thermal
             show thermal information
/sys
$ cat /sys/bus/acpi/devices/LNXTHERM\:01/thermal_zone/temp 
70000
lm_sensors
If you install the lmsensors package like so:

Fedora/CentOS/RHEL:

$ sudo yum install lm_sensors
Debian/Ubuntu:

$ sudo apt-get install lm-sensors
Detect your hardware:

$ sudo sensors-detect
You can also install the modules manually, for example:

$ sudo modprobe coretemp
$ modprobe i2c-i801
NOTE: The sensor-detect should detect your specific hardware, so you might need to modprobe <my driver> instead for the 2nd command above.

On my system I have the following i2c modules loaded:

$ lsmod | grep i2c
i2c_i801               11088  0 
i2c_algo_bit            5205  1 i915
i2c_core               27212  5 i2c_i801,i915,drm_kms_helper,drm,i2c_algo_bit
Now run the sensors app to query the resulting temperatures:

$ sudo sensors
acpitz-virtual-0
Adapter: Virtual device
temp1:        +68.0°C  (crit = +100.0°C)

thinkpad-isa-0000
Adapter: ISA adapter
fan1:        3831 RPM
temp1:        +68.0°C  
temp2:         +0.0°C  
temp3:         +0.0°C  
temp4:         +0.0°C  
temp5:         +0.0°C  
temp6:         +0.0°C  
temp7:         +0.0°C  
temp8:         +0.0°C  

coretemp-isa-0000
Adapter: ISA adapter
Core 0:       +56.0°C  (high = +95.0°C, crit = +105.0°C)

coretemp-isa-0002
Adapter: ISA adapter
Core 2:       +57.0°C  (high = +95.0°C, crit = +105.0°C)


openconnect Failed to open tun device: No such device

    [root@localhost net]# find /lib/modules/ -iname 'tun.ko.gz'
    /lib/modules/3.15.1-1-ARCH/kernel/drivers/net/tun.ko.gz
    [root@localhost net]# insmod /lib/modules/3.15.1-1-ARCH/kernel/drivers/net/tun.ko.gz
    [root@localhost net]# lsmod | grep tun
    tun                    20931  0 
    [root@localhost net]#
