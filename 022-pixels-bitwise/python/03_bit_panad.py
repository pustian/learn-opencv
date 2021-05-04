#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2

img = cv2.imread('./resources/panad.jpg')
cv2.imshow('origin', img)

img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
cv2.waitKey(0)

cv2.destroyAllWindows()

