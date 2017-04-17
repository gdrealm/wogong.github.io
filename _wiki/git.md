---
title: git
date: 2014-06-14
modified: 2015-08-03 23:55:28
---

## note
1. 与其他服务比较  
   其实Dropbox用来做一个简单的版本控制完全木有问题啊，对于小白来说更加直观方便。当然这是针对非程序员或者并非对代码进行版本控制。所以果断将wiki的html文件夹移除Dropbox同步文件夹。双重备份完全没有意义还容易出错。尤其是在双系统情况下。
2. 提交提示输入密码：  
   config中采用了https协议，修改采用git协议即可。
3. git fetch 只会抓取数据，但是不会自动合并，这就是fetch与pull的区别。
4. git pull & git push 均不是全局的(和默认设定有关)，最好的办法是指定远程分支。

        git pull name branch
        git push name branch
3. 常用托管网站
   * [GitHub](http://github.com) 
   * [BitBucket](http://bitbucket.org) 免费私有仓库，比github好太多，就是天朝访问捉急。
   * [GitCafe](http://gitcafe.com)
4. `git blame` Using git blame to trace changes in a file. a really cute name.
5. git on windows corrupt  
   `C:\Program Files (x86)\Git\bin>rebase.exe -b 0x50000000 msys-1.0.dll`
   快捷方式 sh.exe 设置属性快捷键都很方便
6. git branch --set-upstream master origin/<branch> 设置默认提交repo及branch

## 学习书籍
1. Pro Git 本书有简体中文版本
 * 豆瓣：[Pro Git](http://book.douban.com/subject/3420144/)
 * 在线版本en： http://git-scm.com/book
 * Amazon.com： 
   [Pro Git](http://www.amazon.com/Pro-Experts-Voice-Software-Development/dp/1430218339/ref=sr_1_1?ie=UTF8&qid=1367378781&sr=8-1&keywords=pro+git)  

## 常用命令
1. Setup git

        git config --global user.name "Your Name"
        git config --global user.email example@domin.com
        mkdir dotfile
        cd dotfile
        git init
        // git --bare init # 仓库
        touch README
        git add README
        git commit -m 'first commit'
        git remote add origin git@github.com:username/dotfile.git
        git push -u origin master

2. 移除文件
 * git rm --cached "files" 仅仅取消追踪，不会删除文件（文件夹递归操作 -r）
 * git rm "files" 会在工作目录删除这些文件
 * 在github中永久移除文件及其历史记录：
   [github如何永久删除文件及其历史记录](http://help.github.com/remove-sensitive-data/) 

3. 分支管理

 * rename local branch name: 
  `git branch -m oldbranchrename newbranchname`
 * git branch -d branchname
 * rename remote branch name: delete, and recreate
 
            $ git fetch <remote-name>
            $ git checkout -b <branch-name> <remote-branch>
            $ git push <remote-name> <branch-name>
            $ git push <remote-name> <branch-name>:<remote-branch-name>
            $ git merge <remote-branch-name>
            // remove remote branch
            $ git push <remote-name> :<remote-branch-name>
 * 将本地分支推送到远程分支，相当于备份分支 。
   `git push remote-repo-name branchname`
 * 合并本地分支
    git ch mainb
    git merge tomb

4. 远程仓库管理

        git remote -v
        git remote show name -v
        git remote add name url
        git remote rm name
        git remote rename oldneme newname

5. Git的撤消操作：重置, 签出和撤消  
Git提供了多种修复你开发过程中的错误的方法. 方法的选择取决于
你的情况: 包含有错误的文件是否提交了(commited); 如果你把它
已经提交了, 那么你是否把有错误的提交已与其它人共享这也很重要.
 * 修复未提交文件中的错误(重置)  
   如果你现在的工作目录(work tree)里搞的一团乱麻, 但是你现在还没有把它们提交; 你可以通过下面的命令, 让工作目录回到上次提交时的状态(last committed state):

            $ git reset --hard HEAD
这条件命令会把你工作目录中所有未提交的内容清空(当然这不包括未置于版控制下的文件 untracked files). 从另一种角度来说,
这会让"git diff" 和"git diff --cached"命令的显示法都变为空。  
如果你只是要恢复一个文件,如"hello.rb", 你就要使用`git checkout`

            $ git checkout -- hello.rb
这条命令把hello.rb从HEAD中签出并且把它恢复成未修改时的样子。
  * 修复已提交文件中的错误  
    如果你已经做了一个提交(commit),但是你马上后悔了, 这里有两种截然不同的方法去处理这个问题:
      1. 创建一个新的提交(commit), 在新的提交里撤消老的提交所作的修改. 这种作法在你已经把代码发布的情况下十分正确。
      创建一个新的，撤消(revert)了前期修改的提交(commit)是很容易的; 只要把出错的提交(commit)的名字(reference)做为参数传给命令: git revert就可以了; 下面这条命令就演示了如何撤消最近的一个提交:`$ git revert HEAD`  
这样就创建了一个撤消了上次提交(HEAD)的新提交, 你就有机会来修改新提交(new commit)里的提交注释信息。  
你也可撤消更早期的修改, 下面这条命令就是撤消“上上次”(next-to-last)的提交:`$ git revert HEAD^`  
在这种情况下,git尝试去撤消老的提交,然后留下完整的老提交前的版本.　如果你最近的修改和要撤消的修改有重叠(overlap),那么就会被要求手工解决冲突(conflicts),　就像解决合并(merge)时出现的冲突一样。  
译者注: git revert 其实不会直接创建一个提交(commit), 把撤消后的文件内容放到索引(index)里,你需要再执行git commit命令，它们才会成为真正的提交(commit)。

      2. 你也可以去修改你的老提交(old commit). 但是如果你已经把代码发布了,那么千万别这么做; git不会处理项目的历史会改变的情况,如果一个分支的历史被改变了那以后就不能正常的合并。  
      如果你刚刚做了某个提交(commit), 但是你又想马上修改这个提交; git commit 现在支持一个叫--amend的参数，它能让你修改刚才的这个提交(HEAD commit). 这项机制能让你在代码发布前,添加一些新的文件或是修改你的提交注释(commit message).  
      如果你在老提交(older commit)里发现一个错误, 但是现在还没有发布到代码服务器上. 你可以使用 git rebase命令的交互模式, "git rebase -i"会提示你在编辑中做相关的修改. 这样其实就是让你在rebase的过程来修改提交.
6. 暂存工作目录未提交文件。`git stash` 

## 配置
1. help.autocorrect 该配置项只在 Git 1.6.1及以上版本有效，假如你在Git 1.6中错打了一条命令，会显示： 

        $ git com git: 'com' is not a git-command. 
        See 'git --help'. 
        Did you mean this?      commit 
如果你把help.autocorrect设置成1（译注：启动自动修正），那么在只有一个命令被模糊匹配到的情况下，Git 会自动运行该命令。
2. git diff采用vimdiff  
   http://stackoverflow.com/questions/3713765/viewing-all-git-diffs-with-vimdiff
   http://technotales.wordpress.com/2009/05/17/git-diff-with-vimdiff/

        git config --global diff.tool vimdiff
        git config --global difftool.prompt false
        git config --global alias.d difftool
   Typing git d yields the expected behavior, type :wq in vim cycles to the next file in the changeset.
3. 多个仓库可以一个一个推送，也可以在config文件中配置别名
一起推送：

    [remote "all"]
      url = git@github.com:luoshupeng/commonuseppa.git
      url = git@gitcafe.com:chinesedragon/commonuseppa.git
	    url = chinesedragon@gitcd.com:/commonuseppa
4. git log 显示优化  

        git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --"

## git hooks
jekyll 自动部署,注意 `#!/bin/bash -l`
https://www.digitalocean.com/community/articles/how-to-deploy-jekyll-blogs-with-git

## git on server

    sudo add user git
    su git
    cd
    mkdir .ssh
    cp /home/wogong/.ssh/id_rsa .ssh
