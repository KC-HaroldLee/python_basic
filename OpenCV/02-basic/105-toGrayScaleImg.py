import os
import cv2

os.chdir("02-basic\\images")
img1 = cv2.imread('20210624_175217.jpg', cv2.IMREAD_COLOR)

# if img1 = None : # 'is'어야 한다. 'is' is 'is'.
if img1 is None :
    print('파일이 없습니다.') # FileNotFoundError: [WinError 3]

cv2.namedWindow('한글도 되나?')
cv2.imshow('한글도 되나?', img1)

# 이러면 이 창이 꺼지고 아래 코드가 실행된다.
cv2.waitKey(0)

# 이제 그레이 스케일 이미지로 바꿔본다.
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# 담자
cv2.namedWindow('gray')
cv2.imshow('gray', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('gray-test.jpg', img2)
