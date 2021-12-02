import cv2 as cv
import os

os.chdir('10-convolutionAndMask\\images')
img_color = cv.imread('po.jpg')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

img_sobel_x1 = cv.Sobel(img_gray, cv.CV_64F, 1, 0, ksize=3)
img_sobel_x2 = cv.convertScaleAbs(img_sobel_x1)

img_sobel_y1 = cv.Sobel(img_gray, cv.CV_64F, 0, 1, ksize=3)
img_sobel_y2 = cv.convertScaleAbs(img_sobel_y1)

img_sobel_result = cv.addWeighted(img_sobel_x2, 1, img_sobel_y2, 1, 0)

cv.imshow('result', img_sobel_result)
cv.waitKey(0)
cv.destroyAllWindows()