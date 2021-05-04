#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2

shapes=np.zeros((300, 400, 3), dtype=np.uint8)

# cv2.rectangle(shapes, (175, 175), (200, 200), (255, 255, 255), -1)
cv2.rectangle(shapes, (100, 100), (200, 200), (255, 0, 0), -1)
cv2.rectangle(shapes, (125, 125), (200, 200), (0, 255, 0), -1)
cv2.rectangle(shapes, (150, 150), (200, 200), (0, 0, 255), -1)

# cv2.circle(shapes, (300, 200), 70, (255, 255, 255), -1)
cv2.circle(shapes, (300, 200), 50, (0, 255, 255), -1)
cv2.circle(shapes, (300, 200), 30, (255, 255, 0), -1)
cv2.circle(shapes, (300, 200), 10, (255, 0, 255), -1)

cv2.imshow('shapes', shapes)

# 灰度图
shapes_gray = cv2.cvtColor(shapes.copy(), cv2.COLOR_BGR2GRAY)
cv2.imshow('shapes_gray', shapes_gray)

shape_candy = cv2.Canny(shapes_gray, 20, 300)
cv2.imshow('shape_candy', shape_candy)

#轮廓提取模式 Contour_Retrieval_Mode
shapes_contours, contours, hierarchy = cv2.findContours(shapes_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(type(shapes_contours)); print(shapes_contours.shape )
print(type(contours)); print(len(contours)) 
print(type(hierarchy)); print(hierarchy.shape )
cv2.imshow('shapes_contours', shapes_contours)

#创建白色幕布
temp = np.ones(shapes_contours.shape, np.uint8)*255
#画出轮廓：temp是白色幕布，contours是轮廓，-1表示全画，然后是颜色，厚度
cv2.drawContours(temp, contours, -1, (0,255,0), 3)

temp2 = np.ones(shapes.shape, np.uint8)
cv2.polylines(temp2, contours, True, (255,255,0), 1)

cv2.imshow('contours', temp)
cv2.imshow('contours2', temp2)

cv2.waitKey(0)
cv2.destroyAllWindows()
