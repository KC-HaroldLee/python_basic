# 컨투어 검출 

import cv2 as cv

# 1. findContours()
# contours, hierachy = cv.findContours(iamge, modes, method)

# contours - 검출된 컨투어이다. 파이썬에서는 list의 형태로 반환된다.
# 각각 컨투어에는 오브젝트의 외곽선을 구성하는 좌표로 저장된다. (그래서 많았군)

# hierachy(계층) : 검출된 컨투어 정보를 구조적으로 저장하고 있다.

# image - 검은색과 하얀색으로 이루어진 바이너리 이미지이어야한다. (이진화 or 캐니 에지)

# mode - 4가지 모드가 있다. 
# 전체 컨투어를 검출하는 RETR_LIST와 외곽 컨투어만 검출하는 RETR_EXTERNAL을 주로 쓴다.
# RETR_LIST, RETR_CCOMP도 있다.

# method : 컨투어를 구성하는 포인트 검출 방법을 지정한다. 
# CHAIN_APPROX_NONE : 모든 점을 저장
# CHAIN_APPROX_SIMPLE : 직선인 경우는 시작점과 끝점만 저장

# 2. drawContours()
# image = cv.drawContours(image, contours, contouridx, color, thickness)

# contours : 컨투어가 저장된 리스트
# contouridx : 컨투어가 저장된 인덱스 음수로 지정하면 모든 것을 그림