#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np

circle=np.zeros((200, 300, 3), dtype=np.uint8)
rectangle=np.zeros((200, 300, 3), dtype=np.uint8)
# rectangle=np.zeros((200, 200, 3), dtype=np.uint8)

cv2.circle(circle, (100,100), 50, (255, 0, 0), -1)
cv2.rectangle(rectangle, (50,50), (100,100), (0, 0, 255), -1)
cv2.imshow('circle',circle)
cv2.imshow('rect',  rectangle)

circle_rect = circle +  rectangle
cv2.imshow('circle_rect',  circle_rect)

circle_rect_add = cv2.add(circle,  rectangle)
cv2.imshow('circle_rect_add',  circle_rect_add)

circle8_rect2 = cv2.addWeighted(circle, 0.75,  rectangle, 0.25, 0)
cv2.imshow('circle8_rect2',  circle8_rect2)

cv2.waitKey(0)
cv2.destroyAllWindows()
