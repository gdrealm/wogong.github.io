---
layout: wiki
title: nginx
create: 2014-08-30
update: 2014-08-30
---

## 常用命令  
添加php插件后需要重启：

    service nginx restart/reload/stop/start
    service php5-fpm restart/reload/stop/start

## 配置文件
1. 认证

        auth_basic "input you user name and password";
        auth_basic_user_file /path/to/passwd;
        # nginx可以为网站或目录甚至特定的文件设置密码认证。密码必须是crypt加密的。可以用apache的htpasswd来创建密码。
        # htpasswd -b -c pwd username password
2. 目录文件列表功能  
   参考：http://wiki.nginx.org/ChsHttpAutoindexModule  
   如果想希望目录列表支持header,footer则可以安装三方插件: http://wiki.nginx.org/NginxNgxFancyIndex

        autoindex on;
        autoindex_exact_size off; # 默认为on，显示出文件的确切大小，单位是bytes。改为off后，显示出文件的大概大小，单位是kB或者MB或者GB
        autoindex_localtime on; # 默认为off，显示的文件时间为GMT时间。改为on后，显示的文件时间为文件的服务器时间。
3. 301

server {
server_name jefflei.com;
rewrite ^/(.*) http://www.jefflei.com/$1 permanent;
}




## 参考资料
1. 淘宝：http://tengine.taobao.org/book/chapter_02.html
