import cv2 as cv
import os

os.chdir('10-convolutionAndMask\\images')
img = cv.imread('texture.png')
img_blur = cv.bilateralFilter(img, 9, 75, 75) # 

cv.imshow('origin', img)
cv.imshow('blur1', img_blur)

cv.waitKey(0)
cv.destroyAllWindows()