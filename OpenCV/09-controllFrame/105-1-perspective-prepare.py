import cv2 as cv
import os
import numpy as np
import sys

# 빈 이미지를 만드는 것이 아니라
# 퍼스펙티브 변환을 위한 좌표를 저장할 곳이다.
src = np.zeros([4, 2], np.float32)
print(src) #    [[0. 0.]
            #   [0. 0.]
            #   [0. 0.]
            #   [0. 0.]]

print(type(src)) # <class 'numpy.ndarray'>
idx = 0 # 나중에 1 씩 늘릴 것이다.

# numpy.ndarray은 list때 처럼 append하는 것이 아니라
# src[idx] 로 접근하여 값을 재정의 할 것이다.