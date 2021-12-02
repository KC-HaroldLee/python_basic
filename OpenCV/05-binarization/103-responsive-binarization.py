import os
import sys
import cv2 as cv

# 이미지를 읽어 온다.

os.chdir('05-binarization\\images')
img1 = cv.imread('shadow.jpg', cv.IMREAD_COLOR)

if img1 is None :
    print('이미지가 없음')
    sys.exit(1) 

img2 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

img_binary = cv.adaptiveThreshold(img2, 100,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 4)

cv.imshow('img1', img1)
cv.imshow('img2', img_binary)
cv.waitKey(0)
cv.destroyAllWindows()