import cv2 as cv

# 보간법(interpolation)

# 가장 가까운 이웃 보간법
cv.INTER_NEAREST

# 쌍 선형 보간법
cv.INTER_LINEAR

# 영역 보간법
cv.INTER_AREA

# 4*4바이 큐빅 보간법
cv.INTER_CUBIC

# 8*8 란초스 보간법
cv.INTER_LANCZOS4