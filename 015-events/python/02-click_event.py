#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    red = img[y, x, 2]
    blue = img[y, x, 0]
    green = img[y, x, 1]
    strRGB = str(x) + "," + str(y) + "," + str(red) + "," + str(green) + "," + str(blue)

    if event == cv2.EVENT_LBUTTONDOWN:
        print(strRGB)
    if event == cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, strRGB, (x, y), font, 1, (255, 255, 255), 2)
        cv2.imshow('original', img)

img = cv2.imread('./resources/panad.jpg')
cv2.imshow('original', img)

cv2.setMouseCallback("original", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
