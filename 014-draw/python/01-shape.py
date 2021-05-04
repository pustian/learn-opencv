#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2

# 画直线,图片对象，起始坐标(x轴,y轴)，结束坐标，颜色，宽度
# 创建一个高300宽400的黑色画布，RGB(0,0,0)即黑色
line_background=np.zeros((300, 400, 3), np.uint8)

cv2.line(line_background, (20,10), (100,50), (255,0,0), 1)

start_point = (20, 10)
end_point = (20, 40)
bgr_color = (255, 255, 0)
line_width = 2
cv2.line(line_background, start_point, end_point, bgr_color, line_width)

cv2.imshow('line', line_background)
# 用完即关
# cv2.waitKey(0)
# cv2.destroyWindow('line')

# 画矩形，图片对象，左上角坐标，右下角坐标，颜色，宽度
rect_background=np.zeros((300, 400, 3), np.uint8)
cv2.rectangle(rect_background, (30,166), (130,266), (0,255,0), 3)

left_top_point = (20, 20)
right_buttom_point = (50, 60)
bgr_color = (0, 255, 255)
line_width = 2
cv2.rectangle(rect_background, right_buttom_point, left_top_point, bgr_color, line_width)
cv2.imshow('rectangle', rect_background)
# cv2.waitKey(0)
# cv2.destroyWindow('rectangle')

# 画圆形，图片对象，中心点坐标，半径大小，颜色，宽度
circle_background=np.zeros((300, 400, 3), np.uint8)
cv2.circle(circle_background, (100, 100), 50, (0, 0, 255), 1)

center_point=(50,50)
radius=40
bgr_color=(255, 0, 255)
line_width=-1
cv2.circle(circle_background, center_point, radius, bgr_color, line_width)
cv2.imshow('circle', circle_background)
# cv2.waitKey(0)
# cv2.destroyWindow('circle')

# 画椭圆形，图片对象，中心点坐标，长短轴，顺时针旋转度数，开始角度(右长轴表0度，上短轴表270度)，颜色，宽度
ellipse_background=np.zeros((300, 400, 3), np.uint8)
cv2.ellipse(ellipse_background, (100, 100), (50, 20), 0, 0, 180, (255,222,222), 1)
centerCoordinates = (200, 200)
# 椭圆的长轴和短轴(长轴长度，短轴长度)
axesLength=(80, 30)
angle=90
startAngle=180
endAngle=270
bgr_color=(0, 255, 255)
line_width=-1
cv2.ellipse(ellipse_background, centerCoordinates, axesLength, angle, startAngle, endAngle, bgr_color, line_width)

cv2.imshow('ellipse', ellipse_background)
# cv2.waitKey(0)
# cv2.destroyWindow('ellipse')

# 画多边形，指定各个点坐标,array必须是int32类型
polylines_background=np.zeros((300, 400, 3), np.uint8)
# pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts=np.array([10,5,200,300,70,200,50,100], np.int32)
pts = pts.reshape((-1,1,2,))  # [][1][2] 数组转为 [[][][][][]]
# 画多条线，False表不闭合，True表示闭合，闭合即多边形
cv2.polylines(polylines_background, [pts], False, (255,255,0), 2)
cv2.imshow('polylines', polylines_background)
# cv2.waitKey(0)
# cv2.destroyWindow('polylines')

cv2.waitKey(0)
cv2.destroyAllWindows()
