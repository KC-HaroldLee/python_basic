import cv2 as cv
import numpy as np


# img = cv.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness[, thickness])

# axes : 메인 축 방향의 반지름
# startAngle : 호의 시작 각도
# endAngle : 호의 끝 각도

img = np.zeros((500, 500, 3), np.uint8)

center = (int(img.shape[0]/2), int(img.shape[1]/2)) # 센타

print(center, type(center))

cv.ellipse(img, center, (50,200), 0, 0, 270, (250, 100, 255), 2)
cv.ellipse(img, center, (75,225), 45, 0, 270, (0, 100, 255), 2)
cv.ellipse(img, center, (100,250), 90, 0, 270, (0, 0, 255), 2)


cv.imshow('img', img)
cv.waitKey(0)

cv.destroyAllWindows()