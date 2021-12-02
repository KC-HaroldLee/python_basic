import cv2 as cv
import os

os.chdir('16-contours\\images')
img_color = cv.imread('test.jpg', cv.IMREAD_COLOR)

# 그레이로 변환 후 바이너리로 변환(threshold : 문지방)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_bin1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

cv.imshow('img_bin1', img_bin1)
cv.waitKey(0)

# 이진화 결과를 개선 더 깔끔하게 한다.
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
img_bin2 = cv.morphologyEx(img_bin1, cv.MORPH_CLOSE, kernel)

cv.imshow('img_bin2', img_bin2)
cv.waitKey(0)

cv.destroyAllWindows()