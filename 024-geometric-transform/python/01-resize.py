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
zoom_half = cv2.resize(img, (width/2, height/2 ) , interpolation=cv2.INTER_AREA)
cv2.imshow('zoom_half', zoom_half)
print(zoom_half.shape)

zoom_12= cv2.resize(img, (int(width*1.2), int(height*1.2) ), interpolation=cv2.INTER_CUBIC )
cv2.imshow('zoom_12', zoom_12)
print(zoom_12.shape)

zoom_twice = cv2.resize(img, (width*2, height*2 ), interpolation=cv2.INTER_LINEAR)
cv2.imshow('zoom_twice', zoom_twice)
print(zoom_twice.shape)

zoom_x_2_y_4 =cv2.resize(img, (0, 0), fx=0.5, fy=0.25, interpolation=cv2.INTER_NEAREST)
cv2.imshow('zoom_x_2_y_4', zoom_x_2_y_4)
print(zoom_x_2_y_4.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
