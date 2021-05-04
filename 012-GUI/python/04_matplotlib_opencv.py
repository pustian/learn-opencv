#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('resources/tiger.jpeg')  # img1为BGR
cv2.imshow('image', img1)   # 图1
cv2.waitKey(0)

img2 = plt.imread('resources/tiger.jpeg')  # img2为RGB
plt.imshow(img2)            # 图2
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

img_new = np.zeros(img1.shape)
img_new[:,:,0] = img1[:,:,2]
img_new[:,:,1] = img1[:,:,1]
img_new[:,:,2] = img1[:,:,0]  # 将img1转为RGB模式img_new
img_new = img_new.astype(np.uint8) # 将默认的flost64改为uint8
plt.imshow(img_new)  # 此时img_new和img2一样，和图2结果一样
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

plt.imshow(img1) # 利用plt显示opencv读取的图片，则不会正确显示。
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

