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
  * 工具介绍 <br>
    * Python库 <br>
    本项目采用Python3.6实现，需要用到PIL库、skimage库和numpy库。
    * ffmpeg工具 <br>
    本项目要涉及到处理视频，因此用[ffmpeg](http://ffmpeg.org/)来处理视频，ffmpeg功能强大，可以截取视频、转换视频格式、将视频转换为Gif，也可以提取出视频中音频等等。
  * 图像转字符画 <br>
    首先，彩色图像是由(r, g, b)三元组构成的像素点矩阵，灰度图像的每个像素点则是一个0\~255的值，所以对于彩色图像，要先将之转换为灰度图像，方法是利用gray = 0.3 * R + 0.59 * G + 0.11 * B。将彩色图像转为灰度图像之后，像素点的值就是0\~255中的一个整数。<br>
    然后，读取ascii码表，利用公式：index = gray * len(ascii) / 255来计算这个图像像素点灰度在ascii码表中的index，然后该点像素点在字符画对应的位置就是用ascii\[index\]来表示。一般来说，为了视觉效果，对于背景为白色的点，即灰度值为255，采用空白字符来表示。<br>
    这样对于灰度图像的每一个像素点都有对应的字符表示，就得到了字符画。个人做了很多图像的字符画，总结了几个重要的注意点：1.增强灰度图像的对比度，即使得直方图尽量均匀分布（直方图均衡化）会产生较好的效果；2.尽量增强图像的边缘，即使得边缘和邻近区域的灰度值差别很大，可以利用一些梯度算子来实现；3.ascii码表要尽量选取一些对称性比较好的字符，比如'w','o','0','x'等等，美观。<br>
  * 视频转字符画 <br>
    为了将视频转为字符画视频，先利用ffmpeg工具将视频转换为gif图像，使用方式为：ffmpeg -i video_path -s m\*n -r framerate output.gif，video_path为视频位置，可以用video文件夹下的视频文件，m\*n为图像大小，framerate为每秒多少帧，output.gif是输出的gif文件，在gif目录下。<br>
    然后，利用skimage包逐个帧提取gif里面的图像，将之转换为字符画字符串，写入到html文件里面，在html目录下，然后就会生成以视频名为文件名的html文件，然后用浏览器打开即可。推荐使用chrome或edge浏览器，观看时如果效果不佳（字符太大，边缘不平滑），可以用'ctrl'+'-'缩小屏幕。
  
## 实例
  * [Bad Apple](https://www.bilibili.com/video/av706?from=search&seid=17055209907023401309) <br>
   本项目采用了一个比较简单的Bad Apple的视频，在Python3环境下，运行python bad_apple_ascii.py即可得到html/bad.html文件，然后用浏览器打开即可。如果需要尝试其余的视频，可以在video目录下放入需要处理的视频，然后修改bad_apple_ascii.py里面的视频路径配置，以及修改image2txt函数里面的相关代码（可以加入直方图均衡化、边缘增强等步骤），然后运行bad_apple_ascii.py即可。<br>
   <div align=center>
    <img src = "https://github.com/lxcnju/bad_apple_ascii/blob/master/bad_apple.gif"/>
  </div><br>
  
 
