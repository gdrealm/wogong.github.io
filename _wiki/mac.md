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