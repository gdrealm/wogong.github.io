---
layout: wiki
title: marc
update: 2014-10-21
---

# Marc

## 安装
1. Windows 下的安装。Marc 2012 windows 7 64bit 安装记录。

1. 生成License.dat 
下载文件， [[http://pan.baidu.com/share/link?shareid=169479&uk=3087520777|点我]]

以下为license.dat中的说明文档，
- Step 1.  Open license.dat with Notepad.exe, replace localhost with your own hostname, replace 000000000000 with your Ethernet Address, and then save it. DO NOT CHANGE ANY OTHER THINGS!

- Step 2.  Drag license.dat onto Keygen.exe to Generate license.dat.“Drag” means that “将文件拖动到keygen中，然后license.dat被patch成为license for your computer”。如图：

![drag](http://wogong-image.b0.upaiyun.com/wiki/marc_lic_drag.jpg)

- Step 3.  That's all.

 
2.安装 msc_licensing_11.9_windows3264

下载文件，[[http://pan.baidu.com/share/link?shareid=169487&uk=3087520777|点我]]

安装完毕后配置，建议将上一步骤生成的license.dat放在此程序的安装目录，一切按照默认路径即可。以下是配置LMTOOLS

![server](http://wogong-image.b0.upaiyun.com/wiki/marc_lic_server.png)
最后save，开启服务。


3.添加系统变量LM_LICENSE_FILE：

首先，右击计算机→属性→高级系统设置→环境变量→用户变量中新建一个，变量名为LM_LICENSE_FILE，变量值为27500@hostname，hostname可以任意取。


4.安装主程序

选择步骤一生成的license.dat。

安装完成后打开，弹出窗口，一般出现错误会报错，基本按照提示信息就可以解决问题了。

= 日常使用 =
* 改变默认的directory:改变启动程序的快捷方式属性，start设置为需要设置的默认路径。貌似需要在快捷方式处右键。
* 快捷键：Alt-动态视图，可以鼠标拖拽，此时右键可以缩放
* ·
* 

= 教程 =
[[marc_tutorial|MSC.Marc / Mentat 2003 基础与应用实例]]

2. Linux 下还没安装过。

## 使用

