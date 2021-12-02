import cv2 as cv
import math
import os
import numpy as np

os.chdir('12-houghTransform\\images')
img_src = cv.imread('railroad.jpg', cv.IMREAD_GRAYSCALE)
img_edge = cv.Canny(img_src, 50, 150)
img_result =cv.cvtColor(img_edge, cv.COLOR_GRAY2BGR)

cv.imshow('img_src', img_src)
cv.imshow('img_edge', img_edge)
cv.imshow('img_result', img_result)

cv.waitKey(0)

cv.destroyAllWindows()