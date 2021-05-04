#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2

def on_change(x):
    print(x)

origin = cv2.imread('./resources/panad.jpg')
cv2.imshow('origin', origin)

print(origin.shape)

# 添加新窗口
cv2.namedWindow('win_threshold')
# 创建滑块,注册回调函数 lambda x: None没有滑动时
threshold_value = 127
cv2.createTrackbar('color', 'win_threshold', threshold_value, 255, on_change)

while (True):
    threshold_value = cv2.getTrackbarPos('color', 'win_threshold')
    ret, threshold_img = cv2.threshold(origin, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow('win_threshold', threshold_img)

    k = cv2.waitKey(1) & 0xFF
    if (k == 27) or (k == ord('q') ) :
        break

print(threshold_img.shape)

cv2.destroyAllWindows()

