#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./resources/drawing.png')
rows, cols, ch = img.shape
print(img.shape)

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

pts1_pluylines=np.array([[50, 50], [200, 50], [50, 200]], np.int32)
pts= pts1_pluylines.reshape((-1,1,2,))  #[3][2] --> [3][1][2]
cv2.polylines(img, [pts], True, (0,255,255), 3)

pts2_pluylines=np.array([[10, 100], [200, 50], [100, 250]], np.int32)
pts= pts2_pluylines.reshape((-1,1,2,))  #[3][2] --> [3][1][2]
cv2.polylines(dst, [pts], True, (0,255,255), 3)

cv2.imshow('img', img);
cv2.imshow('dst', dst);

src = cv2.imread('./resources/tiger.jpeg')
shift_mat=np.float32([[1, 0, -50],[0, 1, -50]])
shift = cv2.warpAffine(src, shift_mat, src.shape[0:2])
src_transform = cv2.warpAffine(shift, M, src.shape[:2])
cv2.imshow('src', src);
cv2.imshow('src_transform', src_transform);
print(src.size)
print(src_transform.size)

cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.subplot(121, plt.imshow(img), plt.title('Input'))
# plt.subplot(122, plt.imshow(dst), plt.title('Output'))

# plt.figure(figsize=(8, 7), dpi=98)
# p1 = plt.subplot(211)
# p1.show(img)
# p1.set_title('Input')
# 
# p2 = plt.subplot(212)
# p2.show(dst)
# p2.set_title('Output')
# 
# plt.show()

