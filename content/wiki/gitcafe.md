title: gitcafe
date: 2014-08-27
modified: 2015-08-03 23:50:58


如何创建Page
创建一个与用户名(如果是组织，就是组织名)相同名称的项目

在本地创建一个Git目录
添加一个试验性的html文档
提交第一个版本
添加项目remote
创建一个gitcafe-pages的分支，并切换到该分支
提交该分支至GitCafe


在完成上述操作后，您即可访问 XXX.gitcafe.com (XXX指代您的用户名或是组织名) 来查看页面效果了！

如何绑定自定义域名绑定
进入你的Page Repo的项目管理界面： 
你将会看到左侧的导航栏中有自定义域名设置，点击进入，输入你想要设置的域名： 需要注意的是，请正确填写你期望自定义的域名，填写时请不要填写http://这样的协议，当然如果你填写了，我们会智能的擦除这些字符。
最后在你的域名管理界面添加一个A记录，将它指向GitCafe服务器的IP： 
大功告成，现在你就可以通过自己的域名来访问GitCafe为你渲染好的Pages了！

如何创建项目的Pages服务
在你的项目里面，创建一个名为gitcafe-pages的orphan分支。

➜ git:(master) git checkout –orphan gitcafe-pages

就像个人的Pages页面那样，把你的项目页面的静态资源文件放到这个branch里，再push到GitCafe。

➜ git:(gitcafe-pages) git push -u origin gitcafe-pages

随即就可以试着访问 用户名.gitcafe.com/项目名

如何创建非jekyll的Pages
只要在page的项目下加入.nojekyll文件，便会自动认为此page不是jekyll项目

支持环境
jekyll 2.0.3
maruku 0.6.1
kramdown 1.0.2
liquid 2.5.1
