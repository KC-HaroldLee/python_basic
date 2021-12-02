import cv2
import os

os.chdir("02-basic\\images") # 매번 쳐야하는 걸까...
img1 = cv2.imread('20210624_175217.jpg')
print(type(img1))
print(img1)
cv2.namedWindow('viewer-1', cv2.WINDOW_GUI_NORMAL)

cv2.imshow('viewer-1', img1)

cv2.waitKey(0) #? 은 뭐지
cv2.destroyAllWindows()
