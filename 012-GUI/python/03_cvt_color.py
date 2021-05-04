#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import cv2, sys

if len(sys.argv) < 2:
    print('show_image.py image_path. eg: ./03_cvt_color.py resources/tiger.jpeg')
    sys.exit(0)

image_path = sys.argv[1]
try:
    f = open(image_path)
except Exception as e:
    print(e)
    sys.exit(-1)

img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # 包括图像的 alpha 通道
display = img.copy()

# title = image_path.split('/')[-1] + f'{img.shape}'
title = image_path.split('/')[-1]
gray=False

while(True):
    cv2.imshow(title, display)

    k = cv2.waitKey(0)
    print(k)
    
    if k == ord('g') or k == ord('G'):
        if gray == False:
            display = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
            gray = True
        else:
            display = img.copy()
#            display = cv2.cvtColor(display, cv2.COLOR_GRAY2BGR)
            gray = False
    
    if k == ord('q') or k == ord('Q') or k == 27:
        break

cv2.destroyWindow(title)

