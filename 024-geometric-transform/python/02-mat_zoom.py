#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2

# img=cv2.imread('./resources/panad.jpg')
# print(img.shape)
img=cv2.imread('./resources/tiger.jpeg')
print(img.shape)
cv2.imshow('origin', img)

height, width =img.shape[:2]
mat_shift = np.float32([[0.5,0,0],[0, 0.5, 0]])
zoom_half = cv2.warpAffine(img, mat_shift, (width, height))
cv2.imshow('zoom_half', zoom_half)
print(zoom_half.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()
