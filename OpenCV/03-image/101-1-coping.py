import os
import cv2 as cv

os.chdir('03-image\\images')
img1 = cv.imread('mangpo.jpg', cv.IMREAD_GRAYSCALE)

img2 = img1

print(id(img1), id(img2))
bool1 = id(img1)==id(img2)
print('id가 같은가?', bool(id(img1)==id(img2))) # True