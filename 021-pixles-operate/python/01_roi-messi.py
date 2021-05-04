#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2

img = cv2.imread('./resources/messi.jpg')
cv2.imshow('origin', img)

print(img[280:340,330:390].shape)
print(img[273:333,100:160].shape)
ball=img[280:340,330:390]
img[273:333,100:160]=ball #修改像素值

cv2.namedWindow("messi", 0)
cv2.imshow("messi",img)
cv2.waitKey(0)

cv2.destroyAllWindows()

