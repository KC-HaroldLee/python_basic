import cv2 as cv
import os

# dst = cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# 지원하는 알고리즘
cv.ADAPTIVE_THRESH_GAUSSIAN_C # 가우시안
cv.ADAPTIVE_THRESH_MEAN_C # 평균값

os.chdir('05-binarization\\images')
src = cv.imread('mangpo.jpg', cv.IMREAD_REDUCED_GRAYSCALE_8)

def trackbarCallback (x) :
    pass

cv.namedWindow('result')
cv.createTrackbar('maxValue', 'result', 0, 255, trackbarCallback)
# cv.createTrackbar('blockSizeValue', 'result', 2, 50, trackbarCallback)
cv.createTrackbar('C', 'result', -5, 5, trackbarCallback)

adaptiveMethodList = [cv.ADAPTIVE_THRESH_MEAN_C, cv.ADAPTIVE_THRESH_GAUSSIAN_C]
thresholdTypeList = [cv.THRESH_BINARY, cv.THRESH_BINARY_INV, cv.THRESH_TRUNC, cv.THRESH_TOZERO, cv.THRESH_TOZERO_INV]
# idx1 = 0
# idx2 = 0

while True :

    key = cv.waitKey(33)
    if key == ord('q') :
        break

    maxValue = cv.getTrackbarPos('maxValue', 'result')
    blockSizeValue = cv.getTrackbarPos('blockSizeValue', 'result')
    CValue = cv.getTrackbarPos('C', 'result')

    src_adtBin = cv.adaptiveThreshold(src, maxValue, adaptiveMethodList[0], thresholdTypeList[0], 33, CValue)

    cv.imshow('result', src_adtBin)

