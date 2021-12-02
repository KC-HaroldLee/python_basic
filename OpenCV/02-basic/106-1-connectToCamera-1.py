import cv2
print(cv2.__version__) # 4.5.2
# 카메라에서의 객체는 VideoCapture

# cap = cv2.VideoCapture(0) # terminating async callback 경고를 발생시킴
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print(type(cap)) # <class 'cv2.VideoCapture'>

if cap.isOpened() == False :
    print('카메라 연결 실패')
    exit(1)