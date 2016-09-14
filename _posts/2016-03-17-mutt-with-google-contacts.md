---
title: mutt with Google Contact
date: 2016-03-17
---

## install
1. install goobook
    
    pip install --user goobook
    # in arch you should
    pip2 install --user goobook

2. config goobook

    # fisrt get the config template
    $ goobook config-template > .goobookrc
    # "#" or ";" at the start of a line makes it a comment.
    [DEFAULT]
    # The following are optional, defaults are shown
    ...
    [DEFAULT]
    # The following are optional, defaults are shown
    email: you@gmail.com
    password: yourgooglepassword

3. goobook authenticate

    goobook authenticate — non-local-browser

4. config mutt

## .muttrc
    
    #...
    set query_command=”goobook query %s”
    macro index,pager a “<pipe-message>goobook add<return>” “add sender to google contacts”
    bind editor <Tab> complete-query
    #...

## REF
<https://hynek.me/articles/my-mutt-gmail-setup/>
