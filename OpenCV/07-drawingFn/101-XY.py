import cv2 as cv
import numpy as np

width = 400
height = 360

img = np.zeros((width, height, 3), np.uint8) # 튜플의 세번째는 채널

img_h = img.shape[0] # 높이
img_w = img.shape[1] # 너비
img_bpp = img.shape[2] # 채널 수

print(img_h, img_w, img_bpp)

cv.circle(img, (75, 100), 10, (0, 255, 255), -1)
cv.imshow('drawing', img)
cv.waitKey(0)