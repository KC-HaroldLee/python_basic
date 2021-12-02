import cv2 as cv
import numpy as np

def mouse_event(event, x, y, flags, param) :
    global radius
    global colorList
    global colorIdx

    if event == cv.EVENT_LBUTTONDOWN : 
        cv.circle(param, (x, y), radius, colorList[colorIdx], 2)
        cv.imshow('draw', src)
    if event == cv.EVENT_MOUSEWHEEL :
        if flags > 0 :
            radius += 1
        elif flags < 0 :   
            radius -= 1

    if event == cv.EVENT_RBUTTONDOWN :
        if colorIdx == len(colorList) :
            colorIdx = 0
        else :
            colorIdx +=1

radius = 3
colorIdx = 0
colorList = [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,0,255),(0,255,255)]

src = np.zeros((500,500,3), dtype = np.uint8)

cv.imshow('draw', src)
cv.setMouseCallback('draw', mouse_event, src)

cv.waitKey(0)



