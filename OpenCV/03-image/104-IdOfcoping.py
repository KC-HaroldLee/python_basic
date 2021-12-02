import os
import cv2 as cv

os.chdir('03-image\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_GRAYSCALE)
img_copy = img1.copy()

print(type(img_copy)) # <class 'numpy.ndarray'>
print('id가 같은가?', bool(id(img1)==id(img_copy))) # False