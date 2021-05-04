#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

im = cv2.imread('./resources/chessboard.jpeg')
cv2.imshow("im", im)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("imgray", imgray)

ret, thresh = cv2.threshold(src=imgray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("contours size: ", len(contours))

# image, contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print("contours size: ", len(contours))

# 整个画区域
# img = cv2.drawContours(im, contours, -1, (0,255,0), 2)
# cv2.imshow("im_draw", im)

# 分块画区域
for i in range(len(contours)):
    background = np.zeros(im.shape, dtype=np.uint8)
    background = cv2.drawContours(background, contours, i, (0, 255, 0), 2)
    cv2.imshow('background'+str(i), background)

cv2.waitKey(0)
cv2.destroyAllWindows()
