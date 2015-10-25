---
title: transmission
date: 2014-07-18
modified: 2015-07-31 17:21:39
---


sudo apt-get install transmission-daemon

.config/transmission/settings.json

sudo service transmission-daemon stop

sudo cp .config/transmission/settings.json /etc/transmission-daemon

sudo service transmission-daemon start
