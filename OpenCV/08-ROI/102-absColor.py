import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True :

    ret, img_color = cap.read()
    img_result = img_color.copy() # 굳이?
    # print(type(img_color), type(img_result)) # <class 'numpy.ndarray'> <class 'numpy.ndarray'>

    height, width = img_color.shape[:2]

    center_x = int(width/2.0)
    center_y = int(height/2.0)

    # ROI 영역을 빨간색 사각형으로 표시.
    cv.rectangle(img_color, (center_x-100, center_y-100), (center_x+100, center_y+100), (0, 0, 255), 3)

    # ROI 영역을 구해서 평균을 구한다.
    img_ROI = img_color[center_y-100:center_y+100, center_x-100:center_x+100]

    m = cv.mean(img_ROI) # mean이 뭐지...
    print(type(m), m)

    img_mean = np.zeros(img_ROI.shape, dtype=np.uint8)
    # 전부 = 평균값!
    img_mean[:] = (m[0], m[1], m[2])
    cv.imshow('mean', img_mean)
    cv.imshow('color', img_color)
    cv.imshow('ROI', img_ROI)

    key = cv.waitKey(1) 
    if key == 27 :
        break