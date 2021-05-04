import cv2
import numpy as np


img = cv2.imread('./resources/3.tif', cv2.IMREAD_GRAYSCALE)

# threshold
# img=cv2.GaussianBlur(gray,(3,3),0)
edges = cv2.Canny(img, 200, 250)

print(img.shape)
print(edges.shape)

cv2.imshow('img', img)
cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
