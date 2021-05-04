#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(background, (x,y), 10, (255,0,0), 2)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(background, (x,y), (x+5, y+5), (0, 255,0), 3)

# 创建图像窗口并将窗口与回调函数绑定
background = np.zeros((400, 600, 3), np.uint8)
cv2.namedWindow('mouse event')
cv2.setMouseCallback('mouse event', draw_circle)

while(True):
    cv2.imshow('mouse event', background)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
