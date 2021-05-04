#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2

img=cv2.imread('./resources/panad.jpg')
print(img.shape)
cv2.imshow('origin', img)

shift_mat=np.float32([[1, 0, -100],[0, 1, -200]])
shift = cv2.warpAffine(img, shift_mat, img.shape[0:2])
cv2.imshow('shift', shift)


cv2.waitKey(0)
cv2.destroyAllWindows()
