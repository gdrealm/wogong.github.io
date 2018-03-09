--
title: mac
date: 2017-09-29
---

关于 Mac 的一些使用备忘。

## 截图
com.apple.screencapture location /Desktop/ScreenShots
killall SystemUIServer

defaults write com.apple.screencapture type jpg
killall SystemUIServer

defaults write com.apple.screencapture disable-shadow -bool true
killall SystemUIServer
defaults write com.apple.screencapture disable-shadow -bool false
killall SystemUIServer

defaults write com.apple.screencapture name "我的截图"
killall SystemUIServer
defaults write com.apple.screencapture name "\$ScreenShot"
killall SystemUIServer

networksetup -setdnsservers（网络服务）（DNS IP）

例如，将Wi-Fi设置为Google的DNS为8.8.8.8语法将为

networksetup -setdnsservers Wi-Fi 8.8.8.8