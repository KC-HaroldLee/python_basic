import cv2 as cv
import os

os.chdir('02-basic\\videos')
cap = cv.VideoCapture('star.mp4')

cv.namedWindow('frame and msec')


roofCount = 0
infomation = True

while(True) :
    ret, frame = cap.read()
    frameStamp = str(cap.get(cv.CAP_PROP_POS_FRAMES))+ '/'+ str(cap.get(cv.CAP_PROP_FRAME_COUNT))
    msecStamp = str(cap.get(cv.CAP_PROP_POS_MSEC))
    pos_bycalc = str(cap.get(cv.CAP_PROP_POS_FRAMES) / cap.get(cv.CAP_PROP_FRAME_COUNT)) + '%'
    pos_byprop = str(cap.get(cv.CAP_PROP_POS_AVI_RATIO)) + '%'

    if cv.waitKey(33) == ord('`'):
        if infomation :
            infomation = False
        else :
            infomation = True

    if infomation : 
        cv.putText(frame, 'roofcount : ' + str(roofCount), (40,20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,200,255), 1)
        cv.putText(frame, 'framestamp : '+ frameStamp, (40,50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,200,255), 1)
        cv.putText(frame, 'msecStamp : '+ msecStamp, (40,80), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,200,255), 1)

    # 루프
    # if cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT) :
    cap.open('star.mp4')
    roofCount += 1

    # ret False 찾기
    print(frameStamp, ret)

    cv.imshow('frame and msec', frame)
    # q를 누르면 빠져나옴
    if cv.waitKey(33) == ord('q'): 
        break
    else :
        continue