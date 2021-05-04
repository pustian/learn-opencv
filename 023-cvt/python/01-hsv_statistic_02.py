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

def calc_and_draw_hist(image, color):  
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])  
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)  
    hpt = int(0.9* 256);  
      
    for h in range(256):  
        intensity = int(hist[h]*hpt/maxVal)  
        cv2.line(histImg,(h,256), (h,256-intensity), color)  
    return histImg


if __name__ == '__main__':  
    img = cv2.imread("./resources/tiger.jpeg")
#    img = cv2.resize(original_img,None,fx=0.6,fy=0.6,interpolation = cv2.INTER_CUBIC)
    b, g, r = cv2.split(img)  
  
    hist_img_B = calc_and_draw_hist(b, [255, 0, 0])  
    hist_img_G = calc_and_draw_hist(g, [0, 255, 0])  
    hist_img_R = calc_and_draw_hist(r, [0, 0, 255])  

    cv2.imshow("hist_img_B", hist_img_B)  
    cv2.imshow("hist_img_G", hist_img_G)  
    cv2.imshow("hist_img_R", hist_img_R)  
    cv2.imshow("Img", img)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows() 
