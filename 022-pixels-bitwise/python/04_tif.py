#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('./resources/1.tif', cv2.IMREAD_UNCHANGED)
cv2.imshow('origin', img)
print(img.shape)

mask = np.zeros(img.shape, np.uint8)
print(mask.shape)
rect = np.zeros(img.shape, np.uint8)
# cv2.imshow('mask', mask)

cv2.rectangle(rect, (200, 0), (236,30), 254, -1)
cv2.imshow('rect', rect)

bitwise_and_img = cv2.bitwise_and(img, rect, mask)
cv2.imshow('bitwise_and_img', bitwise_and_img)

bitwise_or_img = cv2.bitwise_or(img, rect, mask)
cv2.imshow('bitwise_or_img', bitwise_or_img)

img = cv2.bitwise_and(img, rect, mask)
cv2.imshow('img', img)


cv2.waitKey(0)

cv2.destroyAllWindows()

