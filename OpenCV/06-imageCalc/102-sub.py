import os
import cv2 as cv

os.chdir('06-imageCalc\\images')

img1 = cv.imread('sal (1).jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('sal (2).jpg', cv.IMREAD_GRAYSCALE)

# cv.imshow('img1', img1)
# cv.imshow('img2', img2)

img_sub1 = cv.subtract(img1, img2)
img_sub2 = cv.subtract(img2, img1)

ret1, img_sub_bin1 = cv.threshold(img_sub1, 50, 255, cv.THRESH_BINARY)
ret2, img_sub_bin2 = cv.threshold(img_sub2, 50, 255, cv.THRESH_BINARY)

# cv.imshow('img_sub1', img_sub1)
# cv.imshow('img_sub2', img_sub2)

cv.imshow('img_sub_bin1', img_sub_bin1)
cv.imshow('img_sub_bin2', img_sub_bin2)

cv.waitKey(0)