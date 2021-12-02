import cv2 as cv
import numpy # 약자는 익숙한 다음 써야지
import os

os.chdir('03-image\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_COLOR)

print(type(cv.split(img1))) # <class 'list'>

b,g,r = cv.split(img1)

image_result = cv.merge ((r,g,b))

cv.imshow('merged', image_result)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)

cv.waitKey(0)
cv.destroyAllWindows()