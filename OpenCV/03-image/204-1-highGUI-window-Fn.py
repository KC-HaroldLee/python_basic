import os
import cv2 as cv

os.chdir('03-image\\images')
src = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)

cv.namedWindow('moveWindow1')
cv.moveWindow('moveWindow1', 0, 0)
cv.imshow('moveWindow1', src)
cv.waitKey(0)

cv.moveWindow('moveWindow1', 100, 100)
cv.waitKey(0)

cv.moveWindow('moveWindow1', -200, 100)
cv.waitKey(0)

cv.putText(src, 'title changed', (40,60), 4, 1.5, (170,110,170), 2)
cv.setWindowTitle('moveWindow1', 'heyHeyHey')
cv.waitKey(0)

# cv.setWindowTitle('heyHeyHey', 'didntworked')
cv.setWindowTitle('moveWindow1', 'heyHeyHey22')

# cv.getWindowProperty(str, prop_id)
# 윈도우의 속성을 검색

# cv.setWindowProperty(str, prop_id, prop_value)
# 윈도우의 속성을 prop_id의 prop_value로 변경

# 윈도우를 자동으로 업데이트하는 스레드를 실행
# cv.startWindowThread() # 인자가 없는게 맞음

cv.waitKey(0)
cv.destroyAllWindows()


