#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('./resources/sudoku.jpg')
rows, cols, ch = img.shape
print(img.shape)

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300, 300))
# dst = cv2.warpPerspective(img, M, (rows, cols))

pts1_pluylines=np.array([[56, 65], [368, 52], [28, 387], [389, 390]], np.int32)
pts= pts1_pluylines.reshape((-1,1,2,))  #[3][2] --> [3][1][2]
cv2.polylines(img, [pts], True, (0,255,255), 3)

pts2_pluylines=np.array([[0, 0], [300, 0], [0, 300], [300, 300]], np.int32)
pts= pts2_pluylines.reshape((-1,1,2,))  #[3][2] --> [3][1][2]
cv2.polylines(dst, [pts], True, (0,255, 0), 3)

cv2.imshow('img', img);
cv2.imshow('dst', dst);


# src = cv2.imread('./resources/tiger.jpeg')
# src_transform = cv2.warpPerspective(src, M, (300, 300))
# cv2.imshow('src', src);
# cv2.imshow('src_transform', src_transform);
# print(src.size)
# print(src_transform.size)

cv2.waitKey(0)
cv2.destroyAllWindows()
