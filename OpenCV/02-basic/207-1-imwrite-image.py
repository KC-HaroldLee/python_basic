import cv2 as cv
import os
import numpy as np

os.chdir('02-basic\\images-save')

# 기본저장 옵션은 8비트 3채널이다.
# cv.imwrite(filename, img, params= None)
# 그리고 기본적으로 bool을 반환한다. (저장 실패시 오류를 반환하지 않고 false를 반환)

img1 = np.zeros((256,256), np.uint8)
bool1 = cv.imwrite('test001.jpg', img1, (cv.IMWRITE_JPEG_QUALITY, 100, cv.IMWRITE_JPEG_PROGRESSIVE, 1))
print(bool1)

cv.IMWRITE_JPEG_QUALITY
# JPEG 화질 (0 ~ 100)
cv.IMWRITE_JPEG_PROGRESSIVE
# 점차 선명해짐 적용 (0, 1)
cv.IMWRITE_JPEG_OPTIMIZE
# 최적화 적용 (0 , 1)
cv.IMWRITE_JPEG_RST_INTERVAL
# 마커의 간격 설정 (0 ~ 65535)
cv.IMWRITE_JPEG_LUMA_QUALITY
# 루마 품질 적용 (0 ~ 100)
cv.IMWRITE_JPEG_CHROMA_QUALITY
# 크로마 품질 적용 (0 ~ 100)
cv.IMWRITE_PNG_COMPRESSION
# PNG 압축 (0 ~ 100)
cv.IMWRITE_PNG_BILEVEL
# 바이너리 포맷 사용 (0, 1)
cv.IMWRITE_PXM_BINARY
# PPM, PGM, PBM 파일을 바이너리 포맷 사용
cv.IMWRITE_WEBP_QUALITY
# WebP 적용 (0 ~ 100)
cv.IMWRITE_TIFF_RESUNIT
# TIFF사용 (DPI 값)
cv.IMWRITE_TIFF_XDPI
# TIFF의 X 방향 (DPI 값)
cv.IMWRITE_TIFF_YDPI
# TIFF의 Y 방향 (DPI 값)