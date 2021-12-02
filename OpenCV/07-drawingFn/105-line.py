import cv2 as cv
import numpy as np

# cv.line(img, pt1, pt2, color[, thickness])

img = np.zeros((500,500,3), np.uint8)

line1 = cv.line(img, (200, 230), (500, 400), (255, 0, 255))


line2 = cv.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 0, 255), 3)

cv.imshow('img', img)
cv.waitKey(0)
