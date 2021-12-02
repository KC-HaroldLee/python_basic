import os
import numpy as np
import cv2 as cv

os.chdir('a-paintMakingTool//images')

src = cv.imread('sample1.jpg', cv.IMREAD_COLOR)

def on_trackbar (x) :
    # print('트랙바 조정중')
    pass

# 조건문 달아서 flag 지정할 것
src_reduce = cv.imread('sample1.jpg', cv.IMREAD_REDUCED_COLOR_4)
src_reduce_gray = cv.imread('sample1.jpg', cv.IMREAD_REDUCED_GRAYSCALE_4)

# src_reduce = cv.imread('sample1.jpg', cv.IMREAD_COLOR)
# src_reduce_gray = cv.imread('sample1.jpg', cv.IMREAD_GRAYSCALE)

cv.namedWindow('before')
cv.namedWindow('line')
# cv.imshow('before', src_reduce)
cv.imshow('before', src_reduce)

cv.createTrackbar('d', 'before', 1, 100, on_trackbar)
cv.setTrackbarPos('d', 'before', 1)

cv.createTrackbar('sigmaColor', 'before', 0, 99, on_trackbar)
cv.setTrackbarPos('sigmaColor', 'before', 1)

cv.createTrackbar('sigmaSpace', 'before', 0, 99, on_trackbar)
cv.setTrackbarPos('sigmaSpace', 'before', 1)

cv.createTrackbar('borderType', 'before', 0, 5, on_trackbar)
cv.setTrackbarPos('borderType', 'before', 1)

cv.createTrackbar('threshold', 'before', 0, 254, on_trackbar)
cv.setTrackbarPos('threshold', 'before', 1)

cv.createTrackbar('canny1', 'line', 0, 254, on_trackbar)
cv.setTrackbarPos('canny1', 'line', 1)

cv.createTrackbar('canny2', 'line', 1, 255, on_trackbar)
cv.setTrackbarPos('canny2', 'line', 1)

# 키보드 콜백 필요

while(1) :
    thresh = cv.getTrackbarPos('threshold', 'before')
    bf_d = cv.getTrackbarPos('d', 'before')
    bf_sigmaColor = cv.getTrackbarPos('sigmaColor', 'before')
    bf_sigmaSpace = cv.getTrackbarPos('sigmaSpace', 'before')
    bf_borderType = cv.getTrackbarPos('borderType', 'before')
    canny1 = cv.getTrackbarPos('canny1', 'line')
    canny2 = cv.getTrackbarPos('canny2', 'line')
    
    key = cv.waitKey(1)
    if key == ord('q') :
        print('bf_d : {0}, sigmaColor : {1}, sigmaSpace : {2}, bf_borderType : {3}'.format(bf_d, bf_sigmaColor, bf_sigmaSpace, bf_borderType))
        img_blur = cv.bilateralFilter(src_reduce, bf_d, bf_sigmaColor, bf_sigmaSpace, bf_borderType)
        sharpen_filter= np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        img_sharped= cv.filter2D(img_blur, -1, sharpen_filter)
        cv.imshow('before', img_sharped)

        img_for_gray = cv.cvtColor(img_blur, cv.COLOR_BGR2GRAY)
        ret, img_canny = cv.threshold(img_for_gray, thresh, 255, cv.THRESH_BINARY)  
        img_canny = cv.Canny(img_for_gray, 0, 255)
        cv.imshow('line', img_canny)
        
    if key == ord('w') :
        img_canny = cv.Canny(img_for_gray, canny1, canny2)
        cv.imshow('line', img_canny)

        # retval, img_binary = cv.threshold(img_concath, thresh, 255, cv.THRESH_BINARY)
        # retval, src_reduce_gray_bin = cv.threshold(src_reduce_gray, thresh, 255, cv.THRESH_BINARY)
        # cv.imshow('before', src_reduce_gray_bin)
    
    # retval, src_reduce_bin = cv.threshold(src_reduce, thresh, 255, cv.THRESH_BINARY)
    # cv.imshow('before', src_reduce_bin)


cv.waitKey(0)