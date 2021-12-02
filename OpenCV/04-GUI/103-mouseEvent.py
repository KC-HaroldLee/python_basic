import os
import sys

import cv2 as cv
# import numpy as np
import numpy
import random as r

# 기본 세팅
# 자바와 달리 바로 초기값을 지정해줘야하는구나
# 자바도 결국 대부분 초기값을 지정해야하는 경우가 많긴 했지만
mouse_is_pressing = False # 왼버튼 상태를 체크하기 위해 사용
drawing_mode = True # 현재 그리기 모드 선택을 위해 사용(원/ 사각형)
start_x, start_y = -1, -1 # 최초로 왼마우스를 누른 위치를 저장하기 위해 사용
color = (255, 255, 255) # 색 지정시 사용 당연 튜플

# 마지막으로 그리기 결과를 저장할 이미지
img1 = numpy.zeros((512, 512, 3), numpy.uint8)


# 마우스 이벤트 발생시 호출될 함수를 정의한다. 인자가 많군
def mouse_callback(event, x, y, flags, param) :  
    # 전역변수?
    global color, start_x, start_y, drawing_mode, mouse_is_pressing

    print('event = ', event)
    print('color = ', color) 
    print('start_x = {0}, start_y = {1}'.format(start_x, start_y))
    print('drawing_mode = ', drawing_mode)
    print('mouse_is_pressing = ', mouse_is_pressing)

    # (1) 마우스를 이동하면 발생하는 이벤트
    if event == cv.EVENT_MOUSEMOVE : # 이동중
        if mouse_is_pressing == True : # (+누르면서)
            if drawing_mode == True : # 그리기 모드가 온이면
                cv.rectangle(img1,(start_x, start_y), (x, y), color, -1)
                # 0 - 이미지, 1 - (튜플)시작좌표, 2 - (튜플)끝 좌표, 3 - (튜플)색상, 4 - 이건 뭘까
            else : # 그리기 모드가 오프면
                cv.circle(img1, (start_x, start_y), max(abs(start_x - x), abs(start_y - y)), color, -1)  
                # 0 - 이미지, 1 - (튜플)시작좌표, 2 - ?, 3 - ?, 4 - (), 4 - (튜플)색상, 5 - 이건 뭘까
 
    # (2) 마우스 왼쪽 버튼을 누르면 발생하는 이벤트
    elif event == cv.EVENT_LBUTTONDOWN : 
        # 랜덤으로 색을 생성한다.
        color = (r.randrange(256), r.randrange(256), r.randrange(256))
        
        # 마우스 왼쪽 버튼을 누른 것을 체크
        mouse_is_pressing = True
        # 왼쪽 마우스 버튼을 누른 위치를 저장
        start_x, start_y = x, y

    # (3) 마우스 왼쪽 버튼을 떼면 발생하는 이벤트
    elif event == cv.EVENT_LBUTTONUP :
        mouse_is_pressing = False # 위와 동일
        
        if drawing_mode == True :
            cv.rectangle(img1,(start_x, start_y), (x, y), color, -1)
        else :
            cv.circle(img1, (start_x, start_y), max(abs(start_x - x), abs(start_y - y)), color, -1)

    # (4) 마우스 오른쪽 버튼을 떼면 발생하는 이벤트
    elif event == cv.EVENT_RBUTTONDOWN :
        drawing_mode = 1 - drawing_mode

# 지정한 윈도우에 마우스 콜백 함수를 지정해준다.
cv.namedWindow('mouse-event')
cv.setMouseCallback('mouse-event', mouse_callback)

while(1) :
    cv.namedWindow('mouse-event')
    cv.imshow('mouse-event', img1)

    key = cv.waitKey(1)
    if key == 27 :
        break

cv.destroyAllWindows()
