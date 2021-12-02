import cv2 as cv
import numpy as np

img = np.zeros((640, 640, 3), np.uint8)

r = (0, 0, 255)
g = (0, 255, 0)
y = (0, 255, 255)

thickness = 2

# 오각형 1
pts = np.array([[315,50],[570,240],[475,550],[150,550],[50,240]], np.int32)
pts = pts.reshape((-1,1,2)) #?
cv.polylines(img, [pts], False, r, thickness)

# 오각형 2
pts = np.array([[315,160],[150,280],[210,480],[420,480],[480,280]], np.int32)
pts = pts.reshape((-1,1,2)) #?
cv.polylines(img, [pts], True, g, thickness)

# 오각형 3
pts = np.array([[320,245],[410,315],[380,415],[265,415],[240,315]], np.int32)
pts = pts.reshape((-1,1,2)) #?
cv.fillPoly(img, [pts], y) # 이 경우 필요없는 인자가 생긴다.

cv.imshow('img', img)
cv.waitKey(0)

cv.destroyAllWindows()