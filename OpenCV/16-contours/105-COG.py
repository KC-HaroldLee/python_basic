import os
import cv2 as cv

os.chdir('16-contours\\images')
img_color = cv.imread('test.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, 
                        cv.CHAIN_APPROX_SIMPLE)


for contour in contours :

    mu = cv.moments(contour)
    print(mu) # <class 'dict'>
    print(type(mu)) # 많음...

    cx = int(mu['m10']/mu['m00'] + 1e-5)
    cy = int(mu['m01']/mu['m00'] + 1e-5)

    cv.circle(img_color, (cx, cy), 15, (0,255,255), -1)


cv.imshow("result", img_color)
cv.waitKey(0)