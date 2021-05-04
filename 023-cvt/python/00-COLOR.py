#!/usr/bin/env python

import cv2

colors_const = [ i for i in dir(cv2) if 'COLOR_' in i ]

print colors_const
