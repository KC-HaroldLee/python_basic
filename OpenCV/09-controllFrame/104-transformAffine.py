import cv2 as cv
import os
import numpy as np
import sys

point_list=[]

def mouse_callback(event, x, y, flags, param) :
    if event == cv.EVENT_LBUTTONDOWN :
        print ('(%d, %d)'%(x, y))

        # point_list.append(x, y)
        point_list.append((x, y)) # 아 한 번에 넣어야하니까 튜플...!
        cv.circle(img_color, (x, y), 5, (0, 0, 255), -1)

# 마우스 콜백함수를 등록

cv.namedWindow('src')
cv.setMouseCallback('src', mouse_callback)

# 이미지를 불러오기(def보다 나중이지만)
os.chdir('09-controllFrame\\images')
img_color = cv.imread('sal (1).jpg', cv.IMREAD_COLOR)

while(True):

    cv.imshow('src', img_color)

    if cv.waitKey(1) == 32 :
        if len(point_list) >= 3 :
            break
        else :
            print('점 세개 이상 찍어주세요')
            break

h, w = img_color.shape[:2]
print(img_color.shape[0]) # h
print(img_color.shape[1]) # w
print(img_color.shape[2]) # 채널

# 대응점을 내리기
# 점을 세 개 이상 찍지 않으면 
# IndexError: list index out of range
# 가 발생한다.

try :
    pts1 = np.float32([point_list[0],point_list[1],point_list[2]])
    pts2 = np.float32([point_list[0],point_list[1],point_list[2]])
    pts2[1][1] += 100
except (IndexError) :
    print ('점을 세 개이상 찍지 않음')
    print ('종료')
    sys.exit(1)

print('pts1 : \n', pts1)
print('pts2 : \n', pts2)

# 아핀 변환 행렬을 생성한다
M = cv.getAffineTransform(pts1, pts2)
print('M', M)
# 이미지에 아핀 변환 행렬을 적용한다.
img_result = cv.warpAffine(img_color, M, (w,h))

# 결과를 보여준다.
cv.imshow('img_result', img_result)
cv.waitKey(0)
cv.destroyAllWindows()