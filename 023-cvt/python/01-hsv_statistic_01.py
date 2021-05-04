#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
hist = cv2.calcHist([image],             # 传入图像（列表）
                    [0],                 # 使用的通道（使用通道：可选[0],[1],[2]）
                    None,                # 没有使用mask(蒙版)
                    [256],               # HistSize
                    [0.0,255.0])         # 直方图柱的范围
                                         # return->list
"""

import cv2    
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':  
    img_bgr = cv2.imread("./resources/tiger.jpeg")
#    img = cv2.resize(original_img,None,fx=0.6,fy=0.6,interpolation = cv2.INTER_CUBIC)
    
    # 按R、G、B三个通道分别计算颜色直方图
    b_hist = cv2.calcHist([img_bgr], [0], None, [256], [0, 256])
    g_hist = cv2.calcHist([img_bgr], [1], None, [256], [0, 256])
    r_hist = cv2.calcHist([img_bgr], [2], None, [256], [0, 256])

    # 显示3个通道的颜色直方图
    plt.plot(b_hist, label='B', color='blue')
    plt.plot(g_hist, label='G', color='green')
    plt.plot(r_hist, label='R', color='red')
    plt.legend(loc='best')
    plt.xlim([0, 256])
    plt.show()
    
