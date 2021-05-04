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
cv2.circle(shapes, (300, 200), 50, 64, -1)
cv2.imshow('shapes', shapes)

shape_candy = cv2.Canny(shapes, 20, 200)
cv2.imshow('shape_candy', shape_candy)
 
# 轮廓提取模式 Contour_Retrieval_Mode
shapes_contours, contours, hierarchy = cv2.findContours(shapes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(type(shapes_contours)); print(shapes_contours.shape )
print(type(contours)); print(len(contours)) 
print(type(hierarchy)); print(hierarchy.shape )
cv2.imshow('shapes_contours', shapes_contours)

#创建白色幕布
draw_contours = np.ones(shapes_contours.shape, np.uint8)*127
#画出轮廓：temp是白色幕布，contours是轮廓，-1表示全画，然后是颜色，厚度
# cv2.drawContours(draw_contours, contours, -1, 255, 3)
cv2.drawContours(draw_contours, contours, 0, 255, 2)
cv2.imshow('draw_contours', draw_contours)

polylines = np.ones(shapes.shape, np.uint8)
cv2.polylines(polylines, contours, True, 127, 1)
cv2.imshow('polylines', polylines)

cnt = contours[0]  # 第一个
M = cv2.moments(cnt)

# print(M)
print(M)  # 好看一点

# 根据 这些矩的值 我们可以 计算出对象的重心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print('重心:', cx, cy)

#
area = cv2.contourArea(cnt)
print('面积:', area)

# 第二参数可以用来指定对象的形状是闭合的 True   是打开的FALSE 一条曲线 。
perimeter = cv2.arcLength(cnt, True)
print('周长:', perimeter)
# 轮廓边界
x,y,w,h=cv2.boundingRect(cnt)
img=cv2.rectangle(draw_contours,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
