---
layout: wiki
title: ssl
create: 2000-01-01
update: 2015-01-06
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

XXOO代购SSL证书说明

XXOO代购SSL证书说明 
http://jingyan.baidu.com/album/6766299740dbdd54d41b8456.html?picindex=0 


目录 
1. CSR准备工作 
2. 客服下单, 添加DNS TXT记录 
3. 付款 
4. DNS TXT生效后颁发证书 





1. 您需要准备一份CSR文档, 将内容发给客服;若您嫌麻烦, 客服可以代为生成, 私钥将由客服发给您, 费用另加50元. CSR生成教程见附录. 
2. 等客服下单成功, 客服会通知您往您域名DNS记录中添加一条TXT记录; 格式如下:
DNS TXT: 
globalsign-domain-verification=rHoHVcymojCBz_TwV507r0WuvDhvyjyFYq9kF7u2jsF 

Domain to be Verified: 
(o) www.ssl.so 
(o) ssl.so 

也就是说, 如果您选择www.ssl.so这个域名, 您需要如下步骤添加DNS记录: 
记录 值 TTL 
www globalsign-domain-verification=rHoHVcymojCBz_TwV507r0Wp7hvyjyFYq9kF7u2jsF 600 

同理, 若您选择ssl.so, 添加@的记录即可 

3. 因为域名DNS记录可能会需要较长时间才能生效, 所以我们会要求您在此时付款, 费用为￥300元整; 为避免出错, 请在支付宝备注中注明您的域名 
4. 添加后如果已经生效, 点击verify, 您的域名验证通过后, 证书就会立即颁发; 颁发后客服将立即给您证书; 


___________________________________________________________________________________________________________________________________ 

附录1: CSR生成教程: 

xxoo@ssl:~$ mkdir /tmp/ssl/ 
xxoo@ssl:~$ cd /tmp/ssl/ 
xxoo@ssl:~$ openssl genrsa -out xxoo.pem 2048 
xxoo@ssl:~$ openssl req -new -key xxoo.pem -out xxoo.csr 
You are about to be asked to enter information that will be incorporated 
into your certificate request. 
What you are about to enter is what is called a Distinguished Name or a DN. 
There are quite a few fields but you can leave some blank 
For some fields there will be a default value, 
If you enter '.', the field will be left blank. 
----- 
Country Name (2 letter code) [AU]:CN 
State or Province Name:Shanghai 
Locality Name:PO 
Organization Name:XXOO Co,Ltd 
Organizational Unit Name:Security Dept 
Common Name:*.ssl.so (此栏最重要, 域名出错将不能颁发证书, 泛域请带*.) 
Email Address:xxoo@ssl.so 

Please enter the following 'extra' attributes 
to be sent with your certificate request 
A challenge password []: (此栏留空, 下同) 
An optional company name []: (空) 
xxoo@ssl:~$ 
xxoo@ssl:~$ cat xxoo.csr (将内容直接发给客服, 内容, 不要发文件!) 
-----BEGIN CERTIFICATE REQUEST----- 
MIIC0DCCAbgCAQAwgYoxCzAJBgNVBAYTAkNOMREwDwYDVQQIDAhTaGFuZ2hhaTEL 
MAkGA1UEBwwCUE8xFDASBgNVBAoMC1hYT08gQ28sTHRkMRYwFAYDVQQLDA1TZWN1 
cml0eSBEZXB0MREwDwYDVQQDDAgqLnNzbC5zbzEaMBgGCSqGSIb3DQEJARYLeHhv 
b0Bzc2wuc28wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDGLWukedLI 
GKYmdPcJ9NCwPpKz9YnsRDmIKrt0eRKx/bBNp0Zgx6wMzD9cR2auzXjPs/V1zWya 
8S4LvVJOksdGqxNcLo/vD4RcEkOST6W9+mzRpTJQOBcxA1BNdcqYsRhpnJnjZtn7 
3afucTcsndAlAptAtGVzEYgY4kuRZgFptaFGLlJH8zdQlLXNiKjowEdxAdPhaVFt
RuIetAmfqFQSe13BZjkZyBJI/+eh8sYdI4HMDunH/JE//g+clzr1Zvjty2kskkxY 
WFk3jXQJPOEv6bFp9nDrSX2jIprzqtieIvGI0b5I2WMKYHeG8Nthru+puuPcm6gD 
gGhQFkj9Ni/NAgMBAAGgADANBgkqhkiG9w0BAQUFAAOCAQEAizE8HL85Yg4iPVEo 
QwOLibHq+J1nN+Azbvd+hY6a2lM8+o1a+PVU8tZe3t6U4Mlzfy+VAthkBtUT1JuL 
/yhu7hZHxwyGkYNPpzM6LT16BUpkz5HAoeKTZ6N08L8WDF7jZiz05ctSudmzn+GI 
UGSuYAcq2A7q+dqfQN4o+2cNBP+Y6tYKbpejbxdBYhch/Ekiq3xZQychPU8Xwqsn 
9RyWztqxBhEhg4iL/OAELpOO/f4wLNxV16G4hdY8FwSoGZpSk6XJFBXdnmtXYMS/ 
eW3eiXZXg6Ni8iFAM5CeRJ1H3KBVqFPxyh9jk2zjbiNsAQXL4QS33+gAjinBuT7t 
o77zqw== 
-----END CERTIFICATE REQUEST----- 


附录2: 特殊说明: 
若遇下单失败, 有可能: 
一. 域名问题 
(1) 域名有钓鱼嫌疑, 如 youtube-download.com, google-account.com 之类; 
(2) 域名有违规敏感词语, 如 pay, transfer, earning; 
(3) 域名包含有知名商业公司词语, 如 google, amazon, alibaba, facebook, twitter, baidu之类; 
(4) 域名包含知名高校词语, 如 msit 之类; 
如遇因为域名导致不能下单情况, 请更换域名. 
二. CSR问题 
(5) CSR使用冲突的私钥生成, 虽然概率很小但也有可能; 
如遇CSR问题, 重新生成CSR即可. 


附录3: 中间链证书 
请将下面链证书内容（-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----）附加到您的证书的文件尾 
SHA1 
-----BEGIN CERTIFICATE----- 
MIIELzCCAxegAwIBAgILBAAAAAABL07hNwIwDQYJKoZIhvcNAQEFBQAwVzELMAkG 
A1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv 
b3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw0xMTA0MTMxMDAw 
MDBaFw0yMjA0MTMxMDAwMDBaMC4xETAPBgNVBAoTCEFscGhhU1NMMRkwFwYDVQQD 
ExBBbHBoYVNTTCBDQSAtIEcyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKC 
AQEAw/BliN8b3caChy/JC7pUxmM/RnWsSxQfmHKLHBD/CalSbi9l32WEP1+Bstjx 
T9fwWrvJr9Ax3SZGKpme2KmjtrgHxMlx95WE79LqH1Sg5b7kQSFWMRBkfR5jjpxx 
XDygLt5n3MiaIPB1yLC2J4Hrlw3uIkWlwi80J+zgWRJRsx4F5Tgg0mlZelkXvhpL 
OQgSeTObZGj+WIHdiAxqulm0ryRPYeDK/Bda0jxyq6dMt7nqLeP0P5miTcgdWPh/ 
UzWO1yKIt2F2CBMTaWawV1kTMQpwgiuT1/biQBXQHQFyxxNYalrsGYkWPODIjYYq 
+jfwNTLd7OX+gI73BWe0i0J1NQIDAQABo4IBIzCCAR8wDgYDVR0PAQH/BAQDAgEG 
MBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0OBBYEFBTqGVXwDg0yxh90M7eOZhpM 
EjEeMEUGA1UdIAQ+MDwwOgYEVR0gADAyMDAGCCsGAQUFBwIBFiRodHRwczovL3d3 
dy5hbHBoYXNzbC5jb20vcmVwb3NpdG9yeS8wMwYDVR0fBCwwKjAooCagJIYiaHR0 
cDovL2NybC5nbG9iYWxzaWduLm5ldC9yb290LmNybDA9BggrBgEFBQcBAQQxMC8w 
LQYIKwYBBQUHMAGGIWh0dHA6Ly9vY3NwLmdsb2JhbHNpZ24uY29tL3Jvb3RyMTAf 
BgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzANBgkqhkiG9w0BAQUFAAOC 
AQEABjBCm89JAn6J6fWDWj0C87yyRt5KUO65mpBz2qBcJsqCrA6ts5T6KC6y5kk/ 
UHcOlS9o82U8nxTyaGCStvwEDfakGKFpYA3jnWhbvJ4LOFmNIdoj+pmKCbkfpy61 
VWxH50Hs5uJ/r1VEOeCsdO5l0/qrUUgw8T53be3kD0CY7kd/jbZYJ82Sb2AjzAKb 
WSh4olGd0Eqc5ZNemI/L7z/K/uCvpMlbbkBYpZItvV1lVcW/fARB2aS1gOmUYAIQ 
OGoICNdTHC2Tr8kTe9RsxDrE+4CsuzpOVHrNTrM+7fH8EU6f9fMUvLmxMc72qi+l 
+MPpZqmyIJ3E+LgDYqeF0RhjWw== 
-----END CERTIFICATE----- 

SHA256 
-----BEGIN CERTIFICATE----- 
MIIETTCCAzWgAwIBAgILBAAAAAABRE7wNjEwDQYJKoZIhvcNAQELBQAwVzELMAkG 
A1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv 
b3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw0xNDAyMjAxMDAw 
MDBaFw0yNDAyMjAxMDAwMDBaMEwxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i 
YWxTaWduIG52LXNhMSIwIAYDVQQDExlBbHBoYVNTTCBDQSAtIFNIQTI1NiAtIEcy 
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2gHs5OxzYPt+j2q3xhfj 
kmQy1KwA2aIPue3ua4qGypJn2XTXXUcCPI9A1p5tFM3D2ik5pw8FCmiiZhoexLKL 
dljlq10dj0CzOYvvHoN9ItDjqQAu7FPPYhmFRChMwCfLew7sEGQAEKQFzKByvkFs 
MVtI5LHsuSPrVU3QfWJKpbSlpFmFxSWRpv6mCZ8GEG2PgQxkQF5zAJrgLmWYVBAA 
cJjI4e00X9icxw3A1iNZRfz+VXqG7pRgIvGu0eZVRvaZxRsIdF+ssGSEj4k4HKGn 
kCFPAm694GFn1PhChw8K98kEbSqpL+9Cpd/do1PbmB6B+Zpye1reTz5/olig4het 
ZwIDAQABo4IBIzCCAR8wDgYDVR0PAQH/BAQDAgEGMBIGA1UdEwEB/wQIMAYBAf8C 
AQAwHQYDVR0OBBYEFPXN1TwIUPlqTzq3l9pWg+Zp0mj3MEUGA1UdIAQ+MDwwOgYE 
VR0gADAyMDAGCCsGAQUFBwIBFiRodHRwczovL3d3dy5hbHBoYXNzbC5jb20vcmVw 
b3NpdG9yeS8wMwYDVR0fBCwwKjAooCagJIYiaHR0cDovL2NybC5nbG9iYWxzaWdu 
Lm5ldC9yb290LmNybDA9BggrBgEFBQcBAQQxMC8wLQYIKwYBBQUHMAGGIWh0dHA6 
Ly9vY3NwLmdsb2JhbHNpZ24uY29tL3Jvb3RyMTAfBgNVHSMEGDAWgBRge2YaRQ2X 
yolQL30EzTSo//z9SzANBgkqhkiG9w0BAQsFAAOCAQEAYEBoFkfnFo3bXKFWKsv0 
XJuwHqJL9csCP/gLofKnQtS3TOvjZoDzJUN4LhsXVgdSGMvRqOzm+3M+pGKMgLTS 
xRJzo9P6Aji+Yz2EuJnB8br3n8NA0VgYU8Fi3a8YQn80TsVD1XGwMADH45CuP1eG 
l87qDBKOInDjZqdUfy4oy9RU0LMeYmcI+Sfhy+NmuCQbiWqJRGXy2UzSWByMTsCV 
odTvZy84IOgu/5ZR8LrYPZJwR2UcnnNytGAMXOLRc3bgr07i5TelRS+KIz6HxzDm 
MTh89N1SyvNTBCVXVmaU6Avu5gMUTu79bZRknl7OedSyps9AsUSoPocZXun4IRZZ 
Uw== 
-----END CERTIFICATE----- 


附录4: DNS验证不通过 
若GlobalSign Certificate Center验证地址报错: 
Verification cannot be completed. GlobalSign's verification server is temporally out of service or on system maintenance. Please try again later or contact customer support for a resolution estimate. ErrorCode:-3026 
则有可能由以下原因造成: 
1. 域名之前有过TXT记录, 更新需要20分钟到48小时来生效; 
2. 域名托管在西部数码等调皮等厂商, 限制修改DNS需要延迟生效; 
3. 在加DNS TXT记录前点击Verify了, 因为DNS缓存TTL的原因, 你需要等待2至48小时再验证; 
4. 域名托管在加速乐(jiasule.com), 加速乐违反DNS协议约定, 私自将用户提交的DNS TXT记录值转换成小写, 而x509标准域名验证是严格执行的, 大小写不一致也会导致验证失败. 为了您的生命安全, 请远离加速乐等调皮CDN厂商. 
综上, 为了节约您宝贵的时间建议您使用www.dnspod.cn托管域名. 



附录5: 若浏览器意外关闭 
您可以手工输入CODE继续申请流程.