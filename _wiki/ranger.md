---
layout: wiki
title: ranger
---

vim风格的cli文件管理器。

更改默认编辑器及shell等等：依靠系统环境变量

ubuntu 12.04 下通过{{{apt-get install ranger}}}会提示以下错误。
%ranger
ranger version: 1.5.2, executed with python 2.7.3
Locale: en_US.UTF-8
Current file: None
Traceback (most recent call last):
  File "/usr/lib/python2.7/dist-packages/ranger/core/main.py", line 79, in main
    load_settings(fm, arg.clean)
  File "/usr/lib/python2.7/dist-packages/ranger/core/helper.py", line 105, in load_settings
    fm.apps = apps.CustomApplications()
AttributeError: 'module' object has no attribute 'CustomApplications'

ranger crashed.  Please report this traceback at:
http://savannah.nongnu.org/bugs/?group=ranger&func=additem


手动下载新版本1.6.0的deb文件安装OK。

sudo dpkg -i ranger_1.6.0-1_all.deb
