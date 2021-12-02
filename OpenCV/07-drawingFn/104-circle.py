import cv2 as cv
import numpy as np

# img = cv.circle(img, center, radius, color, thickness)

# center : 중심좌표
# radius : 반지름

# 그냥 바로 해보자

img = np.zeros((800, 900, 3), np.uint8)

circle1 = cv.circle(img, (400,400), 50, (255, 0, 255), 3)
circle2 = cv.circle(img, (400,400), 200, (255, 0, 0), 5)

cv.imshow('img', img)
cv.waitKey(0)

cv.destroyAllWindows()