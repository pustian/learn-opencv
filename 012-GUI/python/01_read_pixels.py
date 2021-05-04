#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

def access_pixles(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    print("width : %s, height : %s, channel : %s" % (width, height, channel))
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    # cv2.imshow("修改后", image)


print(cv2.__version__)

img = cv2.imread('resources/panad.jpg')

cv2.imshow("origin", img)

print(img.shape)

access_pixles(img)

cv2.imshow("reverse", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
