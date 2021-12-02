# edges = cv.Canny(image, thershold1, thershold2, [,edges [, aperureSize [,L2gradient]]])

# image : 그레이 스케일 입력 이미지
# thershold1 : 첫번째 임계값
# thershold2 : 두번째 입계값
# aperureSize : 소벨 연산에서 사용할 마스크 크기

import cv2 as cv
import os

def trackbar_for_callback(x) :
    print('low = {0}, high ={1}'.format(cv.getTrackbarPos('thershold1', 'cannyEdge'), cv.getTrackbarPos('thershold2', 'cannyEdge')))
    pass

cv.namedWindow('cannyEdge')

a = cv.createTrackbar('thershold1', 'cannyEdge', 0, 255, trackbar_for_callback)
b = cv.createTrackbar('thershold2', 'cannyEdge', 0, 255, trackbar_for_callback)


os.chdir('10-convolutionAndMask\\images')
img_gray = cv.imread('po.jpg', cv.IMREAD_GRAYSCALE)

initmin = 50
initmax = 150

cv.setTrackbarPos('thershold1', 'cannyEdge', initmin)
cv.setTrackbarPos('thershold2', 'cannyEdge', initmax)

while (True) :
    t1v = cv.getTrackbarPos('thershold1', 'cannyEdge')
    t2v = cv.getTrackbarPos('thershold2', 'cannyEdge')

    img_canny = cv.Canny(img_gray, t1v, t2v)

    cv.imshow('cannyEdge', img_canny)
    if cv.waitKey(1) & 0xFF==27:
        break


cv.destroyAllWindows()