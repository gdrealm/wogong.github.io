---
layout: wiki
title: shell
---

# bash搜索历史命令：Ctrl+R
# 使用 bash 内置的$RANDOM 可以产生 0-32767 之间随机数:echo $RANDOM
# Linux Shell学习笔记
查看环境变量： env
改变shell种类： chsh -s /bin/bash （更改为bash）
禁用shell /etc/passwd /bin/false

.bashrc文件可以指定某些程序在用户登录的时候就自动启动
.bash_profile shell配置文件


1.变量
1.1本地变量
1.2环境变量
$HOME/.bash_profile)(/etc/profile)
export






env
1.3变量替换
${Variable name}
${Variable name:+value}
${Variable name:?value} 
${Variable name:-value}
${Variable name:=value} 
1.4变量清除
unset
1.5位置变量
位置变量表示：$0,$1...$9
1.6标准变量
bash默认建立了一些环境标准变量，可在/etc/profile中定义
EXINIT
HOME
IFS
LOGNAME
MAIL
MAILCHECK
MAILPATH
TERM
PATH 
TZ
PS1
PS2
PWD
SHELL
MANPATH
TERMINFO

1.7特殊变量
$#
$*
$$
$!
$@
$-
$?

1.8影响变量的命令
declare
export
readonly
set
shift
typeset 
unset


2.引号
2.1引用的必要性
2.2双引号
使用双引号引用除字符$、`、\外的任意字符或字符串。
 2.3单引号
单引号与双引号类似，不同的是shell会 忽略任何引用值。会将引号里的所有字符，包括都作为一个字符串。
# 

