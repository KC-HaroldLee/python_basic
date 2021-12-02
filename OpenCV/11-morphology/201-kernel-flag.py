import cv2 as cv
import os

def on_trackbar (x) :
    pass

os.chdir('11-Morphology\\images')

src = cv.imread('eng.jpg', cv.IMREAD_GRAYSCALE)

img_binary = cv.adaptiveThreshold(src, 220,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 4)
start_x, start_y, end_x, end_y = 873,1921,386,700
img_sub = img_binary[386:750, 873:1980]

cv.namedWindow('img_sub')
cv.createTrackbar('threshold', 'img_sub', 0, 255, on_trackbar)
cv.setTrackbarPos('threshold', 'img_sub', 127)

cv.imshow('img_sub', img_sub)
cv.waitKey(0)

# 루프
while(True) :
    thresh = cv.getTrackbarPos('threshold', 'binarization with track-bar')

    # retval, img_binary = cv.threshold(img_concath, thresh, 255, cv.THRESH_BINARY)
    retval, img_binary = cv.threshold(src, thresh, 255, cv.THRESH_BINARY)
    cv.imshow('binarization with track-bar', img_binary)

    if cv.waitKey(1) & 0xFF ==27 :
        break


# 직사각형 형태
cv.MORPH_RECT

# 십자가 형태
cv.MORPH_CROSS

# 타원 형태
cv.MORPH_ELLIPSE

cv.destroyAllWindows()