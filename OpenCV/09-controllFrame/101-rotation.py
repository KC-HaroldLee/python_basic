import cv2 as cv
import os

os.chdir('09-controllFrame\\images')
img_color = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)

cv.imshow('img_color', img_color)

h,w = img_color.shape[:2]

# 회전하는 '행렬'을 만든다
M = cv.getRotationMatrix2D((w/2.0,h/2.0),45,1)
# 0 - 회전 중심점, 1 - 각도(음수는 cw/양수는 acw), 2 - 이미지 배율
print(type(M)) # <class 'numpy.ndarray'>

# 그리고 만든 회전행렬을 이미지에 붙인다.
img_rotated = cv.warpAffine(img_color, M, (h, w))

cv.imshow('img_rotated', img_rotated)

# img_rotated_extended = cv.warpAffine(img_color, M, (int(h*1.5), int(w*1.5)))
# cv.imshow('img_rotated_extended', img_rotated_extended)

cv.waitKey(0)

cv.destroyAllWindows()