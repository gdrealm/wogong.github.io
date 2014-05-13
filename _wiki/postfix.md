---
layout: wiki
title: postfix
---

== 学习书籍 ==

[[http://www.amazon.com/Postfix-Definitive-Kyle-Dent-D/dp/0596002122/ref=sr_1_1?ie=UTF8&qid=1367378159&sr=8-1&keywords=postfix|Postfix: The Definitive Guide]]

本书有中文版本。

== 常用命令 ==


删除邮件队列中全部文件：
    
 * postsuper -d ALL 删除队列中全部邮件

 * postsuper -d ID  删除指定ID邮件


显示邮件队列邮件
    postcat -q ID

postmap hash:/etc/postfix/name 大部分文件都需要这样做才OK

/etc/aliases 设置别名

修改之后运行 sudo newaliases生效。

http://unix.stackexchange.com/questions/65013/understanding-etc-aliases-and-what-it-does



----
CategoryApp
