import os
import cv2 as cv

os.chdir('06-imageCalc\\images')

logo = cv.imread('logo.png', cv.IMREAD_COLOR)
logo_gray = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
retval2, logo_bin = cv.threshold(logo_gray, 200,255, cv.THRESH_BINARY)
logo_bin_inv = cv.bitwise_not(logo_bin)


bgimg = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)
height, width = logo.shape[:2]
print(logo.shape)

img_roi = bgimg[0:height, 0:width] # 0, 2은 offset

# 이진화 이미지를 사용하여 로고이미지에서는 배경을 지우고
# 배경 이미지에는 로고가 들어갈 위치를 제거한다.
img1 = cv.bitwise_and(logo, logo, mask = logo_bin_inv)
img2 = cv.bitwise_and(img_roi, img_roi, mask = logo_bin)

# cv.imshow('img1', img1)
# cv.imshow('img2', img2)

dst = cv.add(img1, img2)
bgimg[0:height, 0:width] = dst

print(type(bgimg), type(dst)) # <class 'numpy.ndarray'> <class 'numpy.ndarray'>
 
cv.namedWindow('bgimg')
cv.imshow('bgimg', bgimg)

cv.waitKey(0)
cv.destroyAllWindows()