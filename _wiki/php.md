---
layout: wiki
title: php
date: 2015-06-17
---

php参考资料

php官方手册

安装环境：（archlinux）

- php - mysql

使用：

# mysql

sudo /etc/rc.d/mysqld start

mysql -u root -p

create database _databsename_

show databases

drop database _databasename_

create table _tablename_

describe _tablename_

drop table _tablename_ use aliendatabase

select * from aliens_abduction

访问phpmyadmin：http://localhost/phpmyadmin

sha() secure hash algotithm

Setting UTF8 defaults for MySQL is as simple as adding a few lines to your configuration file (typicallymy.cnf):

[mysqld] collation-server = utf8_general_ci character-set-server = utf8
source filename.sql;

[BOTTOM][TOP]ch12 合成与web服务

XML

simplexml_load_file()

RSS

SimpleXMLElement

命名空间


php的文件配置 php.ini

可以采用php --version 简单检查配置文件错误。


基本知识看php手册。


框架学习-Symfony

yml文件的格式十分重要，否则会出各种奇怪的问题。

处理csv文件的函数：fgetcsv


== 框架 ==
[[Symfony]]

== 调试 ==

变量输出：

PHP开发中，经常会查看变量的值，因此经常会将变量的值输出到页面以便于查看。
常用的输出方式有：echo 、print 、print_r 、var_dump 、var_exprot 等；

echo和print常用来输出字符串；

查看数组常用print_r、var_dump、var_exprot；

若使用echo和print输出数组时则，结果只能显示"Array"，不会显示数组的结构。

一下举一例说明几种用法

配合print "<pre>"和print "</pre>"，以数组$a为例说明各种输出的区别。
$a = array ('a' => 'apple', 'b' => 'banana', 'c' => array ('x', 'y', 'z'));

 

print_r($a); 
输出结果：

Array ( [a] => apple [b] => banana [c] => Array ( [0] => x [1] => y [2] => z ) ) 

print "<pre>"; print_r($a); print "</pre>"; 
输出结果：
Array
(
    [a] => apple
    [b] => banana
    [c] => Array
        (
            [0] => x
            [1] => y
            [2] => z
        )

)

var_dump($a); 
输出结果：



array(3) { ["a"]=>  string(5) "apple" ["b"]=>  string(6) "banana" ["c"]=>  array(3) { [0]=>  string(1) "x" [1]=>  string(1) "y" [2]=>  string(1) "z" } } 



print "<pre>"; var_dump($a); print "</pre>"; 
输出结果：

array(3) {
  ["a"]=>
  string(5) "apple"
  ["b"]=>
  string(6) "banana"
  ["c"]=>
  array(3) {
    [0]=>
    string(1) "x"
    [1]=>
    string(1) "y"
    [2]=>
    string(1) "z"
  }
}

var_export($a); 

print "<pre>"; var_export($a); print "</pre>"; 
输出结果：

array (
  'a' => 'apple',
  'b' => 'banana',
  'c' => 
  array (
    0 => 'x',
    1 => 'y',
    2 => 'z',
  ),
)


调试的时候可以根据不同的需要选用不同的输出方式。
