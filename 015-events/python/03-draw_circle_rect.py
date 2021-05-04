#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

# 鼠标按下是转为true
drawing = False
# true 绘制矩形 键盘 m 控制
mode = True
ix, iy=-1, -1

def draw_circle_rect(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # 左键
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), 1)
            else:
                cv2.circle(img, (x,y), 3, (0,0,255), 1)
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False

# 创建图像窗口并将窗口与回调函数绑定
img = np.zeros((400, 600, 3), np.uint8)
cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', draw_circle_rect)

while(True):
    cv2.imshow('canvas', img)
    key = cv2.waitKey(10) & 0xFF 
    if key == ord('m'):
        mode = not mode
    if key == 27:
        break
    

cv2.destroyAllWindows()
