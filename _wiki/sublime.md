---
layout: wiki
title: sublime
create: 2014-08-26
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