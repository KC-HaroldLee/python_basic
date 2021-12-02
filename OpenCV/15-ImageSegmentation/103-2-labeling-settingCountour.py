import cv2 as cv
import os

os.chdir('15-Image segmentation\\images')
img_color = cv.imread("test.jpg", cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY) 
img_edge = cv.Canny(img_gray, 50, 150)
img_edge = cv.bitwise_not(img_edge)
cv.imshow("result", img_edge )
cv.waitKey(0) 

# 컨투어(윤곽)설정
contours = cv.findContours(img_edge.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# 0-이미지, 1-모드, 2-메소드 ...
cv.drawContours(img_edge, contours[0], -1, (0, 0, 0), 1)
# 0-이미지, 1-컨투어s, 2-컨투어s 인덱스, 3-색상, 4-굵기 ...
cv.imshow("result", img_edge )
cv.waitKey(0) 
