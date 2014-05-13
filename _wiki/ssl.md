---
layout: wiki
title: ssl
---

即因为SSL协议层是在HTTP协议层下面的，首先进行SSL连接，SSL模块在Web模块之前和浏览器进行通讯并交换证书、建立加密隧道。众所周知，Web服务器是通过HTTP数据包中的”Host”字段来区分虚拟主机的。而SSL模块在把服务器证书发送到浏览器时，还没有收到任何关于HTTP的数据包，当然也就不知道虚拟主机的域名，因此SSL模块只能固定的将一张SSL证书发送到浏览器，而不能根据域名有选择性的发送证书。因此，无法在一个IP地址的默认SSL443端口下为多个虚拟主机配置多张证书。

由于一个IP与一个端口只能对应一张SSL证书，因此我们可以采用以下方式解决：

1、为需要SSL加密的虚拟主机配置不同的IP地址，端口都使用443。例如：www.domain1.com的SSL使用69.96.69.1:443；www.domain2.com的SSL使用69.96.69.2:443，通过https://www.domain1.com和https://www.domain2.com就可以正常访问这2个SSL加密网站了。

2、如果只有一个IP地址，可以为多个网站配置不同的SSL端口。例如：www.domain1.com的SSL使用69.96.69.1:443；www.domain2.com的SSL使用69.96.69.1:800，通过https://www.domain1.com和https://www.domain2.com:800访问这2个SSL网站了。

如果多个虚拟主机使用一个主域名下的不同个子域名，您可以申请通配符Wildcard SSL证书

例如：有2个虚拟主机mail.domain.com、bill.domain.com，你申请一张*.domain.com的证书，按照前面所说的原理，2个虚拟主机都使用同一个IP和默认的443端口，当浏览器访问IP:443端口时，SSL模块把通配符Wildcard SSL证书传送给浏览器，建立合法的SSL隧道，然后WEB模块接收到HTTP数据包时判断域名选择虚拟主机。

原理是可行的，不幸的是你无法按照这个原理对IIS进行配置，IIS不支持SSL端口配置域名。如果仅依靠IIS，你不得不使用上面的2个方法(不同的IP地址或者不同的端口号)。

如果仅有1个IP地址，采用方法2时，mail.domain.com使用443端口，bill.domain.com使用1000端口，你会发现一个现象，由于SSL端口不区分域名，因此无论访问https://mail.domain.com还是https://bill.domain.com都是指向mail.domain.com网站内容；而无论 访问https://mail.domain.com:800还是https://bill.domain.com:800都是指向bill.domin.com网站内容的。当然这也有好处，你可以在abc.domain.com下放一个程序，程序判断一下域名，如果用户访问https://bill.domain.com就马上跳转到https://bill.domain.com:800，不会有任何的安全警告。

幸运的是，通过SSL反向代理服务器，你可以解决这个问题。就是使用第三方的SSL模块来替代IIS处理SSL加密，将证书安装反向代理服务器中，浏览器访问SSL反向代理服务器，然后反向代理服务器使用HTTP协议访问你的Web服务器。你可以选择SSL反向代理硬软件有：

支持SSL的负载均衡器，如F5、ArrayNetworks
使用ISA Server 2004软件。
使用免费的Squid软件。
使用免费的Stunnel软件。
使用PortTunnel软件。
当然，也可以使用多域名SSL

多域名SSL证书与通配型证书是不同的，通配型SSL证书支持 *.domain.com，即支持同一域名下的所有子域，而多域名证书则是任何域名，不仅限于子域，因为一般一个单位有多个域名和一台虚拟主机上有多个不同的用户的域名，如：domain.com、domain.cn、domain.com.cn、domain.net、domain.net.cn、mydomain.com、domain.us等等。