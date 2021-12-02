import cv2 as cv
import os 

os.chdir('06-imageCalc\\images')

src = cv.imread('tomato.jpg', cv.IMREAD_REDUCED_COLOR_2)
src_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
h, s, v = cv.split(src_hsv)

def trackbar_callback(x) :
    print(cv.getTrackbarPos('lowerb', 'hsvTest'), cv.getTrackbarPos('upperb', 'hsvTest'))

cv.namedWindow('hsvTest')
cv.createTrackbar('h-lowerb', 'hsvTest', 0, 255, trackbar_callback)
cv.createTrackbar('h-upperb', 'hsvTest', 0, 255, trackbar_callback)



while(True) :
    lowerb = cv.getTrackbarPos('h-lowerb', 'hsvTest')
    upperb = cv.getTrackbarPos('h-upperb', 'hsvTest')
    
    h_red = cv.inRange(h, lowerb, upperb)

    dst_hsv = cv.bitwise_and(src_hsv,src_hsv, mask = h_red)
    dst_bgr = cv.cvtColor(dst_hsv, cv.COLOR_HSV2BGR)

    cv.imshow('hsvTest', dst_bgr)
    key = cv.waitKey(33)
    if key == ord('q') :
        break
cv.destroyAllWindows()