#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
# img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)
img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("lena.jpg", cv2.IMREAD_UNCHANGED)

cv2.imshow("lena", img)
cv2.imwrite("lena_backup01.jpg", img, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
cv2.imwrite("lena_backup02.jpg", img, [int( cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("lena_backup.tiff", img, [int( cv2.IMWRITE_JPEG_QUALITY), 5])   # 无效

cv2.waitKey(0)
cv2.destroyAllWindows()
