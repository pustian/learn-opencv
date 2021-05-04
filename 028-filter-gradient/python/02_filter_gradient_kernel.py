#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./resources/sudoku.jpg')
# img = cv2.imread('./resources/car_card.jpg')
# x sobel
sobel_x_kernel = np.array([
        [-3,-10,-3],
        [0,0,0],
        [3,10,3]])
# y sobel
sobel_y_kernel = np.array([
        [-3,0,3],
        [-10,0,10],
        [-3,0,3]])
#拉普拉斯算子 laplacian operator
laplacian_kernel = np.array([
        [0,1,0],
        [1,-4,1],
        [0,1,0]])


laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx_8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
#卷积
sobel_x_img = cv2.filter2D(img,-1,sobel_x_kernel)
sobel_y_img = cv2.filter2D(img,-1,sobel_y_kernel)
laplacian_img = cv2.filter2D(img,-1,laplacian_kernel)


plt.subplot(4,2,1), plt.imshow(img), plt.title('origin'),
plt.xticks([]), plt.yticks([])
plt.subplot(4,2,2), plt.imshow(sobelx_8u), plt.title('sobelx_8u')
plt.xticks([]), plt.yticks([]),
plt.subplot(4,2,3), plt.imshow(sobelx), plt.title('sobelx')
plt.xticks([]), plt.yticks([]),
plt.subplot(4,2,4), plt.imshow(sobel_x_img), plt.title('sobel_x_img')
plt.xticks([]), plt.yticks([]),
plt.subplot(4,2,5), plt.imshow(sobely), plt.title('sobely')
plt.xticks([]), plt.yticks([]),
plt.subplot(4,2,6), plt.imshow(sobel_y_img), plt.title('sobel_y_img')
plt.xticks([]), plt.yticks([]),
plt.subplot(4,2,7), plt.imshow(laplacian), plt.title('laplacian')
plt.xticks([]), plt.yticks([]),
plt.subplot(4,2,8), plt.imshow(laplacian_img), plt.title('laplacian_img')
plt.xticks([]), plt.yticks([]),


plt.show()

