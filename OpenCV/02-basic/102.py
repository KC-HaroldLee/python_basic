import cv2
import os

os.chdir("02-basic\\images") # 매번 쳐야하는 걸까...
img1 = cv2.imread('20200305_194420.jpg')
img2 = cv2.imread('20200801_001001.jpg')

cv2.namedWindow('viewer-1', cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow('viewer-2')

# cv2.resizeWindow('viewer-1', 400, 300) 
# cv2.resizeWindow('viewer-2', 400, 300) 

cv2.imshow('viewer-1', img1)
cv2.imshow('viewer-2', img2)

cv2.waitKey(0) #? 은 뭐지
cv2.destroyAllWindows()
