import cv2 as cv
import os

os.chdir('16-contours\\images')
img_color = cv.imread('test.jpg', cv.IMREAD_COLOR)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_bin1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
img_bin2 = cv.morphologyEx(img_bin1, cv.MORPH_CLOSE, kernel)

# 컨투어를 검출한다.
contours, hierarchy = cv.findContours(img_bin2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# cv.drawContours(img_color, contours, 0, (0,0,255), 3)
# cv.drawContours(img_color, contours, 1, (0,255,0), 3)
# cv.drawContours(img_color, contours, 2, (255,0,0), 3)

for i in range(len(contours)):
    if i == len(contours)-1 : 
        break
    cv.drawContours(img_color, contours, i, (0,255,0), 3)

cv.imshow('result', img_color)
cv.waitKey(0)

cv.destroyAllWindows()