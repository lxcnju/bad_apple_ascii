# bad_apple_ascii
Transfer the video of bad apple to a series of ascii-images.

* 代码架构
* 原理解析
  * 工具介绍
  * 图像转字符画
  * 视频转字符画
* 实例
  * Bad Apple

## 代码架构
 * bad_apple_ascii.py  将Bad Apple视频转为字符画的Python脚本
 * html_tools.py  生成html文件所需要的css样式定义以及逐帧显示字符画的JS脚本
 * load_ascii.py  从文本文件里面读取ascii码表
 * ascii.txt  保存ascii码表的文本文件
 * video  视频目录
 * gif  转成的gif目录
 * html  生成的html目录

## 原理解析
  * 工具介绍
    * Python库
    本项目采用Python3.6实现，需要用到PIL库、skimage库和numpy库。
    * ffmpeg工具
    本项目要涉及到处理视频，因此用![ffmpeg](http://ffmpeg.org/)来处理视频，ffmpeg功能强大，可以截取视频、转换视频格式、将视频转换为Gif，也可以提取出视频中音频等等。
  * 图像转字符画 <br>
  首先，彩色图像是由(r, g, b)三元组构成的像素点矩阵，灰度图像的每个像素点则是一个0~255的值，所以对于彩色图像，要先将之转换为
 
 
