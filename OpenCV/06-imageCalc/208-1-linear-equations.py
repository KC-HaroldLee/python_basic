# 선형 방정식의 해
# linear equations

# 메모만 해둔다...
import cv2 as cv

# success, dst = cv.solve(src1, src2, flags=None)


# flags
cv.DECOMP_LU # LU분해(가우스 소거)
cv.DECOMP_SVD # 특이ㅅ값 분해
cv.DECOMP_EIG # 고유ㅅ값 분해*
cv.DECOMP_CHOLESKY # 슐레스키 분해*
cv.DECOMP_QR # qr인수 분해
cv.DECOMP_NORMAL # 노멀 분해**

# *  src1행렬은 대칭이어야함
# ** src · dst = src2 방정식 사용

