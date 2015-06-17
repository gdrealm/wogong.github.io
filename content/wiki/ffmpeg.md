---
layout: wiki
title: ffmpeg
date: 2014-07-03
---


## Usage

### VPS

1. ID3 mid3iconv
2. mp32aac.sh
3. `mv *.m4a directory`
4. `tar zcvf directory aac.tar.gz`
### ffmpeg + foobar2000 FLAC/APE to iTunes ALAC(m4a)

至于AAC，Windows 上的 ffmpeg 编译无力，还是 iTunes

### Video

➢ ffmpeg是什么，懂的大侠跳过。。。
一款开源的跨平台的命令行软件，同时也是一套程序库，处理视频、音频的神器。。。
命令行？听起来好像很难用，咱看电影不就娱个乐嘛，折腾啥呢？
其实按我说的来用，真心很简单，咱也不说那些高端的，就说点简单实用的。
另外，怎么说，折腾其实是生活态度的问题，娱乐也不仅仅是打发时间，也是生命的一部分，不多说了。。。

➢ 我用ffmpeg干什么？
★ 转换格式
为什么要转格式呢？因为希望用系统播放器。
这里有软解码和硬解码的问题、Airplay的问题、AC3支持的问题、iTunes家庭共享的问题、收藏的问题，等等吧，就不展开说了。


★ 嵌字幕
iTunes不支持外挂字幕，这个确实很蛋疼。

➢ 下面开始演示，重点啊！
★ 我这有部《肖生克的救赎》，视频和字幕已经通过合法途径获取：
The.Shawshank.Redemption.1994.Bluray.x264.anoXmous.mkv
The.Shawshank.Redemption.1994.Bluray.x264.anoXmous_eng.srt

★ 那我就这样
$ ffmpeg -i The.Shawshank.Redemption.1994.Bluray.x264.anoXmous.mkv \
-i The.Shawshank.Redemption.1994.Bluray.x264.anoXmous_eng.srt \
-map 0:0 -map 0:1 -map 1:0 \
-vcodec copy -acodec copy -scodec mov_text \
-y The.Shawshank.Redemption.1994.Bluray.x264.anoXmous.mp4

★ 下面解释一下参数
-i 原视频文件.mkv #这个好理解吧
-i 原字幕文件.srt #这个也好理解了吧
-map n:m #这个是说，我要其中第n个输入文件的第m个流，这里mkv就是n=0，srt就是n=1，等下再说m
-vcodec copy #这是说视频编码格式不变
-acodec copy #同上，音频
-scodec mov_text #指定字幕的编码格式
-y 目标文件.mp4 #直接覆盖，不询问

★ 没看明白的，往下读。。。
流（或者叫“轨”吧）是怎么回事？
你输入这个命令
$ ffmpeg -i 视频文件.mkv
注意找下输出里类似这样的内容：
Stream #0:0(und): Video: h264 ......
Stream #0:1(eng): Audio: aac ......
Stream #0:2: Subtitle: mov_text ......
他们分别是视频的、音频的和字幕的，三种类型的流。有的时候可能没有字幕流，有的时候可能不止一个音频流，因为有不同语言，这都很正常。
重要的是你要先通过这个命令来看看有哪些流，然后挑选你要的，所以这个m，你知道该怎么填了吧。

★ 再说codec
因为这里原始文件就是h264和aac，系统默认支持，所以就不需要转成别的编码，这样就避免了重编码（一些转码软件脑残至极啊！h264转h264啊！慢到死的节奏啊！）。
所以你直接写copy，就是直接硬盘复制的节奏啦！当然你需要的话，可以转成其他的编码，比如音频转成mp3编码，就是“-acodec mp3”，不过那样就不是复制的节奏了，会慢好些哦。。。
字幕，因为是外挂的，所以就需要指定编码格式了，我只用过mov_text，其他不了解了。

★ 既然视频和音频编码都没有改变，那转个什么劲？
其实重要的是转封装，简单说就是视频文件的格式吧，.mkv文件，iTunes就不认得，.mp4谁都认得。

➢ 最后外挂一下，ffmpeg软件如何获取，Mac下推荐用Homebrew，相当方便！
Windows好像可以直接下载编译好的.exe，Linux下用apt-get什么的更爽了。
安装Homebrew:
$ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
安装ffmpeg:
$ brew install ffmpeg


如果原文件的流都需要的话，可以不用写-map n:m

如果想指定音频和字幕语言的话，可以加上
-metadata:s:a:0 language=eng #s就是stream，a就是音频，0就是第0个音轨
-metadata:s:s:0 language=eng #第二个s是subtitle



## audio

1. VBR
mp3 中比特率的含义是：在压缩音频文件至mp3时，由压缩软件所确
定数码文件在播放时每秒传送给播放器大小，其单位是：千位/秒；
英文的含义是：kbps - = kilobits per second。现在mp3文件的最
高数位率是320 kbps。这样的文件体积很大，每分钟的音乐超过两兆
字节。如果采用可变比特率（VBR）编码来生成mp3文件，获得与320 kbps
相当音质，文件的体积会缩小25~50%。请注意：播放时间相同，
而歌曲不同，所获的压缩mp3文件的一般不相同，这是因为VBR编码
所生成的mp3文件的大小不仅仅取决于播放时间的长度，还取决于
源音频文件的其它因素。


2. ID3
MP3 的 ID3 采用 GBK 编码就是坑人，ffmpeg 转过之后根本没办法
被大部分软件识别，还是转码之前用 mid3iconv 转换为 unicode 编码比较靠谱。

    mid3iconv -e gbk name.mp3
    mid3iconv -e gbk *.mp3

ffmpeg -i name.mp3 -f ffmetadata metadata.txt

## codec
1. AAC
AAC is Advanced Audio Coding.
https://trac.ffmpeg.org/wiki/AACEncodingGuide

For AAC-LC the likely answer is: libfdk_aac > libfaac > Native FFmpeg AAC encoder (aac) > libvo_aacenc.
17.4.2 Examples
Use ffmpeg to convert an audio file to VBR AAC in an M4A (MP4) container:
 	
    ffmpeg -i input.wav -codec:a libfdk_aac -vbr 3 output.m4a

Use ffmpeg to convert an audio file to CBR 64k kbps AAC, using the High-Efficiency AAC profile:
 	
    ffmpeg -i input.wav -c:a libfdk_aac -profile:a aac_he -b:a 64k output.m4a

2. ALAC

ALAC is the Apple Lossless Audio Codec



## INSTALL
1. Windows 简单，下载个就好，自己编译就 hard 了，不考虑
2. Linux 有静态编译好的，适合懒人。当然也可以自己编译，比如需要某些解码器

### compile FFMPEG on debian
https://trac.ffmpeg.org/wiki/UbuntuCompilationGuide#ffmpeg

sudo apt-get -y install autoconf automake build-essential libass-dev libfreetype6-dev libgpac-dev \
   libtheora-dev libtool libvorbis-dev pkg-config texi2html zlib1g-dev


sudo apt-get install yasm libmp3lame-dev

    ./configure --prefix="$HOME/ffmpeg_build" --extra-cflags="-I$HOME/ffmpeg_build/include" \
    --extra-ldflags="-L$HOME/ffmpeg_build/lib" --bindir="$HOME/bin" --extra-libs="-ldl" --enable-gpl \
    --enable-libass --enable-libfdk-aac --enable-libfreetype --enable-libmp3lame \
    --enable-libtheora --enable-libvorbis --enable-nonfree



