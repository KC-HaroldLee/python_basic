import cv2 as cv
import numpy as np
import os

os.chdir('09-controllFrame\\images')
img_color = cv.imread('dal (2).jpg', cv.IMREAD_COLOR)

h, w = img_color.shape[:2]

# 이미지를 이동

M = np.float32([[1, 0, 100], [0, 1, 50]])

# 이동 행렬을 이미지에 적용합니다.

img_moved = cv.warpAffine(img_color, M, (w, h))

cv.imshow('img_moved', img_moved)
cv.waitKey(0)

cv.destroyAllWindows()