import os
import cv2 as cv
import numpy as np

os.chdir('16-contours\\images')
img_color = cv.imread('test.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, 
                        cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img_color, contours, 0, (0,0,255), 2)
cv.drawContours(img_color, contours, 1, (0,255,0), 2)

for contour in contours :
    # 물체 회전을 고려하지 않은
    x,y, w,h = cv.boundingRect(contour)
    print(type(cv.boundingRect(contour))) # <class 'tuple'>
    print(cv.boundingRect(contour)) # (66, 102, 276, 357)
    print('x: ',x, 'y : ', y, 'w : ',w, 'h : ', h) # x:  66 y :  102 w :  276 h :  357
    cv.rectangle(img_color, (x,y), (x+w,y+h), (255,255,0), 2)

    # 물체의 회전을 고려함 
    rect = cv.minAreaRect(contour)
    print(type(rect)) # <class 'tuple'>
    print(rect)
     # ((160.07183837890625, 293.6353759765625), (410.744384765625, 117.58914947509766), 48.012786865234375)

    box = cv.boxPoints(rect)
    print('box1 : ',box)
    # [[-21.016571 180.31491 ]
    #  [ 66.38675  101.65193 ]
    #  [341.16025  406.95584 ]
    #  [253.75693  485.61884 ]]

    box = np.int0(box)
    # [[-21 180]
    #  [ 66 101]
    #  [341 406]
    #  [253 485]]
    print('box2 : ',box)
    cv.drawContours(img_color, [box], 0, (255,0,255), 2)

cv.imshow('result', img_color)
cv.waitKey(0)

cv.destroyAllWindows()