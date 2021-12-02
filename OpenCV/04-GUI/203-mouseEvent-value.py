from typing_extensions import ParamSpecKwargs
import cv2 as cv
import numpy as np

zeros = np.zeros((500,500,3), dtype = np.uint8)
src = zeros

cv.namedWindow('mouseEvt')

def mouse_event(event, x, y, flags, param) :
    global src
    # if event == cv.EVENT_LBUTTONDOWN and flags == cv.EVENT_FLAG_CTRLKEY :
    # if event == cv.EVENT_LBUTTONDOWN and flags == 9 :
    #     print('컨 + 왼')
    #     print(flags)
    #     cv.putText(src, 'crtl+Lbtn', (40,60), 2, 1, (255,255,255), 2)

    if event == cv.EVENT_LBUTTONDOWN : 
        src = zeros
        cv.imshow('mouseEvt', src)  
        cv.putText(src, 'cv.EVENT_LBUTTONDOWN', (40,60), 2, 1, (255,255,255), 2)
        print('왼 버튼')
        print(flags)   
        cv.imshow('mouseEvt', src)
    if event == cv.EVENT_MOUSEWHEEL :
        src = zeros
        if flags > 0 :
            print('휠 양수')
            cv.putText(src, 'cv.EVENT_MOUSEWHEEL +', (40,60), 2, 1, (255,255,255), 2)
            print(flags)
            cv.imshow('mouseEvt', src)
        elif flags < 0 :   
            print('휠 음수')
            cv.putText(src, 'cv.EVENT_MOUSEWHEEL -', (40,60), 2, 1, (255,255,255), 2)
            print(flags)
            cv.imshow('mouseEvt', src)
    if event == cv.EVENT_RBUTTONDOWN :
        src = zeros
        cv.imshow('mouseEvt', src)     
        cv.putText(src, 'cv.EVENT_RBUTTONDOWN', (40,60), 2, 1, (255,255,255), 2)
        print('오른 버튼')
        cv.imshow('mouseEvt', src)



cv.imshow('mouseEvt', src)
cv.setMouseCallback('mouseEvt', mouse_event, src)

cv.waitKey(0)



