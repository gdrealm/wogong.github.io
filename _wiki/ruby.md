---
layout: wiki
title: ruby
date: 2016-07-12
---

## note

1. RVM ruby的版本管理工具，可以在同一台电脑安装并管理多个ruby版本
2. RubyGems ruby项目的包管理工具

## Install
在安装 Ruby 之前，先要安装 RVM：

    $ curl -L https://get.rvm.io | bash -s
（如果你已经安装了 RVM，应该运行下面的命令 `rvm get stable`
确保安装的是最新版本。）

然后运行下面的命令检查安装 Ruby 的需求条件：

    $ rvm requirements
在我的系统中，要安装以下所示的库（使用 Homebrew，OS X 中的包管理系统）：

    $ brew install libtool libxslt libksba openssl
在 Linux 中，可以使用 apt-get 或 yum。

我还得安装 YAML 库：

    # For Mac with Homebrew
    $ brew install libyaml
    
    # For Debian-based Linux systems
    $ apt-get install libyaml-dev
    
    # For Fedora/CentOS/RHEL Linux systems
    $ yum install libyaml-devel


## 相关项目
1. Gollum  
基于 ruby 和 git 的 wiki 系统，名称源于指环王。 通过文件夹形式实现层级。很自然的想法，但是遇到一些很奇怪的情况，再看 webrick 的反向查询，见blog。

2. Jekyll

        jekyll server
        jekyll --server --no-auto 利于检查错误

3. Octopress

## gem
0. config

    ~/.gemrc

1. command

    gem environment
    gem install
    # uninstall all installed gems
    `gem list --local |awk '{print $1}' |xargs gem uninstall`

2. gem source 
http://ruby.taobao.org/

为什么有这个？

由于国内网络原因（你懂的），导致 rubygems.org 存放在 Amazon S3 上面的资源文件间歇性连接失败。所以你会与遇到 gem install rack 或 bundle install 的时候半天没有响应，具体可以用 gem install rails -V 来查看执行过程。

这是一个完整 rubygems.org 镜像，你可以用此代替官方版本，同步频率目前为15分钟一次以保证尽量与官方服务同步。
如何使用？

    $ gem sources --remove https://rubygems.org/
    $ gem sources -a https://ruby.taobao.org/
    $ gem sources -l
    *** CURRENT SOURCES ***
    https://ruby.taobao.org

