---
layout: wiki
title: svn
date: 2015-06-17
---

# SUBVERSION or SVN

Google Code 目前使用的版本管理。

    # Non-members may check out a read-only working copy anonymously over HTTP.
    svn checkout http://calibre2opds.googlecode.com/svn/trunk/ calibre2opds-read-only

svn update

## svn diff 使用vimdiff

在svn的手册里有diffwrap.sh这样一个脚本：

    #!/bin/sh
    # 配置你喜欢的diff程序路径
    DIFF="vimdiff"
    # SVN diff命令会传入两个文件的参数 
    LEFT=${6}
    RIGHT=${7}
    # 拼接成diff命令所需要的命令格式
    $DIFF $LEFT $RIGHT

把这个文件改名为svndiff，放在/usr/local/bin/目录里，并给执行权限
然后修改~/.subversion/config文件，将其中


    # diff-cmd = diff_program (diff, gdiff, etc.)

修改成

    diff-cmd = /usr/local/bin/svndiff现实效果如下：

