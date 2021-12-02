import os
import cv2 as cv

os.chdir('03-image\\images')

img1 = cv.imread('dal (1).jpg', cv.IMREAD_UNCHANGED)
cv.putText(img1, 'cv.IMREAD_UNCHANGED', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('IMREAD_UNCHANGED', img1)
cv.waitKey(0)

img1 = cv.imread('dal (1).jpg', cv.IMREAD_GRAYSCALE)
cv.putText(img1, 'cv.IMREAD_GRAYSCALE', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('IMREAD_GRAYSCALE', img1)
cv.waitKey(0)

img1 = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)
cv.putText(img1, 'cv.IMREAD_COLOR', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('IMREAD_COLOR', img1)
cv.waitKey(0)




img1 = cv.imread('dal (1).jpg', cv.IMREAD_ANYDEPTH)
cv.putText(img1, 'cv.IMREAD_ANYDEPTH', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('IMREAD_ANYDEPTH', img1)
cv.waitKey(0)

img1 = cv.imread('dal (1).jpg', cv.IMREAD_ANYCOLOR)
cv.putText(img1, 'cv.IMREAD_ANYCOLOR', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('IMREAD_ANYCOLOR', img1)
cv.waitKey(0)

img1 = cv.imread('dal (1).jpg', cv.IMREAD_REDUCED_GRAYSCALE_2)
cv.putText(img1, 'cv.IMREAD_REDUCED_GRAYSCALE_2', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('IMREAD_REDUCED_GRAYSCALE_2', img1)
cv.waitKey(0)

 

img1 = cv.imread('mangpo.jpg', cv.IMREAD_IGNORE_ORIENTATION)
cv.putText(img1, 'cv.IMREAD_IGNORE_ORIENTATION', (40,60), 4, 1.5, (170,110,170), 2)
cv.imshow('IMREAD_IGNORE_ORIENTATION', img1)
cv.waitKey(0)

img1 = cv.imread('mangpo.jpg', cv.IMREAD_IGNORE_ORIENTATION | cv.IMREAD_REDUCED_COLOR_2)
cv.putText(img1, 'cv.IMREAD_IGNORE_ORIENTATION | cv.IMREAD_REDUCED_COLOR_2', (40,60), 4, 1.5, (170,110,170), 2)

cv.imshow('IMREAD_IGNORE_ORIENTATION', img1)
cv.waitKey(0)

cv.destroyAllWindows()