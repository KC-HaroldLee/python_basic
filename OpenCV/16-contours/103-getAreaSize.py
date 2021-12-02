import cv2 as cv
import os

os.chdir('16-contours\\images')
img_color = cv.imread('test.jpg', cv.IMREAD_COLOR)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_bin1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE ,(5,5))
img_bin2 = cv.morphologyEx(img_bin1, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(img_bin2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# for i in range(len(contours)) :
#     cv.drawContours(img_color, contours, i, (0,255,0), 2)

for i in range(len(contours)):
    cv.drawContours(img_color, contours, i, (0,255,0), 3)

for i, contour in enumerate(contours) :
    area = cv.contourArea(contour)

    print(i, '-', area)
    

cv.imshow('result', img_color)
cv.waitKey(0)

cv.destroyAllWindows()