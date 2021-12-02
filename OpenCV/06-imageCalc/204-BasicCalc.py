import cv2 as cv

# 덧셈
# dst = cv.add(src1, src2, mask = None, dtype = None)
# 덧셈은 최대값을 넘어가기 쉽다. 때문에 이미지 연산시 두 배열의 요소값을 고려하여 사용한다.

# 뺄셈
# dst = cv.subtract(src1, src2, mask = None, dtype = None)

# 곱셈
# dst = cv.multiply(src1, src2, mask = None, dtype = None)

# 나눗셈
# dst = cv.divide(src1, src2, mask = None, dtype = None)