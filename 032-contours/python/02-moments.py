#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

from pprint import pprint

img = cv2.imread('./resources/star.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('./resources/box.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('./resources/star.png', cv2.IMREAD_UNCHANGED)
# img = cv2.imread('./resources/box.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('img', img)

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

cnt = contours[0]  # 第一个
M = cv2.moments(cnt)
pprint(M)  # 好看一点
# 根据 这些矩的值 我们可以 计算出对象的重心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print('重心:', cx, cy)

#面积
area = cv2.contourArea(cnt)
print('面积:', area)

# 第二参数可以用来指定对象的形状是闭合的 True   是打开的FALSE 一条曲线 。
perimeter = cv2.arcLength(cnt, True)
print('周长:', perimeter)



cv2.waitKey(0)
cv2.destroyAllWindows()


