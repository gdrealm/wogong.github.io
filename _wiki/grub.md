---
layout: wiki
title: grub
create: 2015-05-06
update: 2015-05-06
---

重转windows系统后grub修复：
利用光盘进入终端，grub：

grub>root (hd0,x)
grub>setup (hd0)

今日重装系统

用grub命令
>rootnoverify (hd0,0)
>chainloader +1

>boot