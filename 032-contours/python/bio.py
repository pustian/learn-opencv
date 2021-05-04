#!/usr/bin/env python
#-*-  coding:utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('./resources/3.tif', cv2.IMREAD_GRAYSCALE)


candy = cv2.Canny(img, 20, 200)
cv2.imshow('candy', candy)
 
#轮廓提取模式 Contour_Retrieval_Mode cv2.CHAIN_APPROX_NONE  全部点 cv2.CHAIN_APPROX_SIMPLE 拟合线
img_contours, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(type(img_contours)); print(img_contours.shape )
print(type(contours)); print(len(contours)) 
print(type(hierarchy)); print(hierarchy.shape )
cv2.imshow('img_contours', img_contours)

# #画出轮廓：temp是白色幕布，contours是轮廓，-1表示全画，然后是颜色，厚度
# draw_contours = np.ones(img_contours.shape, np.uint8)*255
# cv2.drawContours(draw_contours, contours, 23, 64, 1)
# cv2.imshow('draw_contours23',  draw_contours)
print(cv2.contourArea(contours[23]) )

contours2=[cnt for cnt in contours if cv2.contourArea(cnt)>10.0]#过滤太小的contour
print('过滤太小的contour', len(contours2))
for i in range(len(contours2) ) :
    draw_contours = np.ones((img_contours.shape[0], img_contours.shape[1],3), np.uint8)
    cv2.drawContours(draw_contours, contours, i, (0,0,255), -1) 
    cv2.imshow("draw_contours"+str(i),  draw_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()

