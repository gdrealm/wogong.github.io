---
layout: post
title: "使用Google Drive和Google Apps Script保持你的Twitter存档更新"
description: ""
tags: [Twitter, Google Apps Script, Google Drive]
---

翻译自: [Keep your Twitter Archive fresh on Google Drive using a bit of Google Apps Script](http://mashe.hawksey.info/2013/01/sync-twitter-archive-with-google-drive/)

同越来越多的其他人一样，我也向Twitter请求了自己推文的完整存档。Twitter在你请求数据后做了很棒的工作：打包所有推文，甚至用`HTML`和`JavaScript`创建了一个搜索界面，但是这些推文存档是保持不变的。另一个问题是你需要有虚拟主机去分享你的推文存档给其他人访问。

幸运的是，Google最近发布了在Google Drive上发布站点的功能，将你的存档上传到一个文件夹中，然后共享文件夹，使其“发布在网络上”，你可以让其他人来浏览您的存档（[这里是我的](https://googledrive.com/host/0B6GkLMU9sHmLRFk3VGh5Tjc5RzQ/)）。注意：Mark Sample (@samplereality) 发现，如果你在上传时打开文件转换选项，将会破坏你的存档。【如果你不想使用一个谷歌帐户，你也可以使用Dropbox里的[Public Folder](https://dl.dropbox.com/u/7860124/tweets/index.html)】

>文档没有清晰表明如何做到这一点。基本上，只要根文件夹有`index.html`文件且到子文件夹是相对链接，你只需在Google Drive中打开文件夹，将`URL`的第一部分替换为 `https://googledrive.com/host/`
>
>例如：
>
>https://drive.google.com/#folders/0B6GkLMU9sHmLRFk3VGh5Tjc5RzQ 替换为 https://googledrive.com/host/0B6GkLMU9sHmLRFk3VGh5Tjc5RzQ/


接下来我们需要保持数据的更新。我们来仔细看看Twitter如何打包存档，可以看到每个月份的推文文件都存储在[/data/js/tweets](https://docs.google.com/folder/d/0B6GkLMU9sHmLYmJHWnc4aHJCdmM/edit?forcehl=1&hl=en_GB), 一些关于存档的元数据文件存储在[/data/js/](https://docs.google.com/folder/d/0B6GkLMU9sHmLSlhJNHgwdFNtMFU/edit), 最重要的文件是[tweet_index.js](https://docs.google.com/folder/d/0B6GkLMU9sHmLSlhJNHgwdFNtMFU/edit?docId=0B6GkLMU9sHmLNFRFMkx0TEdlQ2M).

幸运的是，Google Apps Script提供了一种简单的方法处理Google Drive和其他Google Apps或第三方服务的接口，而且基于`JavaScript`的语法使得处理现有的数据文件很容易。因此，我们可以读取现有的数据，获取新的状态更新并写入新的数据文件，保证推文存档的更新。

要做到这一切，我折腾出了这个谷歌电子表格模板：

*** [使用Goolge Drive更新Twitter存档](https://docs.google.com/spreadsheet/ccc?key=0AqGkLMU9sHmLdHRtbUF4OGh6ZnBZeFVsSjNhZlc1Z2c#gid=1) ***
[一旦打开文件 > 制作自己的副本文件]

希望下面的视频介绍了如何设置和使用：

<p align="center"><iframe src="http://www.youtube.com/embed/ce8G3sEOjAY?rel=0" height="377" width="670" allowfullscreen="allowfullscreen" frameborder="0"></iframe></p>


这个解决方案一个很好的特点是，即使你不公开分享你的存档，只要您使用Google Drive的程序同步电脑文件，你本地机器上的存档数据保持更新。

该解决方案使用的模型也挺有意思的。使用Google Apps Script创建接口和应用的[方法](https://developers.google.com/apps-script/html_service)很多。在这个案例中，你不需要依靠笨重的写入处理和动态内容（当然会有一些代码清洗），采用更新Google Drive上的数据和静态文件界面是非常理想的方式。

你也可以选择使用一些额外的代码将更新的文件推送到到另一台Web服务器，或者将本地的Google Drive和虚拟主机之间同步，但现在我很高兴Google存储我的数据。

- update0225：前几天一直没有空折腾，今天搞好自己的了，我的tweets: https://googledrive.com/host/0BwpUrJ713Y8MNi1fUGQtSU4wdWc/
            你也可以打开这个链接: http:twitter.wogong.net

- update20140329：几个月前 Google Script 出现错误，作者的修复更新见这里：https://gist.github.com/mhawksey/7770536
