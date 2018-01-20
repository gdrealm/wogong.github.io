---
layout: wiki
title: shell
date: 2014-07-17
update: 2018-01-19
---

使用 bash 内置的$RANDOM 可以产生 0-32767 之间随机数:echo $RANDOM

参数 

$1 第一个参数

## zsh
* .zshrc in dotfiles repo
* 关闭自动纠正 unsetopt correct_all
* `mv dog.{0..999}.jpg ../`


## PS1相关知识
 
 1.  提示行的转义字符：
 序列         说明  
\a            ASCII 响铃字符（也可以键入 \007）   
\d            "Wed Sep 06" 格式的日期    
\e            ASCII 转义字符（也可以键入 \033）   
\h            主机名的第一部分（如 "mybox"）   
\H            主机的全称（如 "mybox.mydomain.com"）   
\j            在此shell中通过按 ^Z 挂起的进程数  
\l            此 shell 的终端设备名（如 "ttyp4"）   
\n            换行符  
\r            回车符  
\s            shell 的名称（如 "bash"）   
\t            24 小时制时间（如 "23:01:01"）   
\T            12 小时制时间（如 "11:01:01"）   
\@            带有 am/pm 的 12 小时制时间   
\u            用户名   
\v            bash 的版本（如 2.04）   
\V            Bash 版本（包括补丁级别）  
\w            当前工作目录（如 "/home/drobbins"）   
\W            当前工作目录的“基名 (basename)”（如 "drobbins"）   
\!            当前命令在历史缓冲区中的位置   
\#            命令编号（只要您键入内容，它就会在每次提示时累加）   
\$            如果您不是超级用户 (root)，则插入一个 "$"；如果您是超级用户，则显示一个 "#"  
\xxx            插入一个用三位数 xxx（用零代替未使用的数字，如 "\007"）表示的 ASCII 字符  
\\            反斜杠  
\[            这个序列应该出现在不移动光标的字符序列（如颜色转义序列）之前。它使 bash 能够正确计算自动换行。   
\]            这个序列应该出现在非打印字符序列之后。   

 2. 颜色设置：
    颜色设置可用以下格式表示：
       " \[\e[F;B;Cm\]"
    其中，\[与\]是保证其内的非打印字符不占用行上的任何空间，这样就能使自动换行后的颜色设置正常工作了；
    \e[与m之间的内容表示设置颜色，F是前景色，B是背景色，C是代码多个颜色用分号隔开,但F、B、C顺序可变，这是因为他们的数值不冲突。
    特殊的颜色设置格式：
      "\e[0m"、"\e[m"都是通知终端将颜色（前景、背景、加粗）设置重置为默认。
 
 3. 颜色与代码表：
  颜色表：
表代码  
前景          背景              颜色  
---------------------------------------  
30             40             黑色  
31             41             紅色  
32             42             绿色  
33             43             黄色  
34             44             蓝色  
35             45             紫红色  
36             46             青蓝色  
37             47             白色  
}}}
 
表代码
代码              意义  
-------------------------  
0                 OFF  
1                 高亮显示  
4                 underline  
5                 闪烁  
7                 反白显示  
8                 不可见  



## Linux Shell学习笔记
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

