import cv2 as cv
import os


os.chdir('02-basic\\videos')
cap = cv.VideoCapture('star.mp4')

# cv.CAP_PROP_POS_FRAMES 
# 현재 프레임
print(cv.CAP_PROP_POS_FRAMES) # 언제나 1
print(cap.get(cv.CAP_PROP_POS_FRAMES)) # 0.0
cap.read() # 다음 프레임 읽기
print(cap.get(cv.CAP_PROP_POS_FRAMES)) # 1.0
cap.read() # 다음 프레임 읽기
print(cap.get(cv.CAP_PROP_POS_FRAMES)) # 2.0
cap.read() # 다음 프레임 읽기
print(cap.get(cv.CAP_PROP_POS_FRAMES)) # 3.0

# cv.CAP_PROP_POS_MSEC
# 현재 밀리초
cap.open('star.mp4') # 새로 불러오자.
print(cap.get(cv.CAP_PROP_POS_MSEC)) # 0.0
cap.read() # 다음 프레임 읽기
print(cap.get(cv.CAP_PROP_POS_MSEC)) # 0.0
cap.read() # 다음 프레임 읽기
print(cap.get(cv.CAP_PROP_POS_MSEC)) # 41.708333333333336
cap.read() # 다음 프레임 읽기
print(cap.get(cv.CAP_PROP_POS_MSEC)) # 83.41666666666667
cap.read() # 다음 프레임 읽기
print(cap.get(cv.CAP_PROP_POS_MSEC)) # 125.12499999999999

# cv.CAP_PROP_POS_AVI_RATIO
# 동영상 내의 상대적 위치 (0.0 ~ 1.0)
