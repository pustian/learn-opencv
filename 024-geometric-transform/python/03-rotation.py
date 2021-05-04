# -*- coding: utf-8 -*-

# 旋转
import cv2
import numpy as np

img = cv2.imread('./resources/panad.jpg', 0)
rows, cols = img.shape[0:2]
cv2.imshow('img', img)

# 的第一个参数为旋转中心 第二个为旋转角度
#  第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
mat_rotation = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1)

# 第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img, mat_rotation, (cols, rows))

cv2.imshow('dst', dst)

cv2.waitKey(0)  # & 0xFF
cv2.destroyAllWindows()

