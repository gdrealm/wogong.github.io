---
layout: wiki
title: expect
---

expect

#!/usr/bin/expectset timeout 60
spawn /usr/bin/ssh -D 本地端口 -g 用户名@服务器
expect {
"password:" {
send "密码\r"
}
}
interact {
timeout 60 { send " "}
}
