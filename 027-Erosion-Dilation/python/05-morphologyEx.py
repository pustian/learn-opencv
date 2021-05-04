#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./resources/j.png')
# print(img.shape)

kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# 开 先腐蚀再膨胀
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 闭 先膨胀再腐蚀
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 礼帽
# 原始图像与  开运算之后得到的图像的差。
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽  进行闭运算之后得到的图像与原始图像的差
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(321), plt.imshow(img), plt.title('origin')
plt.xticks([]), plt.yticks([])

plt.subplot(322), plt.imshow(gradient), plt.title('gradient')
plt.xticks([]), plt.yticks([])

plt.subplot(323), plt.imshow(opening), plt.title('opening')
plt.xticks([]), plt.yticks([])
plt.subplot(324), plt.imshow(tophat), plt.title('tophat')
plt.xticks([]), plt.yticks([])

plt.subplot(325), plt.imshow(closing), plt.title('closing')
plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(blackhat), plt.title('blackhat')
plt.xticks([]), plt.yticks([])

plt.show()

cv2.destroyAllWindows()
