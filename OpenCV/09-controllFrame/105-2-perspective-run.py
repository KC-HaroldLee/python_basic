import cv2 as cv
import os
import numpy as np
import sys

src = np.zeros([4, 2], np.float32)
idx = 0

def mouse_callback(event, x, y, flags, param) :
    global point_list, idx, src # point_list? 왜?

    if event == cv.EVENT_LBUTTONDOWN :
        print('클릭 감지(down)')

        src[idx] = (x, y) # 튜플이지만 알아서 ndarray에 들어가나? (간다)
        idx = idx + 1
        print ('추가된 포인트 {0}, {1}'.format(x, y))
        print('idx', idx)
        print('src', src)
        cv.circle(img_color, (x, y), 10, (0,0,255), -1)

# 콜백 함수 설정
cv.namedWindow('original')
cv.setMouseCallback('original', mouse_callback)

# 이미지 불러오기
os.chdir('09-controllFrame\\images')
img_color = cv.imread('station.png', cv.IMREAD_COLOR)
img_origin = img_color.copy()

# 반복
while (True) :

    cv.imshow('original', img_color)
    h, w = img_color.shape[:2]

    if cv.waitKey(1) == 32 :
        break

# 사각영역 지정(그러니까 프레임은 원본하고 같네?)
dst = np.float32([[0,0],[w,0],[0,h],[w,h]])

# 퍼스펙티브 변환행렬 지정
M = cv.getPerspectiveTransform(src, dst)

# 이미지에 M 적용
img_result = cv.warpPerspective(img_origin, M, (w,h))

# 쇼
cv.imshow('result', img_result)
cv.waitKey(0)
cv.destroyAllWindows()