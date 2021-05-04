#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('./resources/tiger.jpeg')

print(type(img))
print(img.shape)
cv2.imshow('img', img)

# pyplot.imgshow 在显示图片时是按照RGB通道顺序显示，cv2则相反
# 需要通过 np.flip(img,axis = 2) 调整3个通道的顺序（若不调整图片颜色失真）
plt.imshow(np.flip(img,axis = 2))
# plt.axis('off')
plt.show()                      #图1

plt.imshow(img)
# plt.axis('off')                 #不显示坐标
plt.show()                      #图2

cv2.waitKey(0)
cv2.destroyAllWindows()

