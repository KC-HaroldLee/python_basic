import os
import cv2 as cv

os.chdir('03-image\\images')

img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('not_Flags')
cv.putText(img1, 'not_Flags', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('not_Flags', img1)
cv.waitKey(0)

img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('cv.WINDOW_NORMAL', cv.WINDOW_NORMAL)
cv.putText(img1, 'cv.WINDOW_NORMAL', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('cv.WINDOW_NORMAL', img1)
cv.waitKey(0)

img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('cv.WINDOW_AUTOSIZE', cv.WINDOW_AUTOSIZE)
cv.putText(img1, 'cv.WINDOW_AUTOSIZE', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('cv.WINDOW_AUTOSIZE', img1)
cv.waitKey(0)



img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('cv.WINDOW_KEEPRATIO', cv.WINDOW_KEEPRATIO)
cv.putText(img1, 'cv.WINDOW_KEEPRATIO', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('cv.WINDOW_KEEPRATIO', img1)
cv.waitKey(0)

img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('cv.WINDOW_FREERATIO', cv.WINDOW_FREERATIO)
cv.putText(img1, 'cv.WINDOW_FREERATIO', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('cv.WINDOW_FREERATIO', img1)
cv.waitKey(0)



img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('cv.WINDOW_KEEPRATIO', cv.WINDOW_KEEPRATIO)
cv.putText(img1, 'cv.WINDOW_KEEPRATIO', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('cv.WINDOW_KEEPRATIO', img1)
cv.waitKey(0)

img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('cv.WINDOW_FREERATIO', cv.WINDOW_FREERATIO)
cv.putText(img1, 'cv.WINDOW_FREERATIO', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('cv.WINDOW_FREERATIO', img1)
cv.waitKey(0)




img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('cv.WINDOW_GUI_EXPANDED', cv.WINDOW_GUI_EXPANDED)
cv.putText(img1, 'cv.WINDOW_GUI_EXPANDED', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('cv.WINDOW_GUI_EXPANDED', img1)
cv.waitKey(0)



cv.destroyAllWindows()
