import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while(True) :
    ret,img_frame = cap.read()
    
    # HSV 색공간으로 변환한다.
    img_hsv = cv.cvtColor(img_frame, cv.COLOR_BGR2HSV)

    # 여기서 색을 검출하기 위한 상한, 하한값을 정한다.
    lowest_blue = (120-20, 70 ,0)
    highest_blue = (120+20, 255, 255)
    img_mask = cv.inRange(img_hsv, lowest_blue, highest_blue)

    # 컬러 영상에서 파란색만 보여준다.
    img_result = cv.bitwise_and(img_frame, img_frame, mask=img_mask)
    cv.imshow('color', img_frame)
    cv.imshow('result', img_result)

    key = cv.waitKey(1)
    if key == 27 :
        break

cap.release()
cv.destroyAllWindows()