import cv2 as cv
import os

os.chdir('15-Image segmentation\\images')
img_gray = cv.imread('gradation.png', cv.IMREAD_GRAYSCALE)

# 임계값을 127로 해서 이진화.
ret, img_bin = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

cv.imshow("grayscale", img_gray)
cv.imshow("bin", img_bin)

cv.waitKey(0)
cv.destroyAllWindows()