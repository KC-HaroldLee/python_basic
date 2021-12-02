import cv2 as cv
import os
import numpy as np
import sys

def trackbar_for_callback(x) :
    print('iterations : {0}'.format(cv.getTrackbarPos('iterations', 'output')))
    print('ksize : {0}'.format(cv.getTrackbarPos('ksize', 'output')))
    pass

cv.namedWindow('output')

a = cv.createTrackbar('iterations', 'output', 0, 5, trackbar_for_callback)
cv.setTrackbarPos('iterations', 'output', 5)

b = cv.createTrackbar('ksize', 'output', 3, 10, trackbar_for_callback)
cv.setTrackbarPos('ksize', 'output', 3)

os.chdir('11-Morphology\\images')

while(True) :
    img_gray = cv.imread('sb.jpg', cv.IMREAD_GRAYSCALE)
    ret, img_bin = cv.threshold(img_gray, 200,255, cv.THRESH_BINARY)
    img_bin_ivt = cv.bitwise_not(img_bin)
    iterationsV = cv.getTrackbarPos('iterations', 'output')
    ksizeV = cv.getTrackbarPos('ksize', 'output')
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (ksizeV, ksizeV)) #<class 'numpy.ndarray'>
    img_result = cv.erode(img_bin_ivt, kernel, iterations = iterationsV)

    cv.imshow('output', img_result)

    if cv.waitKey(1) & 0xFF==27:
        break

cv.destroyAllWindows()