---
layout: wiki
title: ahk
date: 2014-09-10
update: 2014-09-10
---

AutoHotKey AHK

## note
1. `;` 表示注释
1. 按键映射：
   # -- Windows
   ^ -- Ctrl
   + -- Shift
   ! -- Alt

## config

    #n::run notepad
    #j::run www.jandan.net
    ::/mail::gmail@gmail.com
    ::/gs::
    
    clipboard = 煎蛋娱乐有限公司
    ;把文字发送到剪贴板（Clipboard）
    Send ^v
    ;Send 也是很常用的命令，表示向当前程序发送按键
    return
    ;代表这一小段程序的结束。像上面只有一行的代码是不需要 return 命令的
    
    ::/dd::
    d = %A_YYYY%-%A_MM%-%A_DD%
    ;获得系统时间比如今天的时间：2007-10-21。如果需要“年”的话请替换上面的“-”。
    clipboard = %d%
    ;把 d 的值发送到剪贴板，变量是不用声明的，想引用变量的值，就在变量的前后加“%”。第二行的变量是 AHK 自带的变量。
    Send ^v
    return
    
    #IfWinActive emacs  ; 判断当前激活的窗口是否是Emacs，这是根据窗口标题实现的，如果你的标题不一样，请替换一下 
    Control::Capslock ; 把Control替换为Capslock 
    Capslock::Control   ; 把Capslock替换为Control 
    #IfWinActive
