import os
import cv2 as cv
import sys

os.chdir('05-binarization\\images')
img1 = cv.imread('gr.jpg', cv.IMREAD_COLOR)
img2 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
ret,img3 = cv.threshold(img1, 127,255, cv.THRESH_BINARY)
ret,img4 = cv.threshold(img2, 127,255, cv.THRESH_BINARY)


cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)
cv.imshow('img4', img4)

cv.waitKey(0)
cv.destroyAllWindows()