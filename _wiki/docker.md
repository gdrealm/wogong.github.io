---
title: docker
date: 2015-08-04 20:34:28
update: 2018-01-24
---


<https://docs.docker.com/articles/dockerfile_best-practices/>

## Get started with images <https://docs.docker.com/userguide/dockerimages/>

    # list images
    docker images
    
    # run bash in the container
    # t means tag
    docker run -ti wogong/run:test /bin/bash

    # Building an image from a Dockerfile
    docker build -t wogong/cow:test docker-cow/

    docker build --no-cache




## REF
* <http://segmentfault.com/a/1190000000448808>

