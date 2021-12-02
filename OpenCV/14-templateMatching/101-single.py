import cv2 as cv
import numpy as np
import os

os.chdir('14-templateMatching\\images')
img_rgb = cv.imread('test.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

# 템플릿 이미지를 불러온다.
img_template = cv.imread('template.jpg', cv.IMREAD_GRAYSCALE)
w, h = img_template.shape[:2]

# 매칭시작
res = cv.matchTemplate(img_gray, img_template, cv.TM_CCOEFF_NORMED)
# 0 - 대상, 1 - 템플릿, 2 - 옵션
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

# 검출된 템플릿 이미지와 유사한 영역에 사각형을 그려준다.
# 두 꼭지점을 구한다.
top_left = max_loc
bottom_right = (top_left[0]+w, top_left[1]+h)

# 사각형을 그린다.
cv.rectangle(img_rgb, top_left, bottom_right, (0,0,255), 2)

cv.imshow('img_rgb', img_rgb)
cv.waitKey(0)