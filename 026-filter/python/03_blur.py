#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('./resources/opencv_logo.png')
img = cv2.imread('./resources/car_card.jpg')
img = cv2.imread('./resources/gray-gradient.jpg')

blur = cv2.blur(img, (5, 5))
# cv2.filter2D(img, -1, blur_kernel)

gaussian = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯模糊

median = cv2.medianBlur(img, 5)  # 中值模糊

bilateral = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur), plt.title('blur')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(gaussian), plt.title('gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(bilateral), plt.title('bilateral')
plt.xticks([]), plt.yticks([])
plt.show()



