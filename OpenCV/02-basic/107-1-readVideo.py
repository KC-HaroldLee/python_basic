import os
import cv2 as cv

os.chdir("02-basic\\images")
cap = cv.VideoCapture('dal.mp4')

if cap.isOpened() == False :
    print('파일이 없음')
    exit(1)

while(True) :
    ret, img_frame = cap.read()

    # 영상을 끝까지 재생하면 read함수는 False를 반환한다.
    if ret == False :
        print('동영상 파일 읽기 완료')
        break

    cv.namedWindow('video') # 생략 가능한 부분
    cv.imshow('video', img_frame)

    key = cv.waitKey(25)
    if key == 30 :
        break

cap.release()
cv.destroyAllWindows()

