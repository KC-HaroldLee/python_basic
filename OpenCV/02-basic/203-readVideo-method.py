import cv2 as cv
import os


os.chdir('02-basic\\videos')
cap = cv.VideoCapture('star.mp4')

# cap.isOpened()
# 열기 성공 여부
print(cap.isOpened()) # True


# cap.read
# 동영상 파일에서 프레임을 읽음
# bool 과 ndarray를 반환한다.
print(cap.read())


# cap.open()
# (새)파일을 읽음 
framecount1 = cap.get(cv.CAP_PROP_FRAME_COUNT)

cap.open('dal.mp4') # 새로 읽고
framecount2 = cap.get(cv.CAP_PROP_FRAME_COUNT)
print('isSame : {0}, f1 = {1}, f2 = {2}'
.format(bool(framecount1 == framecount2), framecount1, framecount2))
# isSame : False, f1 = 141.0, f2 = 323.0


# cap.set(propId, value)
# 동영상 파일 속성을 지정한다.
# cap.get(propId)
# 동영상 파일 속성을(값을) 반환한다.