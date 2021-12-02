import cv2 as cv
import numpy as np

# 1번째 방법 - 사각형의 두 좌표를 사용

# img = cv.rectangle(img, pt1, pt2, color[, thickness])

# img : 사각형을 그릴 이미지
# pt1 : 사각형의 왼쪽 위 좌표
# pt2 : 사각형의 오른쪽 아래 좌표
# color : 사각형의 색
# thickness : 선의 굵기(-1이면 내부가 채워진다)


# 2번째 방법 - 사각형의 왼쪽 위 좌표와 너비, 높이 사용

# img = cv.retangle(img, rec, color[, thickness[, lineType[, shift]]])

# rec는 4가지 값으로 구성된다. 
# 왼쪽위 x좌표, 왼쪽위 y좌표, 너비, 높이