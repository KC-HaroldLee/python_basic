import os
import cv2 as cv

os.chdir('16-contours\\images')
img_color = cv.imread('square.png', cv.IMREAD_COLOR)
# imread할 때 그냥 해보자
img_gray = cv.imread('square.png', cv.IMREAD_GRAYSCALE)
ret, img_bin1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img_bin2 = cv.morphologyEx(img_bin1, cv.MORPH_CLOSE, kernel)
contours, hierarchy = cv.findContours(img_bin2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# 일단 기존의 것을 그려본다.
cv.drawContours(img_color, contours, -1, (0,0,225),2)

# 근사치 계산
for contour in contours :
    
    epsilon = 0.03 * cv.arcLength(contour, True) 
    # 0-curve 1-closed여부
    print('epsilon', epsilon) # epsilon 42.92893891096115
    print(type(epsilon)) #<class 'float'>

    approx = cv.approxPolyDP(contour, epsilon, True)
    # 0-curve 1-엡실론 2-closed여부
    print('approx', approx) 
    # [[[192 192]]
    # [[184 466]]
    # [[485 467]]
    # [[483 193]]]
    print(type(approx))# <class 'numpy.ndarray'>


    cv.drawContours(img_color, approx, 0, (0,255,0), 2)

cv.imshow('result', img_color)
cv.waitKey(0)
cv.destroyAllWindows