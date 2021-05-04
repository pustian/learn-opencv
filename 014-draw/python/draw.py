#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2

# 创建一个宽640高480的黑色画布，RGB(0,0,0)即黑色
img=np.zeros((480, 640, 3),np.uint8)

# 画直线,图片对象，起始坐标(x轴,y轴)，结束坐标，颜色，宽度
cv2.line(img,(0,0),(311,511),(255,0,0),10)
# 画矩形，图片对象，左上角坐标，右下角坐标，颜色，宽度
cv2.rectangle(img,(30,166),(130,266),(0,255,0),3)
# 画圆形，图片对象，中心点坐标，半径大小，颜色，宽度
cv2.circle(img,(222,222),50,(255.111,111),-1)
# 画椭圆形，图片对象，中心点坐标，长短轴，顺时针旋转度数，开始角度(右长轴表0度，上短轴表270度)，颜色，宽度
cv2.ellipse(img,(333,333),(50,20),0,0,150,(255,222,222),-1)

# 画多边形，指定各个点坐标,array必须是int32类型
pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2,))  # [][1][2] 数组转为
# 画多条线，False表不闭合，True表示闭合，闭合即多边形
cv2.polylines(img,[pts],True,(255,255,0),5)

#写字,字体选择
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
# 图片对象，要写的内容，左边距，字的底部到画布上端的距离，字体，大小，颜色，粗细
cv2.putText(img,"OpenCV",(10,400),font,3.5,(255,255,255),2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyWindow("img")
