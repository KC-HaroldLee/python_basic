# 1차 공부 예제는 04-GUI에 있음

import cv2 as cv
import numpy as np
import os

os.chdir('03-image\\images')
three = cv.imread("three.jpg")
four = cv.imread("four.jpg")

# 가로로 배치한다고 가정하고 시작

# 1. 세로크기를 비교한다. (세로 배치일 때는 가로를 비교하겠지.)
h3, w3 = three.shape[:2] # :3까지 하면 (2는 채널)
print(h3, w3)
h4, w4 = four.shape[:2]
print(h4, w4)

if h3 > h4 :
    print('3의 높이가 크다')
    emptySpace = np.zeros((h3-h4, w3, 3), np.uint8)
    # 재정의를 하자
    four = cv.vconcat(three, emptySpace)
    print(three.ndim) # 3
    print(four.ndim) # 3
    four = four[np.newaxis]
    print(three.ndim) # 3
    print(four.ndim) # 3
    result = cv.hconcat(three, four)
    print(result)
elif h3 < h4 :
    print('4의 높이가 크다')
    emptySpace = np.zeros((h4-h3, w3, 3), np.uint8)
    # 재정의를 하자
    # left1 = np.stack # 사용할 수 없음, 어느 한방향은 서로 같지 않다.
    left1 = cv.vconcat([three, emptySpace])
    # left2 = left1[np.newaxis]
    right1 = four
    result = cv.hconcat(left1, right1)
    print(result)
else :
    print('둘이 같다.')
    # emptySpace가 필요없음


cv.imshow("three", three)
cv.imshow("four", four)
cv.imshow("emptySpace", emptySpace)
cv.imshow("left1", left1)
# cv.imshow("left2", left2)
cv.imshow("right1",right1)
cv.imshow("result", result)

cv.waitKey()
cv.destroyAllWindows()
