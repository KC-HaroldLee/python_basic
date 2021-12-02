import cv2 as cv
import os

os.chdir('05-binarization\\images')

# src = cv.imread('mangpo.jpg', cv.IMREAD_REDUCED_COLOR_8)
src = cv.imread('mangpo.jpg', cv.IMREAD_REDUCED_GRAYSCALE_8)

option = [cv.THRESH_BINARY, cv.THRESH_BINARY_INV, cv.THRESH_TRUNC, cv.THRESH_TOZERO, cv.THRESH_TOZERO_INV]

idx = 0

def trackbar_callback (x) :
    pass

cv.namedWindow('result')
cv.createTrackbar('low', 'result', 0, 255, trackbar_callback)
cv.createTrackbar('high', 'result', 0, 255, trackbar_callback)
cv.setTrackbarPos('low', 'result', 170)
cv.setTrackbarPos('high', 'result', 255)

while(True) :

    key = cv.waitKey(33)
    
    if key == ord('+') :
        idx += 1
    elif key == ord('-') :
        idx -= 1
    elif key == ord('q') :
        break

    if idx > len(option) -1 :
        print('오버')
        idx = 0
    elif idx < 0 : 
        print('언더')
        idx = len(option) -1
    
    lowV = cv.getTrackbarPos('low', 'result')
    highV = cv.getTrackbarPos('high', 'result')
    ret, src_bin = cv.threshold(src, lowV, highV, option[idx])
    # cv.putText(src_bin, str(option[idx]), )
    cv.imshow('result', src_bin)


cv.destroyAllWindows()
