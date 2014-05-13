---
layout: wiki
title: defy
---

机锋升级神贴：http://bbs.gfan.com/android-2736285-1-1.html
升级，wipe；
root；
recovery；
关闭调试模式
gms服务包；
1、下载谷歌服务包（地址请自行搜索，你们懂的～），下载完成后修改文件名为update.zip。
2、打开压缩包定位到文件：update.zip\META-INF\com\google\android\updater-script，右键“编辑”，
将updater-script第2行代码：assert(getprop("ro.product.model") == "ME525" && getprop("ro.build.version.sdk") == "8"); 改为：assert(1==1); 然后保存，更新压缩包。
3、将update.zip放到SD卡根目录下。
4、ROOT你的系统（如果已经ROOT请跳过此步）。
5、安装自定义恢复系统（R大师那个就可以）。安装好后打开，点击第一项"安装恢复系统"，出现授权请求时点确认，会弹窗提示你安装成功。
6、在“设置” - “应用程序” - “开发” 中关闭“USB调试”选项（切记！否则恢复模式重启后会黑屏，要是不幸黑屏了，也不要慌，直接拔电池，然后装上重新启动进系统后关闭“USB调试”即可）。
7、在恢复系统中点第二项“恢复模式重启”，系统重启进入自定义恢复系统界面。
8、看到带有“update.zip"字样的选项了吧？使用音量键选择它并按电源键确认，接下来就是安装啦～ 安装完会有提示，此时选择重启即可，启动过程有些慢请耐心等待。
同步

