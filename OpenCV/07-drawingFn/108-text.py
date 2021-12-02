import numpy as np
import cv2 as cv

img = np.zeros((640,800,3), np.uint8)

r = (0, 0, 255)
g = (0, 255, 0)
y = (0, 255, 255)
w = (255, 255, 255)

center_x = int(img.shape[0]/2.0)
center_y = int(img.shape[1]/2.0)

thickness = 2

location = (center_x - 200, center_y - 50)
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
fontScale = 3.5
cv.putText(img, 'NIRVANA', location, font, fontScale, y, thickness)

# location[1] = location[1] + 100 아쉽다.
location = (center_x - 200, center_y - 150)
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 2.0
cv.putText(img, 'KURT', location, font, fontScale, r, thickness)

cv.imshow('text', img)
cv.waitKey(0)

cv.destroyAllWindows()