import os
import cv2 as cv

os.chdir('03-image\\images')

img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
# cv.namedWindow(str, windowFlags)
# 윈도우를 생성한다.

cv.namedWindow('result', cv.IMREAD_GRAYSCALE)
cv.imshow('result', img1)

# cv.setWindowProperty(str, windowPropertyFlags, int)
# int는 일종의 스위치 예를들어 'FullscreeN'플래그에는 WINDOW_NORMAL, WINDOW_FULLSCREEN이 있는데
# 0인경우 노말, 1인경우 풀스크린을 사용한다.

# cv.imshow(str, mat)
# 윈도우에 이미지를 표시한다.(갱신된다고 해서 이미지가 새로 띄워지는 것은 아님)
# 뒤는 Mat형식

# cv.resizeWindow('result', w, h)
# 윈도우 크기 조절
cv.namedWindow('resized', flags=cv.WINDOW_FREERATIO)
cv.resizeWindow('resized', 400, 200)
cv.imshow('resized', img1)
cv.waitKey(0)
cv.destroyAllWindows()

