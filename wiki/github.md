---
title: github
date: 2015-06-17
modified: 2015-07-12 20:12:06
---

https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages

$ dig www.wogong.net +nostats +nocomments +nocmd

; <<>> DiG 9.8.4-rpz2+rl005.12-P1 <<>> www.wogong.net +nostats +nocomments +nocmd
;; global options: +cmd
;www.wogong.net.			IN	A
www.wogong.net.		600	IN	CNAME	wogong.github.com.
wogong.github.com.	30	IN	CNAME	github.map.fastly.net.
github.map.fastly.net.	10	IN	A	103.245.222.133

