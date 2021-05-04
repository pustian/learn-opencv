#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

print(cv2.__version__)

img = cv2.imread('resources/panad.jpg')

cv2.imshow("panad", img)

cv2.waitKey(0)

cv2.destroyWindow("panad")
