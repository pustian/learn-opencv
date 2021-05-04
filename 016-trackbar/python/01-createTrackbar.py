#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

def display(x):
    print(x)

img = cv2.imread('resources/panad.jpg')
# img = np.zeros((400,600, 3), np.uint8)
window_name='trackbar'
cv2.imshow(window_name, img)


cv2.createTrackbar('r', window_name, 0, 255, display)
cv2.createTrackbar('b', window_name, 0, 255, display)
cv2.createTrackbar('g', window_name, 0, 255, display)

while(True):
    if cv2.waitKey(1) & 0xFF == 27:
        break

    r = cv2.getTrackbarPos('r', window_name)
    g = cv2.getTrackbarPos('g', window_name)
    b = cv2.getTrackbarPos('b', window_name)
    # b = 127

    img[:] = [b, g, r] 
    cv2.imshow(window_name, img)

cv2.destroyWindow(window_name)
