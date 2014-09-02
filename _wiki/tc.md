---
layout: wiki
title: tc
---

TC or TotalCommander

## note
1. 安装时可以选择配置文件位置，但是工具栏需要自己
定义，工具栏文件default.bar同样放在Dropbox文件夹
中，方便恢复。
2. 安装时可以自定义配置文件的位置，但是安装完毕之
后则没有这个配置选项。官方网站给出了这样一个小程
序，inireloc，可以满足使用要求
3. viaTC 利用 [[AHK|ahk]] 编写的 TC 下 VIM 风格快捷键插件。
4. TC复制目录结构：为复制限定特殊条件
　首先选择需要复制的目录(当然是最顶级的目录)，然后按下
  F5键，在“只选择下列类型的文件”框中输入如下内容：\*.abdcefgh
  其实输入其它的扩展名也可以，只要尽量古怪、尽量生僻一些就行了。
5. 修改TC的wincmd.ini参数很方便，软件名称为Ultra TC Configuration Editor
6. 输出文件名
   复制文件名；
   
       Dir *.* /s /ad >list.txt
       Tree *.* /s >tree.txt


## 快捷键
* C-m 批量重命名
* ALT+SHIFT+ENTER 　在详细列表状态下显示当前所有目录的大小 
* Ctrl + B 把当前文件夹下所有子目录中的文件放在一起显示 
* CTRL + P 把当前路径拷贝到命令行 
* → 将焦点定位到命令行以便输入命令。
* Ctrl + ↑ 将当前选中的压缩文件或文件夹在一个新的窗口中打开。 
* C+F12 筛选。

## 配置文件
### [Configuration]
* DirBrackets=0 文件夹前后不加中括号。
* SortUpper=2 数字文件名排序，自然数顺序。
* SpaceMovesDown=1 空格键选择后光标下移。
* RenameSelOnlyName=1 重命名不选择扩展名。
* OleComments=0 只显示注释。
* LongInStatus=1 在状态栏显示文件名。
*  
* 

### [Shortcuts]
* F2=cm_RenameOnly <F2> 重命名
* C+E=em_Everything Ctrl+e Everything 搜索。
* CA+F5=cm_PackFiles 压缩文件在本窗格的同一文件夹下。


### [Packer]
* ExpertMode=0  
1：压缩包内的文件回车/双击后直接运行/打开，
0：显示该文件属性窗口，点击“unpack and execute”按钮
后才运行。  运行都是解压到tc的临时目录下，一般是
%TEMP%/\_tc目录下，(`c:\Users\zhen\AppData\Local\Temp\_tc\`)
一般可以自动删除，但如压缩包仍处于打开状态（tc仍在
查看该包内容），则会提示是否不清除临时文件而强行退出。

## 插件
1. QuickSearch eXtended  
`ctrl-s`  
TC拼音首字母搜索功能，或者说，TC本身的快速搜索功能，
早就一统江湖，只是这里没有更新。新王者就是——QuickSearch eXtended 。
它相当于 Shanny 的拼音首字母搜索，加 Google 的
空格/模糊搜索。【xbeta】

2. uLister  
TC的万能文件查看插件  http://xbeta.info/tc-docx.htm
