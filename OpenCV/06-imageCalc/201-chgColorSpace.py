# 색상 공간 변환
import cv2 as cv

# 색상공간 변환 '2'를 중심으로 변환된다.
# BRG[A], RGB[A] 으로도 12개의 조합이 가능하다.
cv.COLOR_BGR2RGB
cv.COLOR_RGB2BGR
cv.COLOR_BGR2BGRA
cv.COLOR_BGR2RGBA
cv.COLOR_RGB2BGRA 
cv.COLOR_BGRA2BGR
# ... 이하 생략
# 그외에 XYZ, YUV, RGB뒤에 숫자가 붙는 것도 많다.

# HSV
# HLS
# Lab = CIE Lab, 반사율 색도1, 색도2
# Luv = CIE luv, CIE UVW기반
# GRAY
# BGR555 = 16 bit
# BGR565 = 16 bit
# XYZ = Rec, 709 색공간
# YCrCb = 크로마

# 8비트 색상범위 0~255
# 16비트 색상범위 0~65536 (65535가 아닌가)
# 32비트 생상범위 0.0~1.0 (42억이 아니라 다행)