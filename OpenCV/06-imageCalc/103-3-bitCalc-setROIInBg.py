import os
import cv2 as cv

os.chdir('06-imageCalc\\images')

logo = cv.imread('logo.png', cv.IMREAD_GRAYSCALE)
retval, logo_bin = cv.threshold(logo, 200,255, cv.THRESH_BINARY)

bgimg = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)

# 반전된 이진화 이미지
logo_bin_inv = cv.bitwise_not(logo_bin)

# 이진화 이미지를 사용하여 잘라내는 과정
height, width = logo.shape[:2]

# 일단 사각형으로 지정
img_roi = bgimg[0:height, 0:width] # 0, 2은 offset

cv.imshow('img_roi', img_roi)
cv.waitKey(0)

cv.destroyAllWindows()