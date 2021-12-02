import cv2 as cv
import os
# import psutil

os.chdir('02-basic\\videos')

cap1 = cv.VideoCapture('star.mp4')
# 성공여부를 반환하진 않는다.
# 읽더라도 프레임을 반환하는 것이 아닌. 프레임에 대한 정보만 갖고 있다.

roofCount = 0
infomation = False

while(True) :
    ret, frame = cap1.read()
    frameStamp = str(cap1.get(cv.CAP_PROP_POS_FRAMES))+ '/'+ str(cap1.get(cv.CAP_PROP_FRAME_COUNT))
    
    if cv.waitKey(33) == ord('`'):
        if infomation :
            infomation = False
        else :
            infomation = True

    if infomation : 
        cv.putText(frame, frameStamp, (40,20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,200,255), 1)
        cv.putText(frame, 'roofcount : ' + str(roofCount), (40,50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,200,255), 1)

    # 루프
    if cap1.get(cv.CAP_PROP_POS_FRAMES) == cap1.get(cv.CAP_PROP_FRAME_COUNT) :
        cap1.open('star.mp4')
        roofCount += 1

    # ret False 찾기
    print(frameStamp, ret)

    cv.imshow('video', frame)

    # q를 누르면 빠져나옴
    if cv.waitKey(33) == ord('q'): 
        break

cap1.release()
cv.destroyAllWindows()