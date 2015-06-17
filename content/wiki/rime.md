---
layout: wiki
title: rime
date: 2015-03-03
update: 2015-03-04
---

## note
* version
    1. Windows: Weasel
    2. Linux: fcitx-rime;ibus-rime
* about fcitx-rime
    1. Ctrl+; == clipboard
* sync
词典同步：~/.config/fcitx/rime/installation.yaml
添加 sync_dir: ' YOUR_DROPBOX/UBUNTU_ONE_HERE'

执行部分：rime_dict_manager 操作

* new start:
1. copy wogong.schemal file to config dir
2. copyt default.custom.yml to config dir
3. deploy + sync_dir + installtion id

## REF
<https://code.google.com/p/rimeime/wiki/>


## OTHER
1. fcitx

Fcitx 小技巧：巧用“快速输入”，提高文字输入效率
关于 Fcitx 的介绍我就不多说了，进入正题：
在进行文字录入时，有很多时候，会有大量重复的语句需要录入，比如：“热烈欢迎 LZ 来到地球”、“我是打酱油的~”等等
Fcitx 有没有什么的方法既能减少敲键盘的量，同时又提高重复语句的输入效率呢？
当然有！
“快速输入”现真身~！！
在“~/.config/fcitx”目录中创建一个《QuickPhrase.mb》文件，并在其中输入自己的常用语句，而后保存
排版格式为：
编码 要输入的内容
激活 Fcitx，按下 Ctrl+5 刷新一遍，按下分号键“;”，接着再敲入对应的编号，预录入的语句就出现了~
