#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2

img = cv2.imread('./resources/panad.jpg')
cv2.imshow('origin', img)

# img[y1:y2, x1:x2]
head=img[340:460,150:280]
img[100:220,0:130]=head #修改像素值
cv2.namedWindow("head", 0)
cv2.imshow("head",head)

print(img.shape)
rows, cols, channel = img.shape
img[0:rows, 0:cols, 0] = 0
img[0:rows, 0:cols, 2] = 0

cv2.namedWindow("panad", 0)
cv2.imshow("panad", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

