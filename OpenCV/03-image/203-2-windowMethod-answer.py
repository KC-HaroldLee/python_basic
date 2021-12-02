import os
import cv2 as cv

os.chdir('03-image\\images')
# src = cv.imread("OpenCV_Logo.png", cv.IMREAD_GRAYSCALE)
src = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)

cv.namedWindow("src", flags=cv.WINDOW_FREERATIO)
cv.resizeWindow("src", 400, 200)
cv.imshow("src", src)
cv.waitKey(0)
cv.destroyWindow("src")