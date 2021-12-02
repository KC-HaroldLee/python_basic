import os
import cv2 as cv

os.chdir('06-imageCalc\\images')

logo = cv.imread('logo.png', cv.IMREAD_GRAYSCALE)
retval, logo_bin = cv.threshold(logo, 200,255, cv.THRESH_BINARY)

bgimg = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)

# 반전된 이진화 이미지
logo_bin_inv = cv.bitwise_not(logo_bin)


cv.imshow('logo_bin', logo_bin)
cv.imshow('logo_bin_inv', logo_bin_inv)
cv.waitKey(0)
