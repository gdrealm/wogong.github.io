---
layout: wiki
title: sublime
date: 2014-08-26
update: 2014-09-02
---

Tutorials book: (all in calibre lib)
1. Instant Sublime Text Starter <http://book.douban.com/subject/21478309/>
2. Mastering Sublime Text <http://book.douban.com/subject/25804133/>

## note
0. Ctrl+Shift+P 是一切之门
1. 小狼毫的光标跟随问题：   
	这是Sublime的bug，不是Rime的问题，别的中文输入法也有这种情况，楼主用Package Control 安装IMESupport这个包然后重启Sublime就行了。
2. fortran support
	<https://github.com/textmate/fortran.tmbundle>
	download [tmLanguage](https://raw.githubusercontent.com/textmate/fortran.tmbundle/master/Syntaxes/Fortran%20-%20Modern.tmLanguage)
3 add date in sublime snippet. <http://stackoverflow.com/questions/11879481/can-i-add-date-time-for-sublime-snippet>
4. { "word_wrap" : true } 自动折行

## package
1. markdown-preview
2. git


## shortcuts Keyboard Shortcuts - Windows/Linux

- Editing

	Windows
	Ctrl + Alt + Up	Column selection up
	Ctrl + Alt + Down	Column selection down
	Linux
	Alt + Shift + Up	Column selection up
	Alt + Shift + Down	Column selection down

- Navigation/Goto Anywhere

	Ctrl + P	Quick-open files by name
	Ctrl + R	Goto symbol
	Ctrl + ;	Goto word in current file
	Ctrl + G	Goto line in current file

- General

	Ctrl + Shift + P	Command prompt
	Ctrl + KB	Toggle side bar
	Ctrl + Shift + Alt + P	Show scope in status bar

- Find/Replace

	Ctrl + F	Find
	Ctrl + H	Replace
	Ctrl + Shift + F	Find in files

- Tabs

	Ctrl + Shift + t	Open last closed tab
	Ctrl + PgUp	Cycle up through tabs
	Ctrl + PgDn	Cycle down through tabs
	Ctrl + Shift	Find in files
	Ctrl + W	Close current tab
	Alt + [NUM]	Switch to tab number [NUM] where [NUM] <= number of tabs

- Split window

	Alt + Shift + 2	Split view into two columns
	Alt + Shift + 1	Revert view to single column
	Alt + Shift + 5	Set view to grid (4 groups)
	Ctrl + [NUM]	Jump to group where num is 1-4
	Ctrl + Shift + [NUM]	Move file to specified group where num is 1-4

- Bookmarks

	Ctrl + F2	Toggle bookmark
	F2	Next bookmark
	Shift + F2	Previous bookmark
	Ctrl + Shift + F2	Clear bookmarks

- Text manipulation

	Ctrl + KU	Transform to Uppercase
	Ctrl + KL	Transform to Lowercase

选择类

Ctrl+D 选中光标所占的文本，继续操作则会选中下一个相同的文本。

Alt+F3 选中文本按下快捷键，即可一次性选择全部的相同文本进行同时编辑。举个栗子：快速选中并更改所有相同的变量名、函数名等。

Ctrl+L 选中整行，继续操作则继续选择下一行，效果和Shift+↓ 效果一样。

Ctrl+Shift+L 先选中多行，再按下快捷键，会在每行行尾插入光标，即可同时编辑这些行。

Ctrl+Shift+M 选择括号内的内容（继续选择父括号）。举个栗子：快速选中删除函数中的代码，重写函数体代码或重写括号内里的内容。

Ctrl+M 光标移动至括号内结束或开始的位置。

Ctrl+Enter 在下一行插入新行。举个栗子：即使光标不在行尾，也能快速向下插入一行。

Ctrl+Shift+Enter 在上一行插入新行。举个栗子：即使光标不在行首，也能快速向上插入一行。

Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。

Ctrl+Shift+] 选中代码，按下快捷键，展开代码。

Ctrl+K+0 展开所有折叠代码。

Ctrl+← 向左单位性地移动光标，快速移动光标。

Ctrl+→ 向右单位性地移动光标，快速移动光标。

shift+↑ 向上选中多行。

shift+↓ 向下选中多行。

Shift+← 向左选中文本。

Shift+→ 向右选中文本。

Ctrl+Shift+← 向左单位性地选中文本。

Ctrl+Shift+→ 向右单位性地选中文本。

Ctrl+Shift+↑ 将光标所在行和上一行代码互换（将光标所在行插入到上一行之前）。

Ctrl+Shift+↓ 将光标所在行和下一行代码互换（将光标所在行插入到下一行之后）。

Ctrl+Alt+↑ 向上添加多行光标，可同时编辑多行。

Ctrl+Alt+↓ 向下添加多行光标，可同时编辑多行。

 

编辑类

Ctrl+J 合并选中的多行代码为一行。举个栗子：将多行格式的CSS属性合并为一行。

Ctrl+Shift+D 复制光标所在整行，插入到下一行。

Tab 向右缩进。

Shift+Tab 向左缩进。

Ctrl+K+K 从光标处开始删除代码至行尾。

Ctrl+Shift+K 删除整行。

Ctrl+/ 注释单行。

Ctrl+Shift+/ 注释多行。

Ctrl+K+U 转换大写。

Ctrl+K+L 转换小写。

Ctrl+Z 撤销。

Ctrl+Y 恢复撤销。

Ctrl+U 软撤销，感觉和Gtrl+Z一样。

Ctrl+F2 设置书签

Ctrl+T 左右字母互换。

F6 单词检测拼写

 

搜索类

Ctrl+F 打开底部搜索框，查找关键字。

Ctrl+shift+F 在文件夹内查找，与普通编辑器不同的地方是sublime允许添加多个文件夹进行查找，略高端，未研究。

Ctrl+P 打开搜索框。举个栗子：1、输入当前项目中的文件名，快速搜索文件，2、输入@和关键字，查找文件中函数名，3、输入：和数字，跳转到文件中该行代码，4、输入#和关键字，查找变量名。

Ctrl+G 打开搜索框，自动带：，输入数字跳转到该行代码。举个栗子：在页面代码比较长的文件中快速定位。

Ctrl+R 打开搜索框，自动带@，输入关键字，查找文件中的函数名。举个栗子：在函数较多的页面快速查找某个函数。

Ctrl+：打开搜索框，自动带#，输入关键字，查找文件中的变量名、属性名等。

Ctrl+Shift+P 打开命令框。场景栗子：打开命名框，输入关键字，调用sublime text或插件的功能，例如使用package安装插件。

Esc 退出光标多行选择，退出搜索框，命令框等。

 

显示类

Ctrl+Tab 按文件浏览过的顺序，切换当前窗口的标签页。

Ctrl+PageDown 向左切换当前窗口的标签页。

Ctrl+PageUp 向右切换当前窗口的标签页。

Alt+Shift+1窗口分屏，恢复默认1屏（非小键盘的数字）

Alt+Shift+2 左右分屏-2列

Alt+Shift+3 左右分屏-3列

Alt+Shift+4 左右分屏-4列

Alt+Shift+5 等分4屏

Alt+Shift+8 垂直分屏-2屏

Alt+Shift+9 垂直分屏-3屏

Ctrl+K+B 开启/关闭侧边栏。

F11 全屏模式

Shift+F11 免打扰模式

其实sulime text菜单栏各个选项中都会提示相关的快捷键，各位可以自己去看看，本文主要是整理一些隐藏或不被发掘的快捷键，个人整理难免会有实用的快捷键遗漏，如果你还发现有实用的sublime text的快捷键和使用栗子，欢迎补充~最后说一句，死记硬背是记不住的，请结合自己的需求，有选择的使用、练习、熟悉相关快捷键，一两个星期后定能提高效率！

---
Sublime Text 3 Scopes

<https://gist.github.com/danpe/6993237>

A list of Sublime Text 3 scopes to be used for Snippets Makers / Plugin Developers.
 
Main Symbol Scopes: entity.name.function, entity.name.type, meta.toc-list
 
	ActionScript: source.actionscript.2
	AppleScript: source.applescript
	ASP: source.asp
	Batch FIle: source.dosbatch
	BibTex: source.bibtex
	C#: source.cs
	C++: source.c++
	Clojure: source.clojure
	CoffeeScript: source.coffee
	CSS: source.css
	D: source.d
	Diff: source.diff
	Erlang: source.erlang
	Go: source.go
	GraphViz: source.dot
	Groovy: source.groovy
	Haskell: source.haskell
	HTML(TCL): text.html.tcl
	HTML: text.html(.basic)
	Java Doc: text.html.javadoc
	Java Properties: source.java-props
	Java: source.java
	Javascript: source.js
	JSON: source.json
	JSP: text.html.jsp
	LaTex Log: text.log.latex
	LaTex Memoir: text.tex.latex.memoir
	LaTex: text.tex.latex
	LESS: source.css.less
	Lisp: source.lisp
	Lua: source.lua
	MakeFile: source.makefile
	Markdown: text.html.markdown
	Matlab: source.matlab
	Multi Markdown: text.html.markdown.multimarkdown
	Objective-C++: source.objc++
	Objective-C: source.objc
	OCaml campl4: source.camlp4.ocaml
	OCaml: source.ocaml
	OCamllex: source.ocamllex
	Pascal: source.pascal
	Perl: source.perl
	PHP: source.php
	Plain text: text.plain
	Python: source.python
	R Console: source.r-console
	R: source.r
	Regular Expression(python): source.regexp.python
	Regular Expression: source.regexp
	RestructuredText: text.restructuredtext
	Ruby HAML: text.haml
	Ruby on Rails: source.ruby.rails
	Ruby: source.ruby
	SASS: source.sass<!--  -->
	Scala: source.scala
	Shell Script: source.shell
	SQL(Ruby): source.sql.ruby
	SQL: source.sql
	Stylus: source.stylus
	TCL: source.tcl
	TeX: text.tex
	Textile: text.html.textile
	XML: text.xml
	XSL: text.xml.xsl
	YAML: source.yaml

---
Sublime Text 3 Environment Variables

list of all Sublime Text 3 Environment Variables to be used by Snippet Makers / Plugin Developers
 
	$SELECTION  The text that was selected when the snippet was triggered.
	$TM_CURRENT_LINE  Content of the line the cursor was in when the snippet was triggered.
	$TM_CURRENT_WORD	Current word under the cursor when the snippet was triggered.
	$TM_FILENAME	File name of the file being edited including extension.
	$TM_FILEPATH	File path to the file being edited.
	$TM_FULLNAME	User’s user name.
	$TM_LINE_INDEX	Column the snippet is being inserted at, 0 based.
	$TM_LINE_NUMBER	Row the snippet is being inserted at, 1 based.
	$TM_SELECTED_TEXT	An alias for $SELECTION.
	$TM_SOFT_TABS	YES if translate_tabs_to_spaces is true, otherwise NO.
	$TM_TAB_SIZE	Spaces per-tab (controlled by the tab_size option).
