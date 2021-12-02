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
 
# 히스토그램을 보여줄 이미지를 생성한다.
hist_w = 256*3
hist_h = 400
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8) # 음? 직접 만들어?

# 히스토그램을 정규화(?)한다.
b_norm = cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist, g_hist, 0, hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist, r_hist, 0, hist_h, norm_type=cv.NORM_MINMAX)

print(type(b_norm)) # <class 'numpy.ndarray'>

notEqual = []
for i in range(256) :
    print(i, ': ', 'b_hist: ', b_hist[i],'\t', 'b_norm', b_norm[i]) # 모두 같음
    if  b_hist[i] != b_norm[i] :
        notEqual.append(i)
print('notEqual',notEqual)