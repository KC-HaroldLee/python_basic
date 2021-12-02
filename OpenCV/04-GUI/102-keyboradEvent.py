# 키보드 이벤트

import os
import sys
import cv2 as cv
 
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
if cap.isOpened() == False : 
    print('연결된 카메라가 없습니다, 종료')
    sys.exit(1)
else :
    print('카메라 연결 성공')

# 단계를 나타낼 간단한 변수
step = 1

while(True) :
    # 튜플이라 나누고, imread()가 아닌 read()다
    ret, img1 = cap.read() # <class 'tuple'>
    print(type(ret), type(img1)) # <class 'bool'> <class 'numpy.ndarray'>

    if ret == False :
        print('캡쳐는 실패, 종료')
        sys.exit(1)
    else :
        print('캡쳐 성공')

    # if step == 1 : # 어차피 1일테니 이건 생략
    if step == 2 :
        img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    if step == 3 :
        img1 = cv.Canny(img1, 30, 90)

    # 앞에서 처리된 결과에 따라 다른 이미지가 보여지게
    cv.namedWindow('result') # 익숙해 지기전까지는 계속 치자
    cv.imshow('result', img1)

    # waitKey()설정인데 흠
    key = cv.waitKey(1)
    if key == 27 : # esc 키
        break

    # 입력된 키에 딸 step변수에 다른 값을 대입한다.
    # 파이썬에서는 ord함수를 사용하여 문자를 아스키코드로 변환..!! 할 수 있다.
    if key == ord('q') :
        step = 1
    if key == ord('w') :
        step = 2
    if key == ord('e') :
        step = 3

cap.release()
cv.destroyAllWindows()