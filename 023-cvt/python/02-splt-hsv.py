#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

pic_file = './resources/tiger.jpeg'

# img_bgr = cv2.imread(pic_file, cv2.IMREAD_COLOR) #OpenCV读取颜色顺序：BRG 
img_bgr = cv2.imread(pic_file, cv2.IMREAD_UNCHANGED) #OpenCV读取颜色顺序：BRG 
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_h = img_hsv[..., 0]
img_s = img_hsv[..., 1]
img_v = img_hsv[..., 2]
fig = plt.gcf()                                  #图片详细信息

fig = plt.gcf()                                  #分通道显示图片
fig.set_size_inches(10, 15)

plt.subplot(221)
plt.imshow(np.flip(img_hsv, axis=2))             #展平图像数组并显示
plt.axis('off')
plt.title('HSV')

plt.subplot(222)
plt.imshow(img_v, cmap='gray')
plt.axis('off')
plt.title('H')

plt.subplot(223)
plt.imshow(img_s, cmap='gray')
plt.axis('off')
plt.title('S')

plt.subplot(224)
plt.imshow(img_h, cmap='gray')
plt.axis('off')
plt.title('V')

plt.show()
