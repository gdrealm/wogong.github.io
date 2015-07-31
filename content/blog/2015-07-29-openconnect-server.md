title: openconnect server
date: 2015-07-29 17:39:48
modified: 2015-07-29 17:39:48
category: 
tags: 
slug: 
authors: wogong
summary: 

Cisco Anyconnect，这并不是一个科学上网商业服务，也不是一个免费的 App，她是 Cisco 研发的企业级 SSL VPN 解决方案，早期只用于 Cisco 的企业用户，背后是开源技术 OpenConnect，简单来说就是对使用 UDP 的 DTLS 协议进行加密，掉线时自动使用 TCP 的 TLS 协议进行备份恢复，所以与其他 VPN（L2TP/PPTP） 比较稳定，可以保持长时间在线，与 Cisco 之前推出（连过 iOS 内置 VPN 的都见过，上面有个 Cisco 的 LOGO）的 IPSec VPN 相比, AnyConnect 在用户认证管理和安全协议等方面更加强大，而且 AnyConnect 对于长 Latency 网络有更高的容忍度。你可以在自己的 VPS 主机上通过 ocserv 搭建 Anyconnect 服务，与 Shadowsocks 有些像吧？综合以上几点，可以发现 Anyconnect 很适合当前大局域网的网络现状，她支持各种平台，Mac, Win, Android, iOS, Linux 涵盖很广。

## server
OpenConnet Server（ocserv）是朋友给我的建议，它通过实现Cisco的AnyConnect协议，用DTLS作为主要的加密传输协议。我认为它的主要好处在于——

AnyConnect的VPN协议默认使用UDP DTLS作为数据传输，但如果有什么网络问题导致UDP传输出现问题，它会利用最初建立的TCP TLS通道作为备份通道，降低VPN断开的概率。
AnyConnect作为Cisco新一代的VPN解决方案，被用于许多大型企业，这些企业依赖它提供正常的商业运作，这些正常运作对应的经济效益（读作GDP），是我们最好的伙伴。
OpenConnet的架设足够麻烦，我的意思是，如果你不是大型企业，你会用AnyConnect的概率无限趋近于零。再者，如果它足够简单，我就不用写这篇文章了。
至于它的自定义路由表支持，我觉得都是次要了。

介绍到此，让我们按步骤干好事情。

（下文选用最新的Ubuntu 14.04 LTS和OCServ 0.10.5作为标准环境，但我会尽量提供不依赖版本的步骤与建议。）

编译OCserv

到官方站点找最新的OpenConnect Server版本。

curl -O ftp://ftp.infradead.org/pub/ocserv/ocserv-0.10.5.tar.xz

tar xvf ocserv-0.10.5.tar.xz

cd ocserv-0.10.5

看下README文件提及的编译依赖。理论上只有libgnutls-dev和libreadline-dev是必须的，但我们还是把可选的功能都带上。

（顺便一提，如果你在Ubuntu 14.04或更早版本上，libgnutls-dev的版本还是2.x，需要用libgnutls28-dev获取3.x的GnuTLS才能支持OCserv。）

sudo apt-get install build-essential pkg-config libgnutls28-dev libreadline-dev libseccomp-dev libwrap0-dev libnl-nf-3-dev liblz4-dev

编译并安装。

./configure

（在我测试的环境里，最终报告只有systemd、dbus、PAM、Radius、GSSAPI的结果为no，如果你发现其他项目显示no，不必担心，你的环境可能安装了可选的包导致出现不同结果。目前只有libgnutls28-dev是必须的模块。）

（在Ubuntu 14.04上，liblz4-dev缺了pkg-config文件，所以即便安装了liblz4-dev，LZ4支持仍显示no。LZ4支持是ocserv 0.10下的新功能，装不装对使用没大碍，如果需要，你得想办法手动安装LZ4。）

make

sudo make install

配置OCserv

我们希望做到的，是无需用户名与密码的客户端证书验证登陆。但在此之前，让我们先测通更简单的密码登录模式。首先让我们把CA证书与服务器证书生成好，具体步骤官方文档也有——

先准备好certtool命令。

sudo apt-get install gnutls-bin

创建CA

mkdir certificates

cd certificates

CA模板，创建ca.tmpl，按需填写，这里的cn和organization可以随便填。

cn = "Your CA name" 
organization = "Your fancy name" 
serial = 1 
expiration_days = 3650
ca 
signing_key 
cert_signing_key 
crl_signing_key

CA密钥

certtool --generate-privkey --outfile ca-key.pem

CA证书

certtool --generate-self-signed --load-privkey ca-key.pem --template ca.tmpl --outfile ca-cert.pem

同理，我们用CA签名，生成服务器证书。先创建server.tmpl模板。这里的cn项必须对应你最终提供服务的hostname或IP，否则AnyConnect客户端将无法正确导入证书。

cn = "Your hostname or IP" 
organization = "Your fancy name" 
expiration_days = 3650
signing_key 
encryption_key
tls_www_server

Server密钥

certtool --generate-privkey --outfile server-key.pem

Server证书

certtool --generate-certificate --load-privkey server-key.pem --load-ca-certificate ca-cert.pem --load-ca-privkey ca-key.pem --template server.tmpl --outfile server-cert.pem

将CA，Server证书与密钥复制到以下文件夹

sudo cp ca-cert.pem /etc/ssl/private/my-ca-cert.pem

sudo cp server-cert.pem /etc/ssl/private/my-server-cert.pem

sudo cp server-key.pem /etc/ssl/private/my-server-key.pem

剩下的就是OCServ配置文件了。同样的，参考官方文档是最佳选项，但为了方便起见，这是你需要注意的一些设置。回到ocserv-0.10.5的文件夹下，将配置文件复制到OCserv默认读取的位置。

sudo mkdir /etc/ocserv

sudo cp doc/sample.config /etc/ocserv/ocserv.conf

确保以下配置正确

# 登陆方式，目前先用密码登录
auth = "plain[/etc/ocserv/ocpasswd]"

# 允许同时连接的客户端数量
max-clients = 4

# 限制同一客户端的并行登陆数量
max-same-clients = 2

# 服务监听的IP（服务器IP，可不设置）
listen-host = 1.2.3.4

# 服务监听的TCP/UDP端口（选择你喜欢的数字）
tcp-port = 9000
udp-port = 9001

# 自动优化VPN的网络性能
try-mtu-discovery = true

# 确保服务器正确读取用户证书（后面会用到用户证书）
cert-user-oid = 2.5.4.3

# 服务器证书与密钥
server-cert = /etc/ssl/private/my-server-cert.pem
server-key = /etc/ssl/private/my-server-key.pem

# 客户端连上vpn后使用的dns
dns = 8.8.8.8
dns = 8.8.4.4

# 注释掉所有的route，让服务器成为gateway
#route = 192.168.1.0/255.255.255.0

# 启用cisco客户端兼容性支持
cisco-client-compat = true

创建一个登陆用的用户名与密码。

sudo ocpasswd -c /etc/ocserv/ocpasswd your-username

这样OCserv就基本配置好了。但如果你和我一样强化过服务器安全，还得为服务器上开些端口才行。以Linode的安全配置为例，我们需要加入和修改以下内容。

sudo nano /etc/iptables.firewall.rules

打开OCserv对应的TCP/UDP端口（别忘了对应你选择的端口数）

-A INPUT -p tcp -m state --state NEW --dport 9000 -j ACCEPT
-A INPUT -p udp -m state --state NEW --dport 9001 -j ACCEPT

注释这行，允许转发

# -A FORWARD -j DROP

启用NAT

*nat
-A POSTROUTING -j MASQUERADE
COMMIT

完成之后导入新配置并检查配置正确。

sudo iptables-restore < /etc/iptables.firewall.rules

sudo iptables -L

sudo iptables -t nat -L

如果你之前没有配置服务器启动时自动导入这个设置

sudo nano /etc/network/if-pre-up.d/firewall

输入以下内容

#!/bin/sh 
/sbin/iptables-restore < /etc/iptables.firewall.rules

最后我们需要打开IPv4的流量转发。

sudo nano /etc/sysctl.conf

启用此项

net.ipv4.ip_forward=1

并刷新配置

sudo sysctl -p /etc/sysctl.conf

测试OCserv

在服务器端启动OpenConnect Server。

sudo ocserv -f -d 1

如果服务没错误退出，是时候来测测客户端了。假设你使用iOS，下载Cisco AnyConnect。

在Connections下加入新的VPN配置，在服务器地址栏目上填入对应的IP/Hostname和TCP端口（我们的例子就是1.2.3.4:9000）

然后到设置标签页下暂时禁用“阻止不信任的服务器”选项。首次连接，AnyConnect会提示你这是不信任证书，如果你之前的服务器证书模板的cn没写错的话（我们的例子是1.2.3.4），你可以接受并导入该证书（可在诊断标签页的证书菜单里的服务器证书列表看到）。以后即便启用“阻止不信任的服务器”选项，也不会报错了（和SSH首次登陆类似）。

确定VPN连接正常并可以科学上网后，我们可以接着提高网络生活质量。

自动化OCserv

假如现有的配置有哪里让人不大满意，大概是这两点——

OCserv的服务最好会自动跑，进程挂了也自动恢复。
AnyConnect每次都要输入密码很麻烦，最好用客户端证书验证。
为OCserv写个简单的upstart脚本。

cd /etc/init.d

sudo ln -s /lib/init/upstart-job ocserv

cd /etc/init

sudo nano ocserv.conf

放入以下内容

#!upstart
description "OpenConnect Server"

start on runlevel [2345]
stop on runlevel [06]

respawn
respawn limit 20 5

script
    exec start-stop-daemon --start --pidfile /var/run/ocserv.pid --exec /usr/local/sbin/ocserv -- -f >> /dev/null 2>&1
end script

这样就可以用以下方式启动/暂停服务

sudo service ocserv start

sudo service ocserv stop

为AnyConnect建个客户端证书

和服务器端证书的步骤基本相同。回到之前的certificates文件夹。

创建user.tmpl

cn = "some random name"
unit = "some random unit"
expiration_days = 365
signing_key
tls_www_client

User密钥

certtool --generate-privkey --outfile user-key.pem

User证书

certtool --generate-certificate --load-privkey user-key.pem --load-ca-certificate ca-cert.pem --load-ca-privkey ca-key.pem --template user.tmpl --outfile user-cert.pem

然后要将证书和密钥转为PKCS12的格式。

certtool --to-p12 --load-privkey user-key.pem --pkcs-cipher 3des-pkcs12 --load-certificate user-cert.pem --outfile user.p12 --outder

然后我们要通过URL将user.p12文件导入AnyConnect，具体位置在诊断标签页的证书栏目下。如果你的服务器已经有Nginx/Apache服务，只要传到一个可以访问的URL路径下即可。另一个选择是将user.p12复制到本地，建立一个HTTP服务（例如用node.js）。

导入成功之后，将对应的VPN设置的高级设置部分的证书栏目，改为导入的这张证书。

最后我们要调整下OCserv的配置——

sudo nano /etc/ocserv/ocserv.conf

修改以下内容

# 改为证书登陆，注释掉原来的登陆模式
auth = "certificate"

# 证书认证不支持这个选项，注释掉这行
#listen-clear-file = /var/run/ocserv-conn.socket

# 启用证书验证
ca-cert = /etc/ssl/private/my-ca-cert.pem

重启OCserv服务，确认VPN无需密码就可以正常登陆。



* [折腾笔记：架设OpenConnect Server给iPhone提供更顺畅的网络生活](http://bitinn.net/11084/)
* <https://www.linode.com/docs/security/securing-your-server>
* <http://www.infradead.org/ocserv/manual.html>
* <http://www.infradead.org/ocserv/download.html>



## client

### iOS

### Windows
导入客户端证书

开始菜单搜索“cmd”，打开后输入 mmc（Microsoft 管理控制台）

“文件”-“添加/删除管理单元”，添加“证书”单元，证书单元的弹出窗口中一定要选“计算机账户”，之后选“本地计算机”，确定。

在左边的“控制台根节点”下选择“证书”-“个人”，然后选右边的“更多操作”-“所有任务”-“导入”打开证书导入窗口。选择刚才生成的 client.cert.p12 文件。下一步输入私钥密码。

下一步“证书存储”选“个人”，导入成功后，把导入的 CA 证书复制到“受信任的根证书颁发机构”的证书文件夹里面，

打开剩下的那个私人证书，看一下有没有显示“您有一个与该证书对应的私钥”，以及“证书路径”下面是不是显示“该证书没有问题”然后关闭 mmc，提示“将控制台设置存入控制台1吗”，选“否”即可，至此，证书导入完成


# temp
no-route 指定不走vpn的ip段
route 指定走vpn的ip段
二者不能同时使用

