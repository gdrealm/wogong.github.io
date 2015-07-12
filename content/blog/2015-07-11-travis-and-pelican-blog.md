title: pelican and travis
date: 2015-07-11 20:08:33
modified: 2015-07-11 20:08:33
category: 
tags: 
slug: 
authors: wogong
summary: 


1. 注册 Travis

2. 添加 .tavis.yml

    language: python
    
    python:
        - "2.7"
    
    before_install:
    
    install:
        - sudo pip install pelican
        - sudo pip install markdown
        - sudo pip install s3cmd
    
    script:
        - mkdir output
        - make html   

3. git push 测试 build 是否成功


4. travis 发布到 S3

gem install travis
travis

http://farseerfc.me/zhs/travis-push-to-github-pages-blog.html

