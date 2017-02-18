---
layout: wiki
title: mysql
date: 2015-06-17
update: 2017-01-20
---

## note
1. set names "latin1" 显示中文

## 常用命令
    # shell
    sudo /etc/rc.d/mysqld start
    mysql.server start
    mysql -u root -p
    
    # command
    create database _databsename_
    show databases
    desc _tablename_
    drop database _databasename_
    create table _tablename_
    describe _tablename_
    drop table _tablename_ use aliendatabase
    
    # sql
    select * from aliens_abduction limit 5;
    
    # import
    source filename.sql;


## List of all MySQL commands:
    Note that all text commands must be first on line and end with ';'
    ?         (\?) Synonym for `help'.
    clear     (\c) Clear the current input statement.
    connect   (\r) Reconnect to the server. Optional arguments are db and host.
    delimiter (\d) Set statement delimiter.
    edit      (\e) Edit command with $EDITOR.
    ego       (\G) Send command to mysql server, display result vertically.
    exit      (\q) Exit mysql. Same as quit.
    go        (\g) Send command to mysql server.
    help      (\h) Display this help.
    nopager   (\n) Disable pager, print to stdout.
    notee     (\t) Don't write into outfile.
    pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
    print     (\p) Print current command.
    prompt    (\R) Change your mysql prompt.
    quit      (\q) Quit mysql.
    rehash    (\#) Rebuild completion hash.
    source    (\.) Execute an SQL script file. Takes a file name as an argument.
    status    (\s) Get status information from the server.
    system    (\!) Execute a system shell command.
    tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
    use       (\u) Use another database. Takes database name as argument.
    charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
    warnings  (\W) Show warnings after every statement.
    nowarning (\w) Don't show warnings after every statement.
    
    For server side help, type 'help contents'


