@echo off
title 通过 Git 同步.. 
::Start...
echo Start synchronizing...

echo Commit changes...

:: get date and time 
for /f "delims=" %%a in ('date/t') do @set mydate=%%a 
for /f "delims=" %%a in ('time/t') do @set mytime=%%a 
set fvar=%mydate%%mytime% 

:: add all new files 
call "c:\Users\chengzhen\AppData\Local\GitHub\PortableGit_8810fd5c2c79c73adcc73fd0825f3b32fdb816e7\git-cmd.bat"

call git add . 
call git commit -a -m "Automated commit on %fvar%"

:: push to the server. Default in "origin" remote, "master" branch
call git push
exit
