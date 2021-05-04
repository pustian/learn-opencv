#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture('resources/Minions_banana.mp4')

# 帧率
fps = cap.get(cv2.CAP_PROP_FPS)  # 25.0
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
# 总共有多少帧
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('total frames {0}'.format(num_frames) )

frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('height={0}  width={1}'.format(frame_height, frame_width) )

FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 第0帧
print('current frame = {0}'.format(FRAME_NOW ) )  # 当前帧数 0.0

# 读取指定帧,对视频文件才有效，对摄像头无效？？
frame_no = num_frames/2 
cap.set(1, frame_no)  # Where frame_no is the frame you want
ret, frame = cap.read()  # Read the frame
cv2.imshow('frame_no'+str(frame_no), frame)

cv2.waitKey(0)
FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 第0帧
print('current frame = {0}'.format(FRAME_NOW ) )  # 当前帧数 0.0

while cap.isOpened():
    ret, frame = cap.read()
    FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 当前帧数
    print('当前帧数', FRAME_NOW)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

