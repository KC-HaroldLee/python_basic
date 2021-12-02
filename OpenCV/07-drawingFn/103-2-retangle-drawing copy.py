import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# ~에, 시작, 끝, 색, 굵
cv.rectangle(img, (50, 50), (450, 450), (0,0,255), 3)
cv.rectangle(img, (150, 200), (250, 300), (0, 255, 0), -1)

# ~에, (시작, 범위), 색, 굵
cv. rectangle(img, (350,150,  50,100), (255, 0, 255), -1)

cv.imshow('img', img)
cv.waitKey(0)

cv.destroyAllWindows()