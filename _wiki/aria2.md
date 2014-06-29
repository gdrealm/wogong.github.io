---
layout: wiki
title: aria2
update: 2014-06-29
---

aria2c --http-auth-challenge=true http://username:passwd@dl.wogong.net/MIT/MITRES2_002S10linear_lec01_300k.mp4

http://www.archive.org/download/MITRES2_002S10nonlinear/MITRES2_002S10nonlinear_lec01_300k.mp4

You can avoid this error by specifying CA certificate file using --ca-certificate option. If you are using Debian/Ubuntu, first install ca-certificates and give --ca-certificate=/etc/ssl/certs/ca-certificates.crt to aria2c. This is the proper and secure way.
There is another insecure way to avoid this error. Just give --check-certificate=false to aria2c.
This is easier than previous one, but it is insecure because it does not verify remote server.


aria2c -i list.txt
