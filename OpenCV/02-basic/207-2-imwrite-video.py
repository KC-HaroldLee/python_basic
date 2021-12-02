import cv2 as cv
# import numpy as np
import os

os.chdir('02-basic\\videos')

# cv.imwrite(filename, fourcc, fps, framesize, isColor=True)
# fourcc : 사용할 압축 코덱
# framesize : 화면 크기

cap = cv.VideoCapture('Star.mp4')
# w = cap.shape[0] # AttributeError 
# h = cap.shape[1] # AttributeError
w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) # float -> int
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

videoWriter = cv.VideoWriter()
isWrite = False

while (True) :
    ret, frame = cap.read()

    # 리와인드 코드 시작
    if (cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT)) :
        # os.chdir('02-basic\\videos')
        os.chdir('..\\videos')
        cap.open('Star.mp4') # 리와인드
    # 리와인드 코드 끝
    
    cv.imshow('current', frame) # 계속 보여줌

    key = cv.waitKey(33)

    # 스위치 코드 시작
    if key == 4 : # ctrl + D
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        os.chdir('..\\videos-save')
        videoWriter.open('result.avi', fourcc, 30, (w, h), True)
        isWrite = True

    elif key == 24 : # ctrl + X
        videoWriter.release()
        isWrite = False

    elif key == ord('q') : break
    # 스위치 코드 끝

    # 저장 코드
    if isWrite == True :
        videoWriter.write(frame)

videoWriter.release()
cap.release()
cv.destroyAllWindows()

# 주요 함수
videoWriter.isOpened() # 성공여부 확인
videoWriter.write() # 동영상 파일에 프레임 저장
videoWriter.open() # 동영상 저장 구조 생성