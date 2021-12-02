import cv2 as cv
import os 

os.chdir('06-imageCalc\\images')

src = cv.imread('dal (1).jpg', cv.IMREAD_REDUCED_COLOR_2)
src_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

h, s, v = cv.split(src_hsv)
print(type(h)) # <class 'numpy.ndarray'>
print(type(s)) # <class 'numpy.ndarray'>
print(type(v)) # <class 'numpy.ndarray'>

cv.imshow('h', h)
cv.imshow('s', s)
cv.imshow('v', v)

cv.waitKey(0)

src_hsv_merged = cv.merge([h,s,v])
cv.imshow('src_hsv_merged', src_hsv_merged)

cv.waitKey(0)