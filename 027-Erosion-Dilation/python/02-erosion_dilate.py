#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./resources/j.png')
print(img.shape)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('origin',img)
cv2.imshow('erosion', erosion)
cv2.moveWindow('erosion', x=img.shape[1], y=0)
cv2.imshow('dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
