---
title: vim
date: 2014-07-10
update: 2016-11-17
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
12. `"D:\Program Files\Vim\vim73\gvim.exe" -p --remote-tab-silent "%*"` Windows 下新标签打开
13. 自动补全时，使用 C-n C-p 选择补全项目。
14. vim with python support in debian.
	sudo apt-get install vim-nox

15. vim 修改 bc 中的小数点位数。`%s/ \(\d*\) USD/ \1.00 USD`
16. specific lines sub: :10,100s/pattern/blah/

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


## Commands
### regex
查找替换实例：
- `%s/"\(\d\{32}\)" ""/"Beiwo" "\1"`
	- 匹配 `\(\)` 后面用 `\1`
	- 重复模式 `\{num, num}`
### setttings

	set syntax = apdl

### cursor movement
- hjkl
- C-f C-b
- %
- w 跳转到词首
- W jump by words
- e 跳转到词尾
- E
b
B
O start of line
^
$
gg
gd
[N]G

* marks
	:marks 查看当前所有书签
	ma a为小写字母，为光标所在处设定文档书签a
	mA A为大写字母，为光标所在处设定全局书签A
	\`a 到文档书签a处，Tab键上方
	'a 到文档书签a所在行行首处，Enter键左边
	\`A 到全局书签A处，Tab键上方
	'A 到全局书签A所在行行首处，Enter键左边
	\`n 如果n=0，缓冲区将打开上一次的文档，且光标在上次编辑最后的位置，1-9以此类推
	'n 如果n=0，缓冲区将打开上一次的文档，且光标在上次编辑最后的位置所在行的行首，1-9以此类推

### insert mode

### editing
:qa(未对文件做过修改，直接退出)
:qa! (不保存文件退出)
:wqa(保存文件并退出)


### cut and paste
d line\_number gg
s
Delete character at cursor and substitute text.

S
Delete line and substitute text.

### visual mode

### search/replace
	* 向下搜索光标所在处的单词（完全匹配）
	# 向上搜索光标所在处的单词（完全匹配）
	g* 向下搜索光标所在处的单词（部分匹配）
	g# 向上搜索光标所在处的单词（部分匹配）
	
	# 扫描当前目录下的.txt 和 .cpp文件，并加入到参数列表
	:args *.txt *.cpp
	
	# 递归扫描所有下级目录的话
	:args **/*.txt
	
	# 只想扫描下一级目录（即不扫描当前目录）的话
	:args */*.txt
	
	# 是将参数列表中的所有文件的hate提换成love，并写入硬盘
	# 如果没有|update，就不会写入，但相应的替换也会被中断）。
	:argdo %s/hate/love/gc | update



### exiting

### windows and multi-file

	:split filename
	:vsplit filename
	<C-w>s
	<C-w>v
	Ctrl+w+方向键   切换到前／下／上／后一个窗格 
	Ctrl+w+h/j/k/l  同上 
	Ctrl+ww         依次向后切换到下一个窗格中
	:q[uit] close the currently active window
	:on[ly] close all windows except the currently active window    
	ctrl-w +    increase height of current window by 1 line
	ctrl-w -    decrease height of current window by 1 line
	ctrl-w _    maximise height of current window
	ctrl-w |    maximise width of current window    
	
	:n          编辑下一个文档。 
	:2n        编辑下两个文档。 
	:N          编辑上一个文档。注意，该方法只能用于同时打开多个文档。 
	:e 文档名        这是在进入vim后，不离开 vim 的情形下打开其他文档。 
	:e# 或 Ctrl+ˆ      编辑上一个文档,用于两个文档相互交换编辑时使用。?# 代表的是编辑前一次编辑的文档 
	:files 或 :buffers 或 :ls     可以列出目前 缓冲区 中的所有文档。加号 + 表示 缓冲区已经被修改过了。＃代表上一次编辑的文档，%是目前正在编辑中的文档 
	:b 文档名或编号      移至该文档。 
	:f  或 Ctrl+g     显示当前正在编辑的文档名称。 
	:f name         改变编辑中的文档名。(file)

### macros

### buffer

	:ls 查看当前打开文件列表
	:bp 前一文件
	:bn 后一文件
	N+Ctrl+^ 跳转到编号N的文件
	Ctrl+^ 跳转下一个文件
	:buffer N
	:b N
	:bd close current buffer file

### table
vim 从 vim7 开始加入了多标签切换的功能， 相当于多窗口.
之前的版本虽然也有多文件编辑功能， 但是总之不如这个方便啦。
:tabnew [++opt选项] ［＋cmd］ 文件            建立对指定文件新的tab
:tabc       关闭当前的tab
:tabo       关闭所有其他的tab
:tabs       查看所有打开的tab
:tabp      前一个
:tabn      后一个
标准模式下：
gt , gT 可以直接在tab之间切换。

还有很多他命令 :help table

### vimgrep

vimgrep是gvim内部集成的一个查找文件命令，可以方便的搜索多个文件，虽然不如外部的命令速度快，但也很实用，特别在大工程文件要查找特定的关键字的时候，格式如下：
 
vimgrep /pattern/ file
patern代表的是你要搜索的内容，可以用正则表达式
file代表的是文件名，文件名也可以用正则表达式，特别是**，下面说明一下**的用法：
	** 代表的是递归查找大于100层目录，例如：
	**/*.c，所有目录下的 a.c


下面就举一下常用的例子：
:vimgrep /test/ \*  说明： 查找当前目录下所有包含test关键字
:vimgrep /test/ \*\*  说明： 递归查找当前目录下所有包含test关键字
:vimgrep /\<test\>/ \*\*  说明： 递归查找当前目录下所有包含只有test关键字,不包括testabc、abctest、abctestabc等等，如果一行有多个test的话，只搜索一个test结果
:vimgrep /\<test\>/g \*\*  说明： 递归查找当前目录下所有包含只有test关键字,不包括testabc、abctest、abctestabc等等，如果一行有多个test的话，搜索多个test结果
:vimgrep /\<test\>/ \*.html 说明： 查找当前目录下所有的html文件包含只有test关键字,不包括testabc、abctest、abctestabc等等，如果一行有多个test的话，搜索多个test结果
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

	:set diffopt=context: 5
	vimdiff filea fileb
	]c 移动到下一个diff
	[c 移动到上一个diff
	
	:diffput
	
	:diffget
	
	:diffupdate

### fold

	zo 打开折叠
	zc 保存退出
	:set diffopt=context: 5
	:set foldmethod = syntax/


---- 
## Plugin
---- 
### vundle
[Github][1]

- 在Windows下使用Vundle  
	[Vundle for Windows]
(https://github.com/gmarik/vundle/wiki/Vundle-for-Windows)
需要注意环境变量的设置。

- 常用命令
BundleInstall，安装插件

手动安装插件：
1. 下载 git 包，到 bundle 目录
2. vimrc 中添加插件名
3. note for update by hand often. watch for GitHub repo update.


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
自动在 rtp runtime path 寻找可用的 snippets，windows 下手动将 $VIM/.vim 加入 rtp 

### utilsnip
pair with vim-snip
personal snippets in \~/.vim/snippets/\_.snippet

### vim-snippet
pre-defined snippets

### vim-multiple-cursors
ST的特性，华丽。代码托管在
[Github][2]

### VOoM
文本文件outliner。详见
[xbeta][3]


需要Python 环境，windows 8 64bit 下需要安装
32bit Python 2.7 (配合Gvim7.3 32bit)。否则提
示无法加载库python27.dll。
安装vimpdb 之后出现问题，reinstall 解决。

### NERDTree
与自带的 netrw 在一定程度上相似，but they are different things. So I choose netrw.

REF:
- [https://www.reddit.com/r/vim/comments/22ztqp/why\_does\_nerdtree\_exist\_whats\_wrong\_with\_netrw/][4]
- [http://vimcasts.org/blog/2013/01/oil-and-vinegar-split-windows-and-project-drawer/][5]

### netrw

	renanme: R
	:[N]Explore[!]  [dir]... Explore directory of current file      *:Explore*

### vim-vinegar
supplement to netrw

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
`let g:vim_markdown_folding_disabled=1`

:Toc 生成目录
### zoom
+ :zoomin
- :zoomout
  :zoomreset

### snipMate
:help snipMate

function<TAB>

### tabular
https://github.com/godlygeek/tabular
http://vimcasts.org/episodes/aligning-text-with-tabular-vim/

### CtrlP
kien/ctrlp.vim 使用模糊匹配搜索/打开文件，非常好用，强烈推荐 

### vim-fugitive
:help fugitive

### vim-airline

### vim-powerline

	"" Powerline
	set laststatus=2   " Always show the statusline
	"let g:Powerline_symbols = 'unicode'
	"let g:Powerline_colorscheme = 'skwp'
	"let g:Powerline_symbols = 'fancy'

[1]:	https://github.com/gmarik/vundle
[2]:	https://github.com/terryma/vim-multiple-cursors
[3]:	http://xbeta.info/vim-voof.htm
[4]:	https://www.reddit.com/r/vim/comments/22ztqp/why_does_nerdtree_exist_whats_wrong_with_netrw/
[5]:	http://vimcasts.org/blog/2013/01/oil-and-vinegar-split-windows-and-project-drawer/