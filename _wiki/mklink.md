---
title: mklink
date: 2015-06-17
update: 2015-07-21 19:51:14
---

Windows 下类似于 Linux 中命令 `ln`

    Creates a symbolic link.
    MKLINK [[/D] | [/H] | [/J]] Link Target
    
            /D      Creates a directory symbolic link.  Default is a file
                    symbolic link.
            /H      Creates a hard link instead of a symbolic link.
            /J      Creates a Directory Junction.
            Link    specifies the new symbolic link name.
            Target  specifies the path (relative or absolute) that the new link
                    refers to.

mklink 命令简介
Windows 7 下的 mklink 命令通过指定参数可以建立出不同形式的文件或目录链接，
分为硬链接(hard link)、符号链接(symbolic link)和软链接（联接）(junction)三种。
1.符号链接(symbolic link)
建立一个软链接相当于建立一个文件（或目录），这个文件（或目录）用于指向别的
文件（或目录），和 win 的快捷方式有些类似。删除这个链接，对原来的文件（或目
录）没有影像没有任何影响；而当你删除原文件（或目录）时，再打开链接则会提示
“位置不可用”。
2.软链接（联接）(junction)
作用基本和符号链接类似。区别在于，软链接在建立时会自动引用原文件（或目录）
的绝对路径，而符号链接允许相对路径的引用。
3.硬链接(hard link)
建立一个硬链接相当于给文件建立了一个别名，例如对 1.TXT 创建了名字为 2.TXT 的
硬链接，若使用记事本对 1.TXT 进行修改，则 2.TXT 也同时被修改，若删除 1.TXT，
则 2.TXT 依然存在，且内容与 1.TXT 一样。
建立链接请注意：
1、建立文件或目录链接限于 NTFS 文件系统，符号（软）链接的建立可以跨文件系
统；
2、硬链接只能用于文件，不能用于目录，符号（软）链接可以为目录建立链接；
3、硬链接只能建立同一分区内的文件指向；
4、硬链接不允许对空文件建立链接，符号（软）链接可以。
Mklink 的参数定义
无参数指定：建立文件的符号链接。无参数指定的默认情况下，建立的是文件的符号
链接，删除链接文件不会影响源文件，
/d：建立目录的符号链接符号链接(symbolic link)
/j：建立目录的软链接（联接）(junction)
/h：建立文件的硬链接(hard link)
命令格式：mklink /d(定义参数) \MyDocs(链接文件) \Users\User1\Documents(原
文件)
