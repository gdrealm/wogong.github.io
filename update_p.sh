#!/bin/sh

git pull
gfwlist2pac -f ~/blog/p -p "SOCKS5 127.0.0.1:8080; SOCKS 127.0.0.1:8080; HTTPS node-cnx.vnet.link:111; PROXY node-cnx.vnet.link:110; DIRECT;" --user-rule ~/blog/file/user_rule.txt
git c -am "update pac"
git push
