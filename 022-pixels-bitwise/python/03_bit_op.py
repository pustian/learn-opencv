#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

circle=np.zeros((200, 300, 3), dtype=np.uint8)
rectangle=np.zeros((200, 300, 3), dtype=np.uint8)
# rectangle=np.zeros((200, 200, 3), dtype=np.uint8)

cv2.circle(circle, (100,100), 50, (255, 255, 0), -1)
cv2.rectangle(rectangle, (50,50), (100,100), (0, 255, 255), -1)
cv2.imshow('circle',circle)
cv2.imshow('rect',  rectangle)

# mask=np.zeros((200,300,3), dtype=np.uint8)
mask=np.full((200,300,3), 255, dtype=np.uint8)
cv2.imshow('mask',  mask)

# mask=np.zeros((200,300,3), dtype=np.uint8)
mask=np.full((200,300,3), 255, dtype=np.uint8)
cv2.bitwise_and(circle, rectangle, mask)
cv2.imshow('mask_bitwise_and',  mask)

mask_and=cv2.bitwise_and(circle, rectangle)
cv2.imshow('mask_and',  mask_and)

# mask=np.zeros((200,300,3), dtype=np.uint8)
mask=np.full((200,300,3), 255, dtype=np.uint8)
mask_or=cv2.bitwise_or(circle, rectangle)
cv2.imshow('mask_or',  mask_or)

circle_not=cv2.bitwise_not(circle)
cv2.imshow('circle_not',  circle_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
