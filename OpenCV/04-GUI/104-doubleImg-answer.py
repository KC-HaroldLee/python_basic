# 2차 공부 예제는 03-IMAGE에 있음

import os
import cv2 as cv
import sys

os.chdir('04-GUI\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_COLOR)
img2 = cv.imread('mangpo-s.jpg', cv.COLOR_BGR2GRAY)

resultH = cv.hconcat([img1, img2])
resultV = cv.vconcat([img1, img2])

#  np를 배우면서 추가하는 코드

print(type(resultH)) # <class 'numpy.ndarray'>
print(type(resultV)) # <class 'numpy.ndarray'>

cv.imshow('hconcat' ,resultH)
cv.imshow('vconcat' ,resultV)

# cv.imshow('a', img1)
# cv.imshow('b', img2)

cv.waitKey(0)
cv.destroyAllWindows()