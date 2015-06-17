---
layout: wiki
title: proxychains
date: 2015-06-17
---


## note

ERROR: ld.so: object 'libproxychains.so.3' from LD\_PRELOAD cannot be preloaded: ignored.

change

export LD\_PRELOAD=libproxychains.so.3 

to

export LD\_PRELOAD=/usr/lib/libproxychains.so.3

in /usr/bin/proxychains


ProxyChains README 
current version: 3.1
======================

This is open source software for GNU/Linux systems.

proxychains - a tool that forces any TCP connection made by any given application
to follow through proxy like TOR or any other SOCKS4, SOCKS5 or HTTP(S) proxy. 
Supported auth-types: "user/pass" for SOCKS4/5, "basic" for HTTP.

proxyresolv - DNS resolving. Used to resolve host names via proxy or TOR.


When to use it ? What for ? Why ?

When you want two (or more) different proxies in chain:
 like: your_host <--> proxy 1 (TOR) <--> proxy 2 (HTTP or SOCKS4/5) <--> target_host

 You may need it when the only way out from your LAN is through proxy server.
 Or to get out from behind restrictive firewall that filters some ports in outgoing traffic.
 And you want to do that with some app like telnet.
 Indeed you can even access your home LAN from outside via reverse proxy if you set it.
 Use external DNS from behind any proxy/firewall.
 Use TOR network with SSH and friends.


Some cool features:

* Different chaining options supported
 random order from the list ( user defined length of chain ).
 exact order (as they appear in the list )
 dynamic order (smart exclude dead proxies from chain)

* You can use it with any application, even network scanners
 oh yes - you can make portscan via proxy (or chained proxies)
 for example with Nmap scanner (www.insecire.org/nmap).
 proxychains nmap -sT -PO -p 80 -iR (find some webservers through proxy)

* Really long chains supported with tunable timeouts.



Configuration:
proxychains looks for config file in following order:
1) ./proxychains.conf
2) $(HOME)/.proxychains/proxychains.conf
3) /etc/proxychains.conf **

**see more in /etc/proxychains.conf

Usage Example:

 bash$ proxychains telnet targethost.com

in this example it will run telnet through proxy(or chained proxies)
specified by proxychains.conf

Usage Example:

 bash$ proxyresolv targethost.com

in this example it will resolve targethost.com through proxy(or chained proxies)
specified by proxychains.conf

NOTE: 
to run suid/sgid programs(like ssh) through proxychains you have to be root

