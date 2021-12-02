import cv2 as cv
import os

os.chdir('10-convolutionAndMask\\images')
img = cv.imread('po.jpg')
img_blur = cv.blur(img, (5,5))

cv.imshow('origin', img)
cv.imshow('blur1', img_blur)
cv.imshow('blur2', cv.blur(img, (5, 50)))
cv.imshow('blur2', cv.blur(img, (25, 25)))
cv.waitKey(0)
cv.destroyAllWindows()