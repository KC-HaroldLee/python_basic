import os
import cv2 as cv

os.chdir('06-imageCalc\\images')

logo = cv.imread('logo.png', cv.IMREAD_GRAYSCALE)
retval, logo_bin = cv.threshold(logo, 200,255, cv.THRESH_BINARY)

cv.imshow('logo_bin', logo_bin)
cv.waitKey(0)
