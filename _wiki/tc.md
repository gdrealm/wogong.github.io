---
layout: wiki
title: tc
---

TC or TotalCommander

## note
1. 安装时可以选择配置文件位置，但是工具栏需要自己定义，工具栏文件defaultbar同样放在Dropbox文件夹中，方便恢复。
2. 安装时可以自定义配置文件的位置，但是安装完毕之后则没有这个配置选项。官方网站给出了这样一个小程
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


## Temp


Total Commander（下称TC）和Everything都是我常使用的软件，一个是功能超级强大的资源管理软件，另一个是速度电光火石的文件搜索软件。将两者结合起来可以极大的提高工作效率。本文对两者的结合方法进行了介绍。这里参考了善用佳软和水木社区的讨论，以及【1】中的方法总结。
 
1. 在Everything中调用TC
在Everything的安装目录下找到Everything.ini文件，其中包含着对Everything软件的设置选项。修改下面的几个条目：
Ini代码 

    1. open_folder_path_command=$exec("c:\Program Files\totalcmd\TOTALCMD.EXE" "/O" "/T" "$parent(%1)")  
    2. open_folder_command=$exec("c:\Program Files\totalcmd\TOTALCMD.EXE" "/O" "/T" "%1")  

 这样在Everything中搜索的时候，对于目录会通过TC来打开。需要注意的地方：

    * 在修改Everything的配置文件之前，最好是退出Everything。否则可能修改不成功或者是修改后会还原。
    * 上面的两个设置中，其中第一个是指搜索到了文件，通过右键中的"Open Path"来打开目录；而第二个是指搜索到了目录，直接双击打开或者通过右键中的“Open”来打开。
    * 在Everything.ini文件中还可以看到，还有类似explore_folder_command、explore_folder_path_command这样的项我们并没有修改。这些条目中定义了右键菜单中“Explore Path”所采取的行为。没有进行修改的一个原因是可以通过此选项来调用Windows的资源管理器，从而给打开目录提供了另外一种选择。
    * 为了避免在新的TC中打开目录，可以设置TC仅仅运行一个实例。具体的操作方式是在“配置->选项->操作方式->主程序”中设置“只允许一个TC运行”。如下图所示。



    * 在上面的条目设置中，"/T"表示在一个新的标签中打开目录。如果不需要的话可以将此选项去掉。在网上的很多版本中，这个地方都写成了"/O /T"，从而导致打开新标签失败。这里要注意的就是将选项单独开来。


2. 在TC中调用Everything
在TC的主目录下找到usercmd.ini（如果没有的话，手工新建一个），在其中输入下面的设置代码：
Ini代码 

    1. [em_Everything]  
    2. cmd=C:\Program Files\Everything\Everything.exe  
    3. param="-search "%P ""  

 在上面的设置代码中，第一个是Everything的可执行文件路径，第二个是参数。这个命令的目的是在当前目录(%P)下进行搜索。如果希望是全局搜索，则可以将param中后面的"%P "去掉。这里需要注意的是，在"%P "中包含有空格，这样做的好处是在搜索的时候将会包含有子目录。如果只是希望在当前目录下搜索而不需要包含子目录，可以将此空格去掉。
接下来在设置选项中的其他设置中找到自定义快捷键的地方，进行快捷键设置。这里使用Windows资源管理器中常用的Ctrl+F作为搜索的快捷键。在自定义快捷键的地方选中Ctrl和F后，在命令后面的放大镜弹出窗口中可以找到前面设置好的em_Everything命令，并按后面的确定按钮使其生效。如下图所示。

通过这样的设置后，按下Ctrl+F，即可以通过Everything在当前目录下搜索文件了。
 
【1】http://iamplaymore.blogspot.com/2009/02/everythingtotal-commander.html

