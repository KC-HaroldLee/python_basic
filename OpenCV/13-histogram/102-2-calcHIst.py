import cv2 as cv
import numpy as np
import os

os.chdir('13-histogram\\images')
src = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)

bgr_planes = cv.split(src)

# 픽셀범위는 0~255 이므로 256개
histSize = 256

# 위에 맞춰서 범위
histRange = (0,255)

# 처음시작시 히스토그램이 비어있도록(하지만 명시적으로 한 번 적는다.)
accumulate = False

# b,g,r별로 히스토그램을 만든다.
# hist = cv.calcHist(images, channels, mask, histSize, ranges[,hist[,accumulate]])

# image : unit8 또는 float32 타입의 이미지
# channels : 히스토그램계산할 채널의 인덱스
# mask : 마스크 이미지, 전체를 한다면 Mat()이나 None을 사용한다.
# hitSize : 막대의 개수
# ranges : 히스토그램을 범위

b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv.calcHist(bgr_planes, [1], None, [256], (0,255), accumulate=False)
r_hist = cv.calcHist(bgr_planes, [2], None, [256], (0,255), accumulate=False)
 
print(type(b_hist)) # <class 'numpy.ndarray'>
print('b_hist = \n', b_hist)
print('g_hist = \n', g_hist)
print('r_hist = \n', r_hist)
