import cv2 as cv
import numpy # 약자는 익숙한 다음 써야지
import os

os.chdir('03-image\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_COLOR)

sizeInfo = img1.shape[:2]
print(sizeInfo) # (1008, 567)
print(type(sizeInfo)) # <class 'tuple'>

# 튜플은 나눠야 제맛...
h, w = sizeInfo
print('h', h)
print('w', w)

# 회전 모두 적용해준다. 자바보다 편한 부분이긴하다.