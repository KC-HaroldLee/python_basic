import cv2 as cv
import numpy # 약자는 익숙한 다음 써야지
import os

os.chdir('03-image\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_COLOR)

sizeInfo = img1.shape[:2]
h, w = sizeInfo
print('h', h)
print('w', w)

img_gray = numpy.zeros((h,w), numpy.uint8) # blank

for y in range(0, h) :
    pass
    for x in range(0, w) :
        pass
        b = img1.item(y,x,0)
        g = img1.item(y,x,1)
        r = img1.item(y,x,2)

        # 평균값을 사용하는 경우
        grayValue = int(r+g+b/3.0)
 
        # BT.709?에 명시된 비율을 사용하는 경우
        # grayValue = int(r*0.2126 + g*0.7152 + b*0.0722)

        img_gray.itemset(y,x, grayValue)

print('복붙완료')

cv.imshow('gray-1', img_gray)
cv.waitKey(0)


img_result = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)
