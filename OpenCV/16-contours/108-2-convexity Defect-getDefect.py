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
# defects = cv.convexityDefects(contours[0], Hull) # 반복문으로 대체
for contour in contours : 
    defects = cv.convexityDefects(contour, Hull)
    print(type(defects)) # <class 'numpy.ndarray'>
    print(defects)
    # [[[    0   139    34 40414]]
    #  [[  140   142   141   154]]
    #  [[  142   289   227 33089]]
    # ...
    #  [[  604   606   605   142]]
    #  [[  606   610   607   114]]
    #  [[  610   764   703 38107]]]

cv.imshow('result', img_color)
cv.waitKey(0)