#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

print(cv2.__version__)

img = cv2.imread('resources/panad.jpg')

cv2.imwrite("panad_backup.png", img)
