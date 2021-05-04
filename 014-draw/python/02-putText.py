#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2

background = np.zeros((300, 400, 3), np.uint8)

# 图片对象，要写的内容，左下角坐标，字体，大小，颜色，粗细
cv2.putText(background, 'hello opencv', (0, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

cv2.imshow('putText', background)
cv2.waitKey(0)
cv2.destroyWindow('putText')
