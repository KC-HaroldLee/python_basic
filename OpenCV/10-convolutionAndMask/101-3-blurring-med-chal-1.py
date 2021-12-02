import cv2 as cv
import os

os.chdir('10-convolutionAndMask\\images')
img = cv.imread('noise.jpg')
img_blur = cv.medianBlur(img, 7) 

cv.imshow('origin', img)
cv.imshow('blur1', img_blur)

cv.waitKey(0)
cv.destroyAllWindows()