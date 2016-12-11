---
title: java
date: 2015-02-14
update: 2016-10-22
---

## environment
1. `apt-get install default-jre`

### Eclipse
1. 自动补全：
   最简单的修改方式是：`Windows-->Preferences-->Java-->Editor-->Content Asist，在Auto activation triggers for Java`后面的文本框里只有一个“.”。现在你将其改为“.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ”即可。然后你再试试，会发现，现在的补全功能跟VS差不多了。你还可以在Advanced和Favorite里进行高级的设置。


## Grammar
System.out.print()
System.out.println()

* error
    1. compile-time error / syntax error
    2. run-time error / logic error
    3. divide by zero

在说明这四个关键字之前，我想就class之间的关系做一个简单的定义，对于继承自己的class，base class可以认为他们都是自己的子女，而对于和自己一个目录下的classes，认为都是自己的朋友。

1、public：public表明该数据成员、成员函数是对所有用户开放的，所有用户都可以直接进行调用
2、private：private表示私有，私有的意思就是除了class自己之外，任何人都不可以直接使用，私有财产神圣不可侵犯嘛，即便是子女，朋友，都不可以使用。
3、protected：protected对于子女、朋友来说，就是public的，可以自由使用，没有任何限制，而对于其他的外部class，protected就变成private。

作用域 当前类 同一 package 子孙类 其他package 

public       √ √ √ √ 

protected √ √ √ × 

friendly     √ √ × × 

private     √ × × × 

不写时默认为friendly 
