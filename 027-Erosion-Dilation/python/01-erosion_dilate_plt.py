#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./resources/j.png')

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)


plt.subplot(221)
plt.imshow(img)
plt.title('origin')

plt.subplot(223)
plt.imshow(erosion)
plt.title('erosion')

plt.subplot(224)
plt.imshow(dilation)
plt.title('dilation')

plt.show()

