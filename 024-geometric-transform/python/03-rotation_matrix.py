#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2 as cv

src = cv.imread('./resources/tiger.jpeg')
cv.imshow("src", src)

h, w, c = src.shape
M = np.zeros((2, 3), dtype=np.float32)
alpha = np.cos(np.pi / 4.0)
beta = np.sin(np.pi / 4.0)
# 初始旋转矩阵
cx = w / 2
cy = h / 2
tx = (1-alpha)*cx - beta*cy

ty = beta*cx + (1-alpha)*cy
M[0, 0] = alpha
M[0, 1] = beta
M[0,2] = tx
M[1, 0] = -beta
M[1, 1] = alpha
M[1,2] = ty
print(M)
# change with full size
bound_w = int(h * np.abs(beta) + w * np.abs(alpha))
bound_h = int(h * np.abs(alpha) + w * np.abs(beta))
# 添加中心位置迁移
M[0, 2] += bound_w / 2 - cx
M[1, 2] += bound_h / 2 - cy
print(M)

dst = cv.warpAffine(src, M, (bound_w, bound_h))
cv.imshow("dst", dst)


cv.waitKey(0)
cv.destroyAllWindows()
