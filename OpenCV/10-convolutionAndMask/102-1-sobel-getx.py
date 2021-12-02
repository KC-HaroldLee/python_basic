import cv2 as cv
import os

os.chdir('10-convolutionAndMask\\images')
img_color = cv.imread('po.jpg')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

img_sobel_x1 = cv.Sobel(img_gray, cv.CV_64F, 1, 0, ksize=3)
img_sobel_x2 = cv.convertScaleAbs(img_sobel_x1)

cv.imshow('x1', img_sobel_x1)
cv.imshow('x2', img_sobel_x2)

cv.waitKey(0)
cv.destroyAllWindows()