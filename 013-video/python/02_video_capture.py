#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2
import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # 一般的笔 本电脑 有内置摄像头。所以参数就是 0。你可以  设置成 1 或 者其他的来 择别的摄像头
while cap.isOpened():  # 检查是否成功初始化，否则就 使用函数 cap.open()
    # Capture frame-by-frame
    ret, frame = cap.read()  # ret 返回一个布尔值 True/False
    # print('frame shape:',frame.shape)#(720, 1280, 3)
    cv2.imshow('camera', frame)
    key = cv2.waitKey(delay=10)
    if key == ord("q"):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

