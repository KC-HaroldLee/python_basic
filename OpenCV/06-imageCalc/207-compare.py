import cv2 as cv

# 비교 ... 극단적
# True면 255 False면 0을 반환
# dst = cv.compare(src1, scr2, cmpop = ...)
# cmpop에 들어갈 수 있는 매개변수
cv.CMP_EQ # 요소가 같음
cv.CMP_GT # src1이 src2 보다 큼
cv.CMP_GE # src1이 src2 보다 크거나 같음
cv.CMP_LT # src1이 src2 보다 작음
cv.CMP_LE # src1이 src2 보다 작거나 같음
cv.CMP_NE # 같지 않음