title: using travis to automatic build pages and sync to Amazon S3
date: 2015-07-11 20:08:33
modified: 2015-07-12 18:18:39
category: 
tags: 
slug: 
authors: wogong
summary: 


1. Register Travis <https://travis-ci.org/>

2. add .tavis.yml first, there is no need to get the file completed at this time

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
first, you should encrypt privacy information by using travis cli `gem install travis`, or you can use [travis api](http://docs.travis-ci.com/api/#repository-keys), which I chosed for the ruby environment really sucks.

        curl -H "Accept: application/vnd.travis-ci.2+json" https://api.travis-ci.org/repos/<github-id/repo>/key | python2 -m json.tool | grep key | sed 's/.*"key": "\(.*\)"/\1/' | xargs -0 echo -en | sed 's/ RSA//' > travis.pem
        # note: <github-id/repo> no '<>'
        # note: this cli command fails in my test, but you can do it by hand, plz see ref[1] for more detail . anyway, you should get the right public key, travis.pem.

then, you can encrypt your privacy info.

        echo -n 'ACCESS_KEY=blah SECRET_KEY=blah' | openssl rsautl -encrypt -pubin -inkey travis.pem | base64 -w0
        # you will get a long base64 string
        # note: no % at the end

last, add the base64 string .travis.yml, and access it by $ACCESS_KEY. see the following finished .tavis.yml file.

        language: python
        python:
            - "2.7"
        env:
            - secure:'blahblah'
        before_install:
            - sudo apt-get update
        install:
            - sudo pip install pelican
            - sudo pip install markdown
            - sudo pip install s3cmd
        script:
            - pelican content
        after_success:
            - s3cmd sync output/ s3://www.wogong.net --acl-public --delete-removed --guess-mime-type --access_key=$ACCESS_KEY --secret_key=$SECRET_KEY

5. git push, see if the build is successful

ref:
* [1] <http://farseerfc.me/zhs/travis-push-to-github-pages-blog.html>

