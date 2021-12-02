import os
import cv2 as cv

os.chdir('03-image\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_GRAYSCALE)
print(type(img1)) # <class 'numpy.ndarray'>

img_sub1 = img1[400:400+400, 200:200+400]
print(type(img_sub1)) # <class 'numpy.ndarray'>

print(img_sub1.base is img1) 
print('id가 같은가?', bool(id(img1)==id(img_sub1))) # False

ret, img_sub1 = cv.threshold(img_sub1, 127, 255, cv.THRESH_BINARY) 
cv.imshow('img1', img1)
cv.imshow('img_sub1', img_sub1)

cv.waitKey(0)
