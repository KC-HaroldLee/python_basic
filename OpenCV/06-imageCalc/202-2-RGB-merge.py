import cv2 as cv
import os 

os.chdir('06-imageCalc\\images')

src = cv.imread('dal (1).jpg', cv.IMREAD_REDUCED_COLOR_2)
mv = cv.split(src) # 분리

dst = cv.merge([mv[0], mv[1], mv[2]])
# dst = cv.merge([mv[0], mv[1]]) # cv2.error:Invalid number of channels in input image
# dst = cv.merge([mv[1], mv[2]]) # cv2.error:Invalid number of channels in input image
# dst = cv.merge([mv[1], mv[2]]) # cv2.error:Invalid number of channels in input image
dst = cv.merge([mv[0]])


dst = cv.merge([mv[2], mv[1], mv[0]]) # 파란 고양이...
dst = cv.merge([mv[1], mv[2], mv[0]]) # 초록 고양이...
dst = cv.merge([mv[2], mv[2], mv[1]]) # 민트 고양이...
cv.imshow('dst', dst)


cv.waitKey(0)