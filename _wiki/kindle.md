---
layout: wiki
title: kindle
update: 2014-07-16
---

1. kindle dxg 适合的PDF：优化->印刷版本。
2. Kindle 的官方充电器输出电流为 0.85A。
3. 切换中亚美亚账户时，生词本会清空

* 产品
1. Kindle DXG 
2. Kindle Keyboard 3
3. Kindle 4
4. Kindle 5 （Kindle 4 的升级产品）
5. Kindle Paperwhite （当前首选）简称KPW，是内置光源的新一代触摸屏版本Kindle
6. Kindle Paperwhite 2（当前首选）简称 KPW2, KPW 的升级版本

## 多看？
推荐同学购买Kindle时，略微做点工作的人便会询问关于
是否需要刷多看的问题。我来说下自己的看法。主要是对
比Kindle的原生系统与多看系统。首先声明，我基本一直
使用原生系统，多看系统还是很久以前体验的，所以相关
对比可能已经不太准确了。我的结论是不推荐多看系统。

为什么不推荐多看？

1. 多看系统无浏览器，在某些需要认证的无线网环境下无
法联网同步推送。例如Tsinghua、CMCC、Chinanet等等，
这个问题应该在很长时间都得不到解决；目前的多看已经带浏览
器了，不过初步的感觉是很差。update20140428

2. 多看系统无法在Amazon上购买电子书，只有内置的多看市场；

3. 虽然多看的目标是打造一整套的电子阅读体系，但是抱
歉，我目前还是更相信Amazon一些；

4. 多看的耗电问题，不知道目前有没有得到解决；

5. 多看的卖点之一是中文界面，但是原生系统目前也支持
中文了，还有拼音输入，我为什么还要因为这个刷多看？
再说，界面中英文对我来说确实没什么大用处；
6. 多看的最大（？）卖点是PDF的阅读优化，例如智能切边
之类，但是抱歉，我不觉得在6寸屏幕上阅读PDF的体验好到
哪里去，就个人而言，从来不在KPW上阅读PDF。update0420：
非扫描电子书的重排很神奇。

刷机：目前Kindle可以选择的操作系统有Duokan、Bambook
等等，刷机步骤不是很有难度，参见多看官方论坛指导。


## 书籍管理
无他，开源软件[Calibre](http://calibre-ebook.com/)
当之无愧之首选。目前采用两个书库PDF单独拿出来了。


管理Archieved items

今天发现Amazon可以同步Personal Documents了，这点真的非常赞。无论是在我的Kindle，还是在Android设备上，我可以看自己传上去的书，还可以分享自己的Highlights，但是Amazon对于Personal Documents的管理十分的不方便，尤其是只能一个一个删除，而且每删除一两项就会自动刷新（虽然可以手动Esc强制取消），搜索找到以下的一个Bookmarklet，现在记录如下：

参考链接： [http://www.mobileread.com/forums/showthread.php?t=162972 mobileread论坛] [http://www.richardzhong.com/2012/03/%E5%A6%82%E4%BD%95_%E6%89%B9%E9%87%8F%E5%88%A0%E9%99%A4_personal_documents_amazon_kindle_%E4%BD%BF%E7%94%A8_%E6%8A%80%E5%B7%A7/#comment-28 个人博客]

书签放在Chrome的书签栏中，URL：

    javascript:(function(){ var v = new RegExp("amazon"); if (!v.test(document.URL)) { return false; } {a=document.getElementsByClassName('rowBodyCollapsed');for(var i = 0; i<a.length; i++){Fion.deleteItem('deleteItem_'+a[i].getAttribute('asin'));};return; }})();

使用calibre的插件管理collection http://www.mobileread.com/forums/showthread.php?t=118635 帮助文档链接

## 系统相关


kindle原生系统下

0. 升级（推荐5.3.5版固件，目前5.3.6越狱未测试，多看也不能装）
官网固件升级：http://www.amazon.cn/gp/help/customer/display.html/ref=hp_softwareupdates_pw?nodeId=200899290 
下载完后，断开USB连接，通过“菜单> 设置> 菜单> 更新你的Kindle”升级安装

1. 越狱

http://www.mobileread.com/forums/showthread.php?t=198446
下载并解压kpw_jb.zip越狱包。把kpw连接到计算机，
a.把越狱包里面的“jailbreak.sh”和“MOBI8_DEBUG”文件直接复制到根目录；
b.把“jailbreak.mobi”的文件 复制到documents文件夹里；
c.安全弹出你的kpw驱动器，断开USB连接；
d.然后看你的KPW机器，你会看到一个新的文件名为“Paperwhite Jailbreak”文档。打开此文档。
e.按照文档中的说明操作 几个简单步骤 就完成了！！！


2.安装KPVBooklet

KPVBooklet支持5.1.2至5.3.5的Kindle固件（建议越狱后升级到5.3以上固件再安装），下载地址：https://code.google.com/p/kpvbooklet-package/downloads 。将下载的zip文件解压缩，把update_kpvbooklet_x.x.x_install.bin文件拷贝到Kindle的磁盘根目录下，断开USB连接。通过“菜单> 设置> 菜单> 更新你的Kindle”安装，注意不要通过重启来安装。 

PS：Update Your Kindle显示为灰色可能是因为安装了特定版本的多看，可在Kindle磁盘根目录下创建一个名为DUOKAN_DISABLE的文件（即：随便建一个文件再去除后缀），然后重启机器再安装。

3.安装Koreader

下载最新的Koreader安装包，下载地址：https://code.google.com/p/koreader-package/downloads 。将下载的zip文件解压缩到Kindle磁盘根目录即可。
其中：Koreader可以通过KPVBooklet与原生系统集成，在原生系统主界面即可显示EPUB、DjVu等文档。默认使用Koreader打开PDF、EPUB、DjVu、FB2、CHM和DOC文档，使用原生系统自带阅读器打开MOBI、AZW和TXT文档。也可以长按PDF文档在弹出窗口中选择GOTO来使用原生阅读器打开PDF文档。（也就是说：不影响原系统字典的使用，楼主我因为扫描pdf不方便在原系统观看才越狱的） 。
至于PDF重排请参考：http://vislab.bjmu.edu.cn/blog/hwangxin/2012/10/read-scanned-pdfs-with-kindlepdfviewer/#Kindle   
启动 `Shift+P+D`

4. 加字体（不需越狱，以window系统为例）

（1）.window上设置让文件显示出扩展名（已经显示了的可以跳过这步骤），首先要在电脑上打开一个文件夹-选择“工具”选项-再选择“文件夹选项”-选择“查看”-把“隐藏已知文件的扩展名”选项的勾去掉。
（2）.KPW通过数据线连接电脑，打开KPW的磁盘在个目录创建一个txt文件，重命名txt文件为
USE_ALT_FONTS ，重命名的时候要确保文件无扩展名（这就是第一步的目的）。


（3）.在KPW的磁盘根目录创建一个文件夹命名fonts ，把要添加的几种字体放在这个fonts文件夹内。
（4）.安全退出kindle的连接，拔下数据线，重启KPW(菜单键-设置-菜单键-重启)
（5）.在kindle上打开一本书，按Aa就可以看到添加的字体了。
（字体可以去网上搜，和电脑字体通用，个人觉得方圆字体、兰亭黑体很不错）

5、书籍存放路径

根目录/documents---------可以在里面建立文件夹给书本分类


多看系统下

1、书籍存放路径
根目录/DK_Documents---------可以在里面建立文件夹给书本分类
根目录/documents---------可以在里面建立文件夹给书本分类

顺便分享一本竖排精装版的《菜根谭》http://pan.baidu.com/share/link?shareid=1267314033&uk=3894070902 

2、屏保

替换路径:\DK_System\xKindle\res\ScreenSaver

方法：把.jpg文件放到以上目录下即可，里面自带的屏保可删除。

分享：水墨画屏保+多看自带的人物屏保  http://pan.baidu.com/share/link?shareid=1285616650&uk=3894070902 

3、字体

替换路径:\DK_System\xKindle\res\userfonts

方法：.ttf文件放入以上目录下即可，自带的字体不建议删除，因为有的书是用几种字体排版的，删除后影响阅读体验。

分享：方正静蕾简体+浪漫雅圆简体+迷你简雪君简体  http://pan.baidu.com/share/link?shareid=1303124577&uk=3894070902 

4、字典词典

替换路径:\DK_System\xKindle\res\dict

方法：将..dict、.idx、.ifo三个文件放入以上目录下即可，多看自带的牛津词典建议删除，因为排版很乱，方法是删除以上目录下的四个以oxford开头的文件即可。

分享：朗道英汉词典+新华字典  http://pan.baidu.com/share/link?shareid=1353575379&uk=3894070902 



### 正版
1. Amazon 官方商城  
   中国 amazon.cn 中文资源丰富，很多免费电子书，推荐。
   美国 amazon.com 需要注册 amazon.com 账号，与中国区账号独立
   获取英文书籍推荐这里（不过价格很喜人）。
2. 多看商城  
   只适用于安装了多看系统的 Kindle，由于其版权保护严格（DRM，只能在
   购买的账号注册的设备上阅读）。中文排版优于 amazon.cn。
3. 豆瓣  
   现在无法在 Kindle 上直接阅读，不推荐。
3. 唐茶  
   中文书籍，默认无DRM，排版精美，价格高昂，资源较少，不推荐。

### 盗版
1. 各种网盘  
   百度，360，微盘，尤其推荐 新浪爱问。
2. 专业论坛  
   如 Hi-PDA 的 [E-ink 版](http://www.hi-pda.com/forum/forumdisplay.php?fid=59)
3. 网络搜索  
   大海捞针，有经验的可以最后选择此途径。

## 我的找书方法
1. [Google 自定义搜索](http://wogong.net/kindle)  
   涵盖了百度网盘，新浪爱问，以及各大电子书商城。
   通过此搜索引擎，基本可以找到大多数的畅销书、经典书。
2. Hi-PDA  
   此论坛屏蔽了搜索引擎，需要自己进入网站自行搜索，地址见上，不需注册。
3. Google  
   还是找不到的话就搜索吧。外文书籍还可以尝试海盗湾 TPB 这个网站，
   互联网最有名的种子分享地，也是盗版的天堂。不过需要翻墙。


移动铁通的网络，由于墙的影响，kindle会无法连接推送服务器，提示如此。

![kindle](http://wogong-image.b0.upaiyun.com/wiki/kindlegfw.gif)
