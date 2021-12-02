import cv2 as cv
import numpy as np
from random import randint

width = 640
height = 480

img = np.zeros((height, width, 3), np.uint8)

img_h = img.shape[0] # shape에선 h가 먼저
img_w = img.shape[1] # shape에선 w가 나중
print('img-h={0}, img-w={1}'.format(img_h, img_w))

for y in range(img_h) :
    for x in range(img_w) :
        img.itemset(y,x,0,randint(0,255))
        img.itemset(y,x,1,randint(0,255))
        img.itemset(y,x,2,randint(0,255))

cv.imshow("ranColor", img)
cv.waitKey(0)

cv.destroyAllWindows()