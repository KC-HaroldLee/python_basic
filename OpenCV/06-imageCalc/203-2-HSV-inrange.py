import cv2 as cv
import os 

os.chdir('06-imageCalc\\images')

# src = cv.imread('dal (1).jpg', cv.IMREAD_REDUCED_COLOR_2)
src = cv.imread('tomato.jpg', cv.IMREAD_REDUCED_COLOR_2)
src_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

h, s, v = cv.split(src_hsv)
h_red = cv.inRange(h, 8, 20)
print(type(h_red)) # <class 'numpy.ndarray'>

dst_hsv = cv.bitwise_and(src_hsv,src_hsv, mask = h_red)
dst_bgr = cv.cvtColor(dst_hsv, cv.COLOR_HSV2BGR)

cv.imshow('dst_bgr', dst_bgr)

cv.waitKey(0)