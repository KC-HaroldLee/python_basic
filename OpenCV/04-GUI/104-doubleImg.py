# 2차 공부 예제는 03-IMAGE에 있음

import os
import cv2 as cv
import sys

os.chdir('04-GUI\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_COLOR)
img2 = cv.imread('gray-test.jpg', cv.IMREAD_COLOR)

# resultH = cv.hconcat([img1, img2])
# resultV = cv.vconcat([img1, img2])

# cv.imshow('hconcat' ,resultH)
# cv.imshow('vconcat' ,resultV)

cv.imshow('a', img1)
cv.imshow('b', img2)

cv.waitKey(0)
cv.destroyAllWindows()