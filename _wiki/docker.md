---
title: docker
date: 2015-08-04 20:34:28
modified: 2015-08-04 20:34:28
category: 
tags: 
slug: 
authors: wogong
summary: 
---


<https://docs.docker.com/articles/dockerfile_best-practices/>

## Get started with images <https://docs.docker.com/userguide/dockerimages/>

    # list images
    docker images
    
    # run bash in the container
    docker run -t -i wogong/run:test /bin/bash

    # Building an image from a Dockerfile
    docker build -t="wogong/cow:test" docker-cow/

    # 



## REF
* <http://segmentfault.com/a/1190000000448808>

