---
title: pip
date: 2015-10-30 23:29:47
modified: 2015-10-30 23:29:47
---

## install
<http://pip.readthedocs.org/en/latest/installing.html>
`sudo apt-get install pip`

## usage

1. --user (recommend)
    
    # install to ~/.local
    pip install --user pkg_name

2. virtualenv

    sudo pip install virtualenv
    virtualenv NEW
    cd NEW
    source ./bin/activate
    pip list
    deactivate
    virtualenv -p /usr/bin/python2.7 ENV2.7
    * virtualenv --relocatable ./
    * pip freeze > requirements.txt
      pip install -r requirements.txt
    # ref:<http://www.jianshu.com/p/08c657bd34f1>

3. command

    pip install -U
    pip uninstall
