title: proxychains
date: 2015-06-17
modified: 2015-08-03 21:54:07

## note

ERROR: ld.so: object 'libproxychains.so.3' from LD\_PRELOAD cannot be preloaded: ignored.

change

export LD\_PRELOAD=libproxychains.so.3 

to

export LD\_PRELOAD=/usr/lib/libproxychains.so.3

in /usr/bin/proxychains


ProxyChains README 
current version: 3.1

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

see more in /etc/proxychains.conf

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


最近这段时间需要在Linux下做开发，我的机子是通过一台windows机器上的CCProxy代理上网。可是在设置了系统代理以后，发现在终端下若要进行ftp或者ssh等操作，并不能使用代理（但是wget是可以的）。期间试过一些方法，比如在.bash_profile里面设置http_proxy等，都没有达到使用代理的效果。最后发现了一个很好用的代理客户端软件，它同时支持http代理和socks4与socks5代理。可以从http://proxychains.sourceforge.net/轻松下载到proxychains-3.\*.tar.gz文件，目前最新版本是3.1版，它可以支持几乎所有程序的代理，包括ssh，telnet，ftp，cvs等，只要在命令前多输一个proxychains命令。
安装和配置也很简单，安装我就不多说了，它的配置文件是按照以下顺序寻找的：
1. ./proxychains.conf
2. $(HOME).,proxychains/proxychains.conf
3. /etc/proxychains.conf
找到该文件后，就可以在里面添加代理服务器列表：
可以选择三种代理方式：dynamic_chain, strict_chain, random_chain
第一种方式是动态的，它按照代理服务器在列表中出现的先后顺序（A,B,C,...）将这些代理服务器串成一条链，但是不要求链上每一台代理服务器都是在线的，至少有一台代理服务器在线即可；
第二种方式是严格的，它按照代理服务器在列表中出现的先后顺序（A,B,C,...）将这些代理服务器串成一条链，要求链上每一台代理服务器都是在线的；
第三种方式是随机的，链中的代理服务器的任何一台都可以成为所使用的代理服务器（链长有chain_len指定），这种方式很适合网络扫描操作（参数chain_len只对random_chain有效）。
给出使用random_chain的配置实例：

        random_chain
        chain_len=1
        tcp_read_time_out 15000
        tcp_connect_time_out 10000
        
        [ProxyList]
        http        ***.***.***.*** 808
        socks5   ***.***.***.*** 1080


使用也非常方便：
如通过代理ssh：
          # proxychains ssh abc.efg.com
通过代理telnet：
          # proxychains telnet abc.efg.com
通过代理ftp：
          # proxychains ftp
          > ftp cd ..

cvs同样也可以。

