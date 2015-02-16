---
layout: wiki
title: vim
create: 2014-07-10
update: 2014-07-16
---

coolshell has some great vim articles about vim. when you feel boring,
you can always find some interesting things there.

http://coolshell.cn


## note

1. 改变当前文本文件编码：set fileencoding=gbk

2. "set syntax=on" in .vimrc may cause this problem: "filetype unknown Press ENTER or type command to continue ". Finally resolved.

3. 安装帮助文件：:helptags $VIM/doc 如果环境变量没有设置的话，直接在doc路径下打开vim，运行 :helptags .

4. vim 7.3以后才支持 undofile

5. Windows下使用注意环境变量的设置，%VIM%
6. `:set guifont`
7. 高亮第80列 set cc = 80
   高亮当前列 set cuc
8. TODO: spellcheck
   ]s [s
   z=
   zg
   zw
9. word count: In command mode, press g, then ctrl-g
10. :ju C-o C-i
    Use C-o to jump back to previous locations which were autosaved in a jumplist.
11. :set paste 粘贴模式

## useful commands
### basic
s
Delete character at cursor and substitute text.

S
Delete line and substitute text.

1. 强大的buffer
:ls 查看当前打开文件列表
:bp 前一文件
:bn 后一文件
N+Ctrl+^ 跳转到编号N的文件
:buffer N


### vimgrep

vimgrep是gvim内部集成的一个查找文件命令，可以方便的搜索多个文件，虽然不如外部的命令速度快，但也很实用，特别在大工程文件要查找特定的关键字的时候，格式如下：
 
vimgrep /pattern/ file
patern代表的是你要搜索的内容，可以用正则表达式
file代表的是文件名，文件名也可以用正则表达式，特别是**，下面说明一下**的用法：
** 代表的是递归查找大于100层目录，例如：
**/*.c，查找的文件可以是
1. a.c
2. dir/a.c
3. a/b/c/d/e/a.c

下面就举一下常用的例子：
:vimgrep /test/ *  说明： 查找当前目录下所有包含test关键字
:vimgrep /test/ **  说明： 递归查找当前目录下所有包含test关键字
:vimgrep /\<test\>/ **  说明： 递归查找当前目录下所有包含只有test关键字,不包括testabc、abctest、abctestabc等等，如果一行有多个test的话，只搜索一个test结果
:vimgrep /\<test\>/g **  说明： 递归查找当前目录下所有包含只有test关键字,不包括testabc、abctest、abctestabc等等，如果一行有多个test的话，搜索多个test结果
:vimgrep /\<test\>/ *.html  说明： 查找当前目录下所有的html文件包含只有test关键字,不包括testabc、abctest、abctestabc等等，如果一行有多个test的话，搜索多个test结果
搜索的结果不会立即显示出来，但可以用:copen来打开所有的搜索结果，并会打开第一个符合的文件中第一个符合的位置
 
下面是常用的搜索结果的命令：
:cnext (:cn) 当前页下一个结果
:cprevious (:cp) 当前页上一个结果
:clist (:cl) 打开quickfix窗口，列出所有结果，不能直接用鼠标点击打开，只能看
:copen (:cope) 打开quickfix窗口，列出所有结果，可以直接用鼠标点击打开
:ccl[ose] 关闭 quickfix 窗口
ctrl + ww 切换编辑窗口和quickfix窗口，在quickfix里面和编辑窗口一样jk表示上下移动，回车选中进入编辑窗口
 
最后，可以给:copen和:cn设定一个快捷键，在.vimrc里加入
map <leader>c :copen<CR>
map <leader>n :cn<CR>
map <leader>p :cp<CR>

### syntax
set syntax = apdl

根据后缀设置 syntax，see vimrc


### vimdiff

vimdiff filea fileb

移动到下一个diff：

]c
移动到上一个diff：

[c

:diffput

:diffget

:diffupdate


zo
（folding open，之所以用z这个字母，是因为它看上去像折叠着的纸）
或者打开折叠

zc
保存退出

在比较和合并告一段落之后，可以用下列命令对两个文件同时进行操作。比如同时退出：

:qa(未对文件做过修改，直接退出)
:qa! (不保存文件退出)
:wqa(保存文件并退出)

:set diffopt=context: 5





## vimrc
1. mouse设置  
set mouse=a 不可以右键粘贴，但是可以鼠标操作切换vsplit窗口
set mouse-=a 相反
2. 判断 OS

    if has('win32')
    ... 
    elseif has('unix')
    ... 
    elseif has('mac')
    ... 
    endif

----
## Plugin

### vundle
[Github](https://github.com/gmarik/vundle)

- 在Windows下使用Vundle  
[Vundle for Windows]
(https://github.com/gmarik/vundle/wiki/Vundle-for-Windows)
需要注意环境变量的设置。

- 常用命令
BundleInstall，安装插件

手动安装插件：
1. 下载 git 包，到 bundle 目录
2. vimrc 中添加插件名
3. done


### vimwiki
用过很长一段时间，由于使用的是自己的wiki语法，而且当wiki条目数量很多时，修改html模板带来的转换成本太高，所以抛弃了。

### zencoding-vim
html手写神器，目前我还没怎么使用。

### taglist
需要ctags配合生成tags文件，浏览代码必备。

    set tags=tags;
    set autochdir

注意第一个命令里的分号是必不可少的。这个命令让vim首先在当前目录里寻找tags文件，如果没有找到tags文件，或者没有找到对应的目标，就到父目录中查找，一直向上递归。因为tags文件中记录的路径总是相对于tags文件所在的路径，所以要使用第二个设置项来改变vim的当前目录。

扫描指定的源文件，找出其中所包含的语法元素，并将找到的相关内容记录下来

当前路径运行`ctags -R`

vim文件时，用用ctrl-]来执行跳转，通过ctrl+t来跳转回来就可以了

### tagbar
因为受不了 Taglist 会把 method 和 attribute 混在一起这个设定以及和 NERDTree 配合是会出现 bug，我决定将使用了快两年的它抛弃。然后找到了它的替代品，Tagbar。应该有不少 Vim 用户都在使用了吧，还没有的就赶紧换吧。


### snipmate

### vim-multiple-cursors
ST的特性，华丽。代码托管在
[Github](https://github.com/terryma/vim-multiple-cursors)

### VOoM
文本文件outliner。详见
[xbeta](http://xbeta.info/vim-voof.htm)

需要Python 环境，windows 8 64bit 下需要安装
32bit Python 2.7 (配合Gvim7.3 32bit)。否则提
示无法加载库python27.dll。
安装vimpdb 之后出现问题，reinstall 解决。

### NERDTree
碉堡。
read the help file, you'll get everything

bookmark is useful


### NERDCommenter
Want to be able to comment and uncomment code with 
a few keypresses? You need NERDCommenter. It’s 
surprising that Vim doesn’t have decent commenting 
functionality built in, but NERDCommenter fixes that.
I really only use this plugin for one single 
function: “toggle comment” with <leader>c<space>. 
That function alone is worth installing it.

### Syntastic
可以每次在保存文件时检查语法和代码。比如Python中定义了一个变量但没有用，就会高亮警告。

### calendar
calendar.vim 默认日记文件后缀为.cal, 用 Vim 安装 MarkDown 写作插件则为 .md
### vim-indent-guides

### vim-markdown
let g:vim_markdown_folding_disabled=1

### zoom
+ :zoomin
- :zoomout
  :zoomreset

### snipMate
:help snipMate

function<TAB>


## shortcut
### cursor movement
- hjkl
- C-f C-b
- %
- w
- W jump by words
- e
- E
b
B
O start of line
^
$
gg
gd
[N]G
### insert mode

### editing

### cut and paste

### visual mode

### search/replace

### exiting 

### multi-file

### macros


