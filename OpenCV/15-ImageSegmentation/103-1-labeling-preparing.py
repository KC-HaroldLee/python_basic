import cv2 as cv
import os

os.chdir('15-Image segmentation\\images')
img_color = cv.imread("test.jpg", cv.IMREAD_COLOR)

# 그레이 스케일
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY) 
cv.imshow("result", img_gray )
cv.waitKey(0)

# 에지 추출
img_edge = cv.Canny(img_gray, 50, 150)
cv.imshow("result", img_edge )
cv.waitKey(0)

# 인버트(?)
img_edge = cv.bitwise_not(img_edge)
cv.imshow("result", img_edge )
cv.waitKey(0) 
