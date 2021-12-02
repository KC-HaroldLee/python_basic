import os
import cv2 as cv

os.chdir('03-image\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_GRAYSCALE)
print(type(img1)) # <class 'numpy.ndarray'>

# numpy.ndarray[start_y:end_y, start_x:end_x]
# 쉽게 오프셋y+범위, 오프셋x=범위
img_sub1 = img1[20:20+150, 20:20+150]
print(type(img_sub1)) # <class 'numpy.ndarray'>

# numpy.ndarray.base
# ~의 베이스
# 예전에 상속에서 배운거랑 좀 비슷한 느낌이다.
print(img_sub1.base is img1) 
print('id가 같은가?', bool(id(img1)==id(img_sub1))) # False

cv.line(img1, (0,0), (500,500), 0, 10)
cv.imshow('img1', img1)
cv.imshow('img_sub1', img_sub1)

cv.waitKey(0)
