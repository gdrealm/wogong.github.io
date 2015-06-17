---
layout: wiki
title: nginx
date: 2014-08-30
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


4. Nginx 反代草榴论坛 的配置如下：

        server
        {
        listen 80;
        server_name xxx.xxx;

        location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-Ip $remote_addr;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_pass http://184.154.128.246/;
        }

        }
        #把所有的xxx.xxx改为你自己的域名即可

5. Nginx 反代 Google Scholar 的配置如下：

        server
        {
        listen 443;
        server_name xxx.xxx;

        ssl on;
        ssl_certificate /usr/local/nginx/ssl.crt;#这里改为你自己的证书路径
        ssl_certificate_key /usr/local/nginx/ssl.key;#这里改为自己的密钥路径
        ssl_protocols SSLv3 TLSv1;
        ssl_ciphers ALL:-ADH:+HIGH:+MEDIUM:-LOW:-SSLv2:-EXP;


        location / {
        proxy_redirect http://scholar.google.com/ /;
        proxy_set_header Host "scholar.google.com";
        proxy_set_header Accept-Encoding "";
        proxy_set_header User-Agent $http_user_agent;
        proxy_set_header Accept-Language "zh-CN";
        proxy_set_header Cookie "PREF=ID=047808f19f6de346:U=0f62f33dd8549d11:FF=2:LD=zh-CN:NW=1:TM=1325338577:LM=1332142444:GM=1:SG=2:S=rE0SyJh2W1IQ-Maw";
        proxy_pass http://scholar.google.com;
        sub_filter scholar.google.com xxx.xxx;
        sub_filter_once off;
        }

        }

        server
        {
        listen 80;
        server_name xxx.xxx;
        rewrite ^(.*) https://xxx.xxx/$1 permanent;
        }
        #把所有的xxx.xxx改为你自己的域名
