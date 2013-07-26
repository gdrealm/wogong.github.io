---
layout: post
title: "虚拟机中的 Gollum 运行缓慢"
description: "gollum in vmware runs extremely slow"
category: it
tags: [gollum, webrick, vmware]
---
{% include JB/setup %}

在家，告别了学校的百兆网络。目前3G 过活。无奈发现虚
拟机中的gollum 运行极度缓慢，Chrome 的开发者工具显示
waiting time 达到了10+ seconds。遂至Github 的官方repo
中搜索"slow"，发现
[issus177](https://github.com/gollum/gollum/issues/177)
遂解决。

same problem, I'm here by searching slow in the repo.
Thanks @arr2036 for "One thing that can cause Gollum 
to appear like it was responding slowly is that webrick
does reverse DNS lookups by default (don't ask me why). "

This is really stupid when you setup gollum in vm(vmware)
and browser in the host machine, the IP is something 
like 192.168.8.* . and the reverse DNS lookups webrick 
does cause me 10s or more under my poor 3G network.

To resolve it, just add two lines in the hosts of vm.

        192.168.8.1 host-m
        192.168.8.101 vm

Then, Everything is OK.

话说，webrick 为甚要反向查询呢？真是坑爹。
