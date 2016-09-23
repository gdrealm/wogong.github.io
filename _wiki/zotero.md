---
title: zotero
date: 2014-07-21
modified: 2015-09-05
---

Zotero是一款很好用的开源文献管理软件，集成了Word和Libreoffice的插件，可以方便的进行文献管理和文献引用。一般安装Zotero Standalone版本时，软件会自动根据系统语言选择界面语言（Zotero for Firefox的界面语言由Firefox的语言而确定），如果想换成英文的节目语言，需要进行如下操作。

    1、在工具->选项中，选择高级选项卡 将Zotero界面语言调成英文

     2、在杂项中，选择“打开配置编辑器”，在弹出来的对话框中点击“I will be careful, I promise!”

     3、在Search框中输入intl.locale.matchOS，将true双击变成false，这意味这Zotero将使用English而不再是系统语言。


## note

已下载符合中国论文标准的引文样式

暂时不支持 S 标准

1. change lang
In Zotero Standalone, the interface language defaults to matching the operating system's language. To override this and use English instead of the operating system's language, open Preferences→Advanced→Open about:config), and set intl.locale.matchOS to false. Then restart Zotero.


## add-on
1. Markdown here
    Ctrl+Alt+M
2. zotero-scholar-citation  https://github.com/beloglazov/zotero-scholar-citations
3. Word

##导入第一篇文献

好了，准备工作做完了。现在，让我们导入第一篇文献。Zotero支持以下六种导入方法：

* 互联网自动识别：Web Translators (URL bar icon) 
* 手动输入：Manual Input or Edit From a bibliographic 
* 文件导入：format (RIS, BibTeX, MARC, etc.) 
* 通过标示符增加：Add by identiﬁer (DOI, ISBN, PMID) 
* 通过PDF元数据识别：Add PDF then Retrieve Metadata 
* 从网页识别：Get any Webpage with basic data


##Zotero更多资源

Zotero还有更多进阶玩法，在这里不展开讲了。各位感兴趣的敬请查阅资料：

###入门教程

* zotero中文快速入门：http://www.zotero.org/support/zh/quick_start_guide
* Zotero中文入门介绍：http://www.zotero.org/support/_media/zotero_miniguide.pdf
* 台湾中央研究院计算中心关于Zotero的介绍：http://ascc.sinica.edu.tw/iascc/articals.php?_section=2.4&_op=?articalID:3934
* MIT图书馆的教程：http://libguides.mit.edu/zotero
* Washington University St. Louis: http://libguides.wustl.edu/zotero
* Zotero入门介绍：http://www.slideshare.net/adam3smith/intro-zotero
*[你为什么需要Zotero](http://www.slideshare.net/tjowens/zotero-workshop-slides)：其中关于六类人的漫画描述，极其生动。
* [研究生2.0关于Zotero的介绍](http://pulipuli.blogspot.jp/search/label/Zotero)
* [老杨与他本科同学写的Zotero介绍](http://blog.yesmryang.net/tags/Zotero/)

###核心插件

* [Zotero插件大全](http://www.zotero.org/support/plugins)
* [Papermachine](http://web.library.emory.edu/blog/supercharge-your-zotero-library-using-paper-machines-part-i)
* [Zotfile](http://www.columbia.edu/~jpl2136/zotfile.html)
* [Multi-Lingual Zotero](http://www.citationstylist.org)
* [Qnotero](http://www.cogsci.nl/software/qnotero)
* [Translator testing](http://zotero-translator-tests.s3-website-us-east-1.amazonaws.com/)
* Zotero隐藏的偏好：http://www.zotero.org/support/preferences/hidden_preferences
* [RTF Scan](http://www.zotero.org/support/rtf_scan)

###版式风格在线可视编辑

* [csl-editor](https://github.com/citation-style-editor/csl-editor)

###整合工具

* [Omeka](https://github.com/omeka/Omeka)  : Zotero开发学校的另一个项目
* [editorsnotes](https://github.com/editorsnotes/editorsnotes)
* Zotero开发机构的其他项目：http://chnm.gmu.edu/research-and-tools/

###移动支持

* [ZotPad](https://github.com/mronkko/ZotPad)：iPad版的Zotero
* [zandy](https://github.com/ajlyon/zandy)：安卓版的Zotero
* [bibup](http://elearning.unifr.ch/bibup/tuto/index.php)：iphone版本的Zotero，更多参见：

<http://www.zotero.org/blog/zotero-apps-go-mobile/>

##小结

与其说[Zotero]是一个文献管理软件，不如说是一个知识管理平台。选择开源软件，就是选择一个生态链，这是与商业软件，如[Papers2]、[mendeley]或[Endnote]非常不一样的地方。
