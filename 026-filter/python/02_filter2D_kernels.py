#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./resources/opencv_logo.png')
# image = cv2.imread('./resources/car_card.jpg')
#自定义
kernel_sharpen_1 = np.array([
        [-1,-1,-1],
        [-1,9,-1],
        [-1,-1,-1]])
kernel_sharpen_2 = np.array([
        [1,1,1],
        [1,-7,1],
        [1,1,1]])
kernel_sharpen_3 = np.array([
        [-1,-1,-1,-1,-1],
        [-1,2,2,2,-1],
        [-1,2,8,2,-1],
        [-1,2,2,2,-1], 
        [-1,-1,-1,-1,-1]])/8.0
#图像锐化 sharpen
kernel_sharpen_4 = np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]])
#图像模糊 blur
kernel_sharpen_5 = np.array([
        [0.0625,0.125,0.0625],
        [0.125,0.25,0.125],
        [0.0625,0.125,0.125]])
#索贝尔 buttom sobel
kernel_sharpen_6 = np.array([
        [-1,-2,-1],
        [0,0,0],
        [1,2,1]])
# x sobel
kernel_sharpen_6 = np.array([
        [-3,-10,-3],
        [0,0,0],
        [3,10,3]])
# y sobel
kernel_sharpen_6 = np.array([
        [-3,0,3],
        [-10,0,10],
        [-3,0,3]])
#浮雕 emboss
kernel_sharpen_7 = np.array([
        [-2,-1,0],
        [-1,1,1],
        [0,1,2]])
#大纲 outline
kernel_sharpen_8 = np.array([
        [-1,-1,-1],
        [-1,8,-1],
        [-1,-1,-1]])
#拉普拉斯算子 laplacian operator
kernel_sharpen_9 = np.array([
        [0,1,0],
        [1,-4,1],
        [0,1,0]])


#卷积
# output_1 = cv2.filter2D(image,-1,kernel_sharpen_1)
output_2 = cv2.filter2D(image,-1,kernel_sharpen_2)
output_3 = cv2.filter2D(image,-1,kernel_sharpen_3)
output_4 = cv2.filter2D(image,-1,kernel_sharpen_4)
output_5 = cv2.filter2D(image,-1,kernel_sharpen_5)
output_6 = cv2.filter2D(image,-1,kernel_sharpen_6)
output_7 = cv2.filter2D(image,-1,kernel_sharpen_7)
output_8 = cv2.filter2D(image,-1,kernel_sharpen_8)
output_9 = cv2.filter2D(image,-1,kernel_sharpen_9)

plt.subplot(3,3,1)
plt.imshow(image)
plt.xticks([]), plt.yticks([]),
plt.title('origin')
plt.subplot(3,3,2)
plt.imshow(output_2)
plt.xticks([]), plt.yticks([]),
plt.title('define_2')
plt.subplot(3,3,3)
plt.imshow(output_3)
plt.xticks([]), plt.yticks([]),
plt.title('define_3')

plt.subplot(3,3,4)
plt.imshow(output_4)
plt.xticks([]), plt.yticks([]),
plt.title('sharpen')
plt.subplot(3,3,5)
plt.imshow(output_5)
plt.xticks([]), plt.yticks([]),
plt.title('blur')
plt.subplot(3,3,6)
plt.imshow(output_6)
plt.xticks([]), plt.yticks([]),
plt.title('sobel')

plt.subplot(3,3,7)
plt.imshow(output_7)
plt.xticks([]), plt.yticks([]),
plt.title('emboss')
plt.subplot(3,3,8)
plt.imshow(output_8)
plt.xticks([]), plt.yticks([]),
plt.title('outline')
plt.subplot(3,3,9)
plt.imshow(output_9)
plt.xticks([]), plt.yticks([]),
plt.title('laplacian op')
plt.show()

