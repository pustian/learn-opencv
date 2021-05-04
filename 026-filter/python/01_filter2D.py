#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('./resources/opencv_logo.png')
kernel3 = np.ones((3, 3), np.float32) / 9
kernel4 = np.ones((4, 4), np.float32) / 16 
kernel5 = np.ones((5, 5), np.float32) / 25
# print(kernel)

# cv2.filter2D(src, avg, kernel3, anchor=(-1, -1))
avg3 = cv2.filter2D(src, -1, kernel3)
avg4 = cv2.filter2D(src, -1, kernel4)
avg5 = cv2.filter2D(src, -1, kernel5)

plt.subplot(2,2,1)
plt.imshow(src)
plt.xticks([]), plt.yticks([]), plt.title('origin')
plt.subplot(2,2,2)
plt.imshow(avg3)
plt.xticks([]), plt.yticks([]),plt.title('avg3')
plt.subplot(2,2,3)
plt.imshow(avg4)
plt.xticks([]), plt.yticks([]), plt.title('avg4')
plt.subplot(2,2,4)
plt.imshow(avg5)
plt.xticks([]), plt.yticks([]), plt.title('avg5')
plt.show()

