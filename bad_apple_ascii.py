#-*- coding:utf-8 -*-

# 将视频转为字符画视频
# 1、利用ffmpeg将视频转为gif图像
# 2、分割gif图像，得到逐帧图像
# 3、对每一幅图像生成字符画：先将RGB转为灰度图像，然后根据灰度等级选择相应的字符
# 4、将生成的字符写入到html中，利用javascript进行循环显示

import os
import sys
from PIL import Image
import matplotlib.pyplot as plt
from skimage import filters
import numpy as np
import random

from html_tools import config, Style, JavaScript
from load_ascii import load_ascii


colors = load_ascii('ascii.txt')      # 加载ascii码表当作像素点颜色
random.shuffle(colors)                # 随机排序

video_dir = "video"                   # 视频目录
video_name = "bad1.mp4"                # 视频文件名
realname = video_name.split('.')[0]   # 视频名称
gif_dir = "gif"                       # gif图像目录
html_dir = "html"                     # html文件目录位置

# 视频转gif图像
def video2gif():
    os.system('ffmpeg -i %s/%s -s %d*%d -r %d %s/%s.gif' % 
              (video_dir, video_name, config['width'], config['height'], config['frame'], gif_dir, realname))

# 图像转字符画
def image2txt(img):
    w, h = img.size
    h = int(h * config['ratio'])
    w = int(w * config['ratio'])
    image = img.convert('L').resize((w, h))          # 根据比例ratio进行缩放
        
    pix = image.load()                               # 像素点数组
    
    threshold = 127                                   # 阈值，由于bad_apple视频简单，可以通过简单阈值进行分割
    
	# 得到字符串
    pic_str = ''
    for i in range(h):
        for j in range(w):
		    # 如果是其余视频，则根据灰度级进行选择像素点，线性选择
			# index = int(pix[j, i] * 1.0 * (len(colors) - 1) / 255)
            # index = max(0, index)
			# index = min(index, 255)
            # pic_str += colors[index]
			
			# 这里bad_apple视频直接根据阈值进行划分即可
            if pix[j, i] <= threshold:
                pic_str += '*'
            else:
                pic_str += ' '
        pic_str += '\r\n'
    return '<pre>' + pic_str + '</pre>'

# 分割gif图像，逐个帧转字符画，加入到html中
def split_gif():
    img = Image.open("%s/%s.gif" % (gif_dir, realname))
    img.seek(1)
    
    Pre = ''                           # 要写入html文件的所有图像的字符画结果，字符串形式
    count = 0
    
    try:
        while True:
            Pre += image2txt(img)      # 添加结果
            if count % (config['frame'] * 10) == 0:
                print('%d S' % (count / config['frame']))
            count += 1
            img.seek(img.tell() + 1)
    except EOFError:
	    # gif图像处理结束，将结果写入html文件
        html_file = open('%s/%s.html' % (html_dir, realname), 'w', encoding = 'utf-8')
        html_file.write(
            '''<html>
            <head>
            %s
            %s
            </head>
            <body>
            <div class = "div-a">%s</div>
            <div class="div-b"><img src = "../%s/%s.gif" /></div> 
            </body>
            </html>
            ''' % (JavaScript, Style, Pre, gif_dir, realname)
        )
        html_file.close()

def main():
    video2gif()
    split_gif()

main()