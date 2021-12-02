import os
import cv2 as cv

os.chdir('03-image\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_GRAYSCALE)

img2 = img1

print(id(img1), id(img2))
bool1 = id(img1)==id(img2)
print('id가 같은가?', bool(id(img1)==id(img2))) # True

cv.line(img1, (0,0), (500,500), 0, 10)

cv.imshow('img1', img1)
cv.imshow('img2', img2)

cv.waitKey(0)
cv.destroyAllWindows()