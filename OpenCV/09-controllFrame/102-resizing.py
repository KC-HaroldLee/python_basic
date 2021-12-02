import cv2 as cv
import os

# dst = cv.resize(src, dsize, [,dst[,fx[,fy,[interpolation]]]])

# src : 소스
# dst : 결과이미지
# dize : 결과이미지의 크기
# fx, fy : 수평, 수직 방향 크기 조정 비율(src 기준인듯하다)
# interpolation : 보간법

os.chdir('09-controllFrame\\images')
img_color = cv.imread('dal (2).jpg', cv.IMREAD_COLOR)
w,h = img_color.shape[:2]

# 방향크기 조정 비율(fx, fy)
img_result_with_f = cv.resize(img_color, None, 2, 2, cv.INTER_CUBIC)
# img_result = cv.resize(img_color, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow('img_result_with_f', img_result_with_f)

w,h = img_color.shape[:2]
# img_result_with_tuple = cv.resize(img_color, (int(w/2.0), int(h/2.0)), interpolation=cv.INTER_LINEAR)
img_result_with_tuple = cv.resize(img_color, (int(h/2.0), int(w/2.0)), interpolation=cv.INTER_LINEAR)
cv.imshow('img_result_with_tuple', img_result_with_tuple)


cv.waitKey(0)
cv.destroyAllWindows()