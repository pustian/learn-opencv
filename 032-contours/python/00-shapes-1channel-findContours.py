#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2

shapes=np.zeros((300, 400, 1), dtype=np.uint8)

cv2.rectangle(shapes, (100, 100), (200, 200), 255, -1)
cv2.rectangle(shapes, (125, 125), (200, 200), 192, -1)
cv2.rectangle(shapes, (150, 150), (200, 200), 128, -1)
cv2.rectangle(shapes, (175, 175), (200, 200), 64, -1)

cv2.circle(shapes, (300, 100), 40, 192, -1)
cv2.circle(shapes, (300, 200), 50, 192, -1)
cv2.imshow('shapes', shapes)

shape_candy = cv2.Canny(shapes, 20, 200)
cv2.imshow('shape_candy', shape_candy)
 
#轮廓提取模式 Contour_Retrieval_Mode
shapes_contours, contours, hierarchy = cv2.findContours(shapes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(type(shapes_contours)); print(shapes_contours.shape )
print(type(contours)); print(len(contours)) 
print(type(hierarchy)); print(hierarchy.shape )
cv2.imshow('shapes_contours', shapes_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
