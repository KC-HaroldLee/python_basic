# 테두리 외삽법 유형
import cv2 as cv

# 고정 값으로 픽셀을 확장
cv.BORDER_CONSTANT 
# iiiiii | abcdefgh | iiiiii

# 테두리 픽셀을 복사해서 확장
cv.BORDER_REPLICATE
# aaaaaa | abcdefgh | hhhhhh

# 픽셀을 반사해서 확장
cv.BORDER_REFLECT
# gfecba | abcdefgh | hgfedc

# 반대쪽 픽셀을 복사해서 확장
cv.BORDER_WRAP
# cdefgh | abcdefgh | gfedcba

# 이중픽셀을 만들지 않고 반사해서 확장 
cv.BORDER_REFLECT_101
cv.BORDER_DEFAULT # 동일
# gfedcb | abcdefgh | gfdcba

# 픽셀을 투명하게 해서 확장
cv.BORDER_TRANSPARENT
# uvwxyz | abcdefgh | ijklmno

# ROI밖은 고려하지 않음
cv.BORDER_ISOLATED