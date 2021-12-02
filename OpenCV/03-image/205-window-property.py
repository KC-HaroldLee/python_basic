import os
import cv2 as cv

os.chdir('03-image\\images')
src = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)


# 전체화면
cv.namedWindow('prop1', cv.WINDOW_NORMAL) # 노말로 만들어야 가능하다.
cv.setWindowProperty('prop1', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN) # 전체화면

# 숫자로 설정하기
# cv.setWindowProperty('prop1', cv.WND_PROP_FULLSCREEN, 1) # 전체화면
# cv.setWindowProperty('prop1', cv.WND_PROP_FULLSCREEN, 0) # 해제
cv.imshow('prop1', src)
cv.waitKey(0)

# 전체화면 해제 후 크기 조절
cv.setWindowProperty('prop1', cv.WND_PROP_FULLSCREEN, 0) # 해제
cv.resizeWindow('prop1', 400, 400)
cv.waitKey(0)


cv.setWindowProperty('prop1', cv.WND_PROP_ASPECT_RATIO, 1)
cv.waitKey(0)

cv.destroyAllWindows()


