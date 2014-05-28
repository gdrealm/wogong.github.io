---
layout: wiki
title: cron
---

# CRON
Linux定时任务

## note
1. crontab -e  
每个用户均有个人的计划任务配置，root用户的话需要sudo或者直接~

2. 如果安装过rsyslog (安装 apt-get install rsyslog)，
修改它的配置文件( vim /etc/rsyslog.d/50-default.conf, 把cron那一行注释去掉), 然后重启rsyslog 和 cron 就可以
记录log (/var/log/cron.log)了

3. `MAILTO=username`  
直接邮件通知任务执行情况。

0    1   *  *   5     每周5早上一点运行
0    1   *  *   1-5  每周1到周5早上一点运行
10  *    1  *  *      每个月的第一天的每个小时的第十分钟运行
*/10  *  *  *  *     每十分钟运行

