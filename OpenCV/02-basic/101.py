import cv2
# from os import path 나는 무어을 위해...
import os

from numpy.core.fromnumeric import shape


print('작업위치1', os.getcwd())
os.chdir("02-basic\\images")
print('작업위치2', os.getcwd())
# img1 = cv2.imread(os.getcwd()+'\\opencv\\test.jpg', cv2.IMREAD_COLOR)


img1 = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
print(img1.shape)


if img1 is None :
    print('이미지가 없다')
else :
    cv2.namedWindow('viewer')
    cv2.imshow('viewer', img1)

    cv2.waitKey(0) #? 은 뭐지
    cv2.destroyAllWindows()