import cv2 as cv
import numpy as np
import os

# 이미지를 불러온다.

os.chdir('13-histogram\\images')
src = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)

# 컬러이미지를 BGR컬러로 분리한다.
bgr_planes = cv.split(src)

print(type(bgr_planes)) # <class 'list'> # 세개 로 나뉨
print(bgr_planes)