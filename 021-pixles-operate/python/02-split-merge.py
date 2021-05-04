#!/usr/bin/env python
#-*- coding:utf-8 -*-


import cv2

img = cv2.imread('./resources/tiger.jpeg')
cv2.imshow('origin', img)
b,g,r=cv2.split(img)
print(b.shape)
print(b.dtype)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
# img2=cv2.merge(b, g)
# cv2.imshow('merged', img2)


# #
# b=img[:,:,0]
# #使所有像素的红色通道值都为 0,你不必先拆分再赋值。
# # 你可以 直接使用 Numpy 索引,这会更快。
# img[:,:,2]=0




cv2.waitKey(0)

cv2.destroyAllWindows()
