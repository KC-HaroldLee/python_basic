import cv2 as cv
import os
import numpy as np

os.chdir('16-contours\\images')
img_color = cv.imread('hand.png', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img_color, contours, 0, (255, 0, 0), 3)  

Hull = cv.convexHull(contours[0])
print(type(Hull)) # <class 'numpy.ndarray'>
print(Hull)

cv.drawContours(img_color, [Hull], 0, (255,0,255), 2)

# Convexity Defect
Hull = cv.convexHull(contours[0], returnPoints=False)
print(type(Hull)) # <class 'numpy.ndarray'>
print(Hull)

# Convexity Defect를 구한다.
for contour in contours : 
    defects = cv.convexityDefects(contour, Hull)
    print(type(defects)) # <class 'numpy.ndarray'>

    print('.',defects.shape[0]) 
    for i in range(defects.shape[0]) :
        s,e,f,d = defects[i, 0]
        print('s : ', s, 'e : ', e , 'f: ', f ,'d : ', d)
            # s :  0 e :  139 f:  34 d :  40414
            # s :  140 e :  142 f:  141 d :  154
            # s :  142 e :  289 f:  227 d :  33089
            # ...
            # s :  604 e :  606 f:  605 d :  142
            # s :  606 e :  610 f:  607 d :  114
            # s :  610 e :  764 f:  703 d :  38107
        start = tuple(contour[s][0])
        end = start = tuple(contour[e][0])
        far = start = tuple(contour[f][0])

        # start와 end를 잇는 직선과 저 far의 거리가 10000이상 차이나는 경우에만 그림
        if d > 10000 :
            cv.line(img_color, start, end, (0,255,0), 3)
            cv.circle(img_color, far, 5, (0,0,255), -1)

cv.imshow('result', img_color)
cv.waitKey(0)