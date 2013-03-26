---
layout: post
title: "SmartVPS香港节点入门套餐VPS测试"
description: "SmartVPS香港节点入门套餐VPS测试"
category: it
tags: [VPS]
---
{% include JB/setup %}

-----

- 起因：[smartVPS少量测试主机免费赠送](http://c3.orca.io/t/63630#reply59)


- 测试VPS信息

> 可选OS : CentOS, debian, ubuntu  
> 内存 : 512M（保证） ~ 1G（最大）  
> 硬盘 : 20G  
> 流量限制 : 无  
> IP地址 : IPv4 x 1 + IPv6 x 1  
> 升级:此套餐暂无选项  
> root权限 : 有  
> SSH console : 有  
> 管理界面 : 有

----

## 速度

本地环境：北京教育网

1. IPV4 ping 78ms  
ping result

		C:\Users>ping 36.54.x.x
		Pinging 36.54.x.x with 32 bytes of data:
		Reply from 36.54.x.x: bytes=32 time=76ms TTL=47
		Reply from 36.54.x.x: bytes=32 time=111ms TTL=47
		Reply from 36.54.x.x: bytes=32 time=56ms TTL=47
		Reply from 36.54.x.x: bytes=32 time=69ms TTL=47
	
		Ping statistics for 36.54.x.x:
	    	Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
		Approximate round trip times in milli-seconds:
	    	Minimum = 56ms, Maximum = 111ms, Average = 78ms
	
2. IPV6 ping 158ms  
ping result

		C:\Users>ping 2405:3700:400:203:2:1:0:3
		
		Pinging 2405:3700:400:203:2:1:0:3 with 32 bytes of data:
		Reply from 2405:3700:400:203:2:1:0:3: time=305ms
		Reply from 2405:3700:400:203:2:1:0:3: time=110ms
		Reply from 2405:3700:400:203:2:1:0:3: time=113ms
		Reply from 2405:3700:400:203:2:1:0:3: time=107ms
		
		Ping statistics for 2405:3700:400:203:2:1:0:3:
		    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
		Approximate round trip times in milli-seconds:
		    Minimum = 107ms, Maximum = 305ms, Average = 158ms

3. 全局ping测试  
如下图
<img src="http://ww3.sinaimg.cn/large/bfadf3bejw1e33bfvjp16j.jpg" width=600px/>
4. 下载速度  
 美国  
 VPS下载外部文件

			% wget http://cachefly.cachefly.net/100mb.test
			--2013-03-23 11:06:44--  http://cachefly.cachefly.net/100mb.test
			Resolving cachefly.cachefly.net... 204.93.150.151
			Connecting to cachefly.cachefly.net|204.93.150.151|:80... connected.
			HTTP request sent, awaiting response... 200 OK
			Length: 104857600 (100M) [application/octet-stream]
			Saving to: `100mb.test'	
			24% [========>                   ] 25,200,695   991K/s  eta 80s
 本地下载VPS上文件  
 chrome下载 500+kb/s  
 阿里云  
 下载VPS文件

			HTTP request sent, awaiting response... 200 OK
			Length: 104857600 (100M) [text/plain]
			Saving to: `100M.img'
			
			 4% [===>       ] 4,994,512    324K/s  eta 6m 11s  
	
	
	
-----

## 硬盘读写速度

测试硬盘 51.4M/s

	% dd if=/dev/zero of=test bs=64k count=4k oflag=dsync
	4096+0 records in
	4096+0 records out
	268435456 bytes (268 MB) copied, 5.22514 s, 51.4 MB/s

-----

## CPU、内存基本信息

CPU

	% cat /proc/cpuinfo
	processor       : 0
	vendor_id       : GenuineIntel
	cpu family      : 6
	model           : 45
	model name      :       Intel(R) Xeon(R) CPU E5-2430L 0 @ 2.00GHz
	stepping        : 7
	cpu MHz         : 798.852
	cache size      : 15360 KB
	physical id     : 0
	siblings        : 1
	core id         : 0
	cpu cores       : 1
	fpu             : yes
	fpu_exception   : yes
	cpuid level     : 13
	wp              : yes
	flags           : fpu de tsc msr pae cx8 apic sep cmov pat clflush 
                    acpi mmx fxsr sse sse2 ss ht syscall nx lm constant_tsc 
                    ida arat pni ssse3 cx16 sse4_1 sse4_2 popcnt lahf_lm
	bogomips        : 5031.29
	clflush size    : 64
	cache_alignment : 64
	address sizes   : 46 bits physical, 48 bits virtual
	power management:

内存

	% free -m
	             total       used       free     shared    buffers     cached
	Mem:          1024        312        711          0          0          0
	-/+ buffers/cache:        312        711
	Swap:            0          0          0

----

## unixbench测试

result

	   BYTE UNIX Benchmarks (Version 5.1.2)
	
	   System: hkg-vps-srv008: GNU/Linux
	   OS: GNU/Linux -- 2.6.18-194.3.1.el5.028stab069.6xen -- #1 SMP Wed May 26 18:35:38 MSD 2010
	   Machine: i686 (unknown)
	   Language: en_US.utf8 (charmap="ANSI_X3.4-1968", collate="ANSI_X3.4-1968")
	   CPU 0: Intel(R) Xeon(R) CPU E5-2430L 0 @ 2.00GHz (5031.3 bogomips)
	          Hyper-Threading, x86-64, MMX, Physical Address Ext, SYSENTER/SYSEXIT, SYSCALL/SYSRET
	   19:13:07 up 4 days,  5:56,  1 user,  load average: 0.54, 0.17, 0.05; runlevel 2

------------------------------------------------------------------------
	Benchmark Run: Tue Mar 26 2013 19:13:07 - 19:44:19
	1 CPU in system; running 1 parallel copy of tests
	
	Dhrystone 2 using register variables        3591458.9 lps   (10.0 s, 7 samples)
	Double-Precision Whetstone                     1216.1 MWIPS (10.9 s, 7 samples)
	Execl Throughput                                317.0 lps   (29.9 s, 2 samples)
	File Copy 1024 bufsize 2000 maxblocks         50510.6 KBps  (30.0 s, 2 samples)
	File Copy 256 bufsize 500 maxblocks           13009.0 KBps  (30.0 s, 2 samples)
	File Copy 4096 bufsize 8000 maxblocks        164252.2 KBps  (30.0 s, 2 samples)
	Pipe Throughput                               82899.4 lps   (10.0 s, 7 samples)
	Pipe-based Context Switching                  21736.0 lps   (10.0 s, 7 samples)
	Process Creation                                803.2 lps   (30.0 s, 2 samples)
	Shell Scripts (1 concurrent)                    657.8 lpm   (60.1 s, 2 samples)
	Shell Scripts (8 concurrent)                     87.0 lpm   (60.4 s, 2 samples)
	System Call Overhead                          69815.3 lps   (10.0 s, 7 samples)
	
	System Benchmarks Index Values               BASELINE       RESULT    INDEX
	Dhrystone 2 using register variables         116700.0    3591458.9    307.8
	Double-Precision Whetstone                       55.0       1216.1    221.1
	Execl Throughput                                 43.0        317.0     73.7
	File Copy 1024 bufsize 2000 maxblocks          3960.0      50510.6    127.6
	File Copy 256 bufsize 500 maxblocks            1655.0      13009.0     78.6
	File Copy 4096 bufsize 8000 maxblocks          5800.0     164252.2    283.2
	Pipe Throughput                               12440.0      82899.4     66.6
	Pipe-based Context Switching                   4000.0      21736.0     54.3
	Process Creation                                126.0        803.2     63.7
	Shell Scripts (1 concurrent)                     42.4        657.8    155.1
	Shell Scripts (8 concurrent)                      6.0         87.0    145.0
	System Call Overhead                          15000.0      69815.3     46.5
	                                                                   ========
	System Benchmarks Index Score                                         110.8

-----
## 总结

带宽一般，硬盘读写OK，速度可以接受，ssh操作基本流畅，值得购买。另外说个插曲，周末的时候貌似服务器被人折腾了一下，导致一段时间无法登陆。

## 后记

初次评测，基本只是列出参数，并未斗胆评价什么，欢迎各位拍砖或讨论或点评。



