#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
自适应阈值

Adaptive Method- 指定 算阈值的方法。
– cv2.ADPTIVE_THRESH_MEAN_C  值取自相邻区域的平均值
– cv2.ADPTIVE_THRESH_GAUSSIAN_C  值取值相邻区域 的加权和 ，权重为一个高斯窗口
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./resources/sudoku.jpg', 0)
cv2.imshow('img', img);

rows, cols=img.shape[:2]
# 中值滤波
img_mdeidan = cv2.medianBlur(img, 5)
cv2.imshow('img_mdeidan', img_mdeidan);
# 左侧统一 + 50
img_half = img.copy()
img_half[0:cols,0:rows/2] = img_half[0:cols, 0:rows/2] + 99 
cv2.imshow('img_half', img_half);

imgs = [img, img_mdeidan, img_half]
for i in xrange(3):
    ret, th1 = cv2.threshold(imgs[i], 127, 255, cv2.THRESH_BINARY)
    # 11 为 Block size 邻域大小 用来计算阈值的区域大小 ,
    # 2 为 C值，常数， 阈值就等于的平均值或者加权平均值减去这个常数。
    th2 = cv2.adaptiveThreshold(imgs[i], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(imgs[i], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [imgs[i], th1, th2, th3]

    for j in range(4):
        plt.subplot(2, 2, j + 1), 
        plt.imshow(images[j], 'gray')
        plt.title(titles[j])
        plt.xticks([]), plt.yticks([])
    
    plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
