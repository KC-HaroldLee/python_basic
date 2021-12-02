# edges = cv.Canny(image, thershold1, thershold2, [,edges [, aperureSize [,L2gradient]]])

# image : 그레이 스케일 입력 이미지
# thershold1 : 첫번째 임계값
# thershold2 : 두번째 입계값
# aperureSize : 소벨 연산에서 사용할 마스크 크기

import cv2 as cv
import os



os.chdir('10-convolutionAndMask\\images')
img_color = cv.imread('car.jpg', cv.IMREAD_COLOR)
cv.imshow('not canny', img_color)
cv.waitKey(0)

img_gray = cv.imread('car.jpg', cv.IMREAD_GRAYSCALE)
img_canny = cv.Canny(img_gray, 150, 175)

cv.imshow('cannyEdge', img_canny)
cv.waitKey(0)
cv.destroyAllWindows()