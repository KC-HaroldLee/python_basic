import cv2 as cv
import math
import os
import numpy as np

# 허프 변환 (직선을 구하기 위한.)

# lines = cv.HoughLines(iamge, rho, theta, threshold)

# image : 8비트 바이너리 이미지어야한다.
# ~Lines : 극 좌표계에서의 교차점 정보인 r, θ 을 리턴한다.
# Rho : r의 범위, 0에서 1사이의 실수를 입력한다.
# Theta : θ 범위, 0에서 180사이 단위는 라디안
# Threshold : 곡선이 만다는 기준, 클수록 정확도는 올라가고 검출되는 직선의 개수는 줄어든다.