import cv2 as cv
import numpy as np
import os

os.chdir('13-histogram\\images')
src = cv.imread('dal (1).jpg', cv.IMREAD_GRAYSCALE)

# bgr_planes = cv.split(src)
histSize = 256
histRange = (0,255)
accumulate = False

# b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
# g_hist = cv.calcHist(bgr_planes, [1], None, [256], (0,255), accumulate=False)
# r_hist = cv.calcHist(bgr_planes, [2], None, [256], (0,255), accumulate=False)
gray_hist = cv.calcHist([src], [0], None,[histSize], histRange, accumulate=accumulate)

# hist_w = 256*3
hist_w = 256
hist_h = 400
# histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
histImage = np.zeros((hist_h, hist_w, 1), dtype=np.uint8)

# cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
# cv.normalize(g_hist, g_hist, 0, hist_h, norm_type=cv.NORM_MINMAX)
# cv.normalize(r_hist, r_hist, 0, hist_h, norm_type=cv.NORM_MINMAX)
cv. normalize(gray_hist, gray_hist, 0 ,hist_h, norm_type=cv.NORM_MINMAX)

for i in range(0, histSize) :
    #b
    cv.line(histImage, ( i, hist_h - int(np.round(gray_hist[i])) ),
            ( i, hist_h - 0 ), ( 255, 0, 0), thickness=2)
            
cv.imshow('Source image', src)
cv.imshow('Histogram', histImage)
cv.waitKey()