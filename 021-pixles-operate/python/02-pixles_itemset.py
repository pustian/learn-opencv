#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import os


# ------ x col
# |
# |y row
def access_pixles(image):
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    # print("width : %s, height : %s, channel : %s" % (width, height, channel) )
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    # cv2.imshow("修改后", image)

def fill_pixles(image):
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    # print("width : %s, height : %s, channel : %s" % (width, height, channel) )
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                if pv > 250:
                    image[row, col, c] = 255
                else:
                    image[row, col, c] = 0
                    

filepath='./resources/tiger.jpeg'
# filepath='./resources/panad.jpg'
# filepath='./resources/1.tif'

img=cv2.imread(filepath)
print(img.shape)
print(img.size)
print(img.dtype)
print(img[10,10])
print(img.item(10,10, 1))
img.itemset((10,10,1), 190)
print(img.item(10,10, 1))
img.itemset((10,10,1), 290) # 290-256
print(img.item(10,10, 1))


# reverse=img.copy()
# access_pixles(reverse)
# cv2.imshow('reverse', reverse)
# 
# fill=img.copy()
# fill_pixles(fill)
# cv2.imshow('fill', fill)
cv2.waitKey(0)
cv2.destroyAllWindows()
