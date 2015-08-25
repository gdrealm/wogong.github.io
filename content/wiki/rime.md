title: rime
date: 2015-03-03
modified: 2015-08-02 19:40:27


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
2. copy default.custom.yml to config dir
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

2. 双拼

记忆双拼口诀

只要记住以下口诀即可：
>棉球鞋，更松软，书痴靠您来追贼，分行；
>m-ian q-iu x-ie g-eng s-ong r-uan sh-u ch-i k-ao n-in l-ai zh-ui z-ei f-en h-ang
>（以下是不能相拼的）
>哇呀，私用日元急案，特约此药剥藕，破文韵，得汪洋。
>w-uaia s-iong r-van j-an t-ue c-iao b-ou p-unvn d-uangiang
>（ing在微软中是；键，在自然码中是y键。ui是v,uai是y,和该字母英文读音一样）


双拼对于单音节的处理：
每个汉字都是单音节的，你指的是只有一个字母作为拼音，或者是只有韵母没有声母？不同输入法是不一样的，有的是直接输入韵母的第一个字母作为第一键，有的是先输入一个代表零声母的字母（一般是“O”），第二键则输入韵母。


