import os
import sys
import cv2 as cv

def on_trackbar (x) :
    pass

os.chdir('05-binarization\\images')
# img1 = cv.imread('gr.jpg', cv.IMREAD_COLOR)
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_COLOR)
# img2 = cv.imread('gr.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)


# img_concath = cv.hconcat([img1, img2]) 

cv.namedWindow('binarization with track-bar')
cv.createTrackbar('threshold', 'binarization with track-bar', 0, 255, on_trackbar)
cv.setTrackbarPos('threshold', 'binarization with track-bar', 127)

# 루프
while(True) :
    thresh = cv.getTrackbarPos('threshold', 'binarization with track-bar')

    # retval, img_binary = cv.threshold(img_concath, thresh, 255, cv.THRESH_BINARY)
    retval, img_binary = cv.threshold(img1, thresh, 255, cv.THRESH_BINARY)
    cv.imshow('binarization with track-bar', img_binary)

    if cv.waitKey(1) & 0xFF ==27 :
        break