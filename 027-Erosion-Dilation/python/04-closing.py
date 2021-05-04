#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./resources/j.png')
print(img.shape)
cv2.imshow('origin',img)

kernel = np.ones((5, 5), np.uint8)
# 闭运算：先膨胀再腐蚀就叫做闭运算。 除燥音
closing1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('origin1',img)
cv2.imshow('closing1', closing1)

img= cv2.dilate(img, kernel, iterations=1)
closing2= cv2.erode(img, kernel, iterations=1)
cv2.imshow('origin-dilation', img)
cv2.imshow('closing|origin-dilation-erosion', closing2)
cv2.waitKey(0)

plt.subplot(221), plt.imshow(img), plt.title('origin')
plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(closing1), plt.title('closing1')
plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(closing2), plt.title('closing2')
plt.xticks([]), plt.yticks([])

plt.show()

cv2.destroyAllWindows()
