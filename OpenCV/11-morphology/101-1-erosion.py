import cv2 as cv
import os
import numpy as np

os.chdir('11-Morphology\\images')
img_gray = cv.imread('i.png', cv.IMREAD_GRAYSCALE)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3)) #<class 'numpy.ndarray'>
img_result = cv.erode(img_gray, kernel, iterations = 10)

cv.imshow('input', img_gray)
cv.imshow('output', img_result)

cv.waitKey(0)
cv.destroyAllWindows()