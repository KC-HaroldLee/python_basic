import cv2 as cv
import numpy as np
import os

os.chdir('13-histogram\\images')
src = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)

bgr_planes = cv.split(src)
histSize = 256
histRange = (0,255)
accumulate = False

b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv.calcHist(bgr_planes, [1], None, [256], (0,255), accumulate=False)
r_hist = cv.calcHist(bgr_planes, [2], None, [256], (0,255), accumulate=False)
 
hist_w = 256*3
hist_h = 400
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist, g_hist, 0, hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist, r_hist, 0, hist_h, norm_type=cv.NORM_MINMAX)

for i in range(0, histSize) :
    #b
    cv.line(histImage, ( i, hist_h - int(np.round(b_hist[i])) ),
            ( i, hist_h - 0 ), ( 255, 0, 0), thickness=2)

    #g
    cv.line(histImage, ( i + 256, hist_h - int(np.round(g_hist[i-1])) ),
            ( i + 256, hist_h - 0 ), ( 0, 255, 0), thickness=2)

    #r
    cv.line(histImage, ( i + 256 * 2, hist_h - int(np.round(r_hist[i-1])) ),
            ( i + 256 *2, hist_h - 0 ), ( 0, 0, 255), thickness=2)

cv.imshow('Source image', src)
cv.imshow('Histogram', histImage)
cv.waitKey()