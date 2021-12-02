import cv2 as cv
import os

os.chdir('10-convolutionAndMask\\images')
img = cv.imread('po.jpg')
# img_blur = cv.GaussianBlur(img, (50,50), 0) # 50은 안되네
img_blur = cv.GaussianBlur(img, (25,25), 0) # 

cv.imshow('origin', img)
cv.imshow('blur1', img_blur)

cv.waitKey(0)
cv.destroyAllWindows()