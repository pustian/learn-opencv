#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./resources/j.png')
print(img.shape)
cv2.imshow('origin',img)

kernel = np.ones((5, 5), np.uint8)
# 开运算：先腐蚀再膨胀就叫做开运算。 除燥音
opening1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('origin1',img)
cv2.imshow('opening1', opening1)

img= cv2.erode(img, kernel, iterations=1)
opening2 = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('origin-erosion', img)
cv2.imshow('opening|origin-erosion-dilation', opening2)
cv2.waitKey(0)

plt.subplot(221)
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.title('origin')

plt.subplot(223)
plt.imshow(opening1)
plt.xticks([]), plt.yticks([])
plt.title('opening1')

plt.subplot(224)
plt.imshow(opening2)
plt.xticks([]), plt.yticks([])
plt.title('opening2')

plt.show()

cv2.destroyAllWindows()
