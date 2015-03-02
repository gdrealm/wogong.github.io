---
layout: wiki
title: javascript
create: 2015-02-14
update: 2015-02-14
---
## javascript
1. variables `var counter=140;`
        var tweet = "hello world";
        var lenght = tweet.length;
2. comparisons
        > - Greater than
        < - Less than
        >= Greater than or equal to
        <= Less than or equal to
        === Equal to
        !== Not equal to
3. if
        if(condition) {
        
        }
4. function
        var main = funtion(parameters) {
        
        };

## jQuery
1. main
        var main=function() {
            
        }
            
        $(document).ready(main) //$(document)选择整个网页
5. Event
  - .click()
  - .keypress()
          var main = function() {
            $(document).keypress(function() {
              $(".btn").toggleClass("btn-like");
              });
            };
          $(document).ready(main);
          
          //键盘m
          $(document).keypress(function(event) {
            if(event.which === 109) {
              $('.dropdown-menu').toggle();
              }
            });
  - 
  
          


## other 

学习教材：《JavaScript网页编程从入门到精通》 北京科海电子出版社 


第一篇 语言概述

CHAPTER 1 JavaScript概述
1.1概念

1.2基本特点及其与Java的比较

1.3作用
1.3.1进行交互
1.3.2进行本地验证

1.4应用
1.4.1服务器端应用
1.4.2客户端应用

1.5如何使用
1.5.1嵌入JavaScript
1.5.2链接JavaScript

1.6怎样编写
1.6.1使用纯文本编辑器
1.6.2专业脚本编辑工具 

1.7如何运行


CHAPTER 2 HTML是学习JavaScript的基础


CHAPTER 3 JavaScript基本语法
3.1注释
3.1.1单行注释 //注释文字
3.1.2多行注释  /*多行注释文字*/
3.1.3隐藏脚本注释 <--! //-->

3.2关键字 基本关键字（报错）+特殊关键字（不报错）

3.3<script>标记
3.3.1属性设置 language/type（HTML自身）；src（js路径）
3.3.2位置 head或者body标签内
3.3.3数量 没有要求

3.4分号 一句代码可以不使用（不会报错，不推荐），多行代码需要使用。

3.5数据类型
3.5.1基本数据类型
整数 十进制；19进制：0X或者0x前缀；八进制：加0
浮点数 基本形式+指数形式（指数不得超过3位，需为整数）
string
boolean布尔型
3.5.2特殊数据类型
null
undefined
3.5.3数据类型转换
基本数据类型转换为字符串型 toString()
字符串型转换成数值型 parseInt;parseFloat
转换为布尔型
其他数据类型转换成数值型
特殊数值类型转换为字符串安

3.6变量
3.6.1变量命名 六条命名规则
3.6.2变量声明和初始化 关键字var
3.6.3变量类型 弱变量语言，在程序运行中类型可以改变
3.6.4变量作用域 局部变量/全局变量。（二者可以同名【不推荐】；函数体中必须采用var声明局部变量，否则为全局变量。）


CHAPTER4 JavaScript运算符


CHAPTER5 JavaScript结构语句
