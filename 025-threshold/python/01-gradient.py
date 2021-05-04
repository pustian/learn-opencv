#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('./resources/gradient.png')
img = cv2.imread('./resources/gray-gradient.jpg')

ret, threshold_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, threshold_2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, threshold_3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, threshold_4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, threshold_5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles=['origin', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images=[img, threshold_1, threshold_2, threshold_3, threshold_4, threshold_5]

for i in xrange(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
