title: using travis to automatic build pages and sync to Amazon S3
date: 2015-07-11 20:08:33
modified: 2015-07-12 18:18:39
category: 
tags: 
slug: 
authors: wogong
summary: 


1. Register Travis <https://travis-ci.org/>

2. add .tavis.yml first, there is no need to get the file completed at this time.

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
            - pelican content

3. git push to test if the travis build is successful

4. sync to Amazon S3



ref:
* [1] <http://farseerfc.me/zhs/travis-push-to-github-pages-blog.html>

