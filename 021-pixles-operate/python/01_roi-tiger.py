#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2

img = cv2.imread('./resources/tiger.jpeg')
cv2.imshow('origin', img)

# img[y1:y2, x1:x2]
head=img[90:250,310:490]
img[20:180,30:210]=head #修改像素值

cv2.namedWindow("tiger", 0)
cv2.imshow("tiger",img)

cv2.namedWindow("head", 0)
cv2.imshow("head",head)

cv2.waitKey(0)

cv2.destroyAllWindows()

