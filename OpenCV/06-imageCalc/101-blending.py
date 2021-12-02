import os
import cv2 as cv

alpha = 0.0
beta = 1.0

os.chdir('06-imageCalc\\images')

while alpha <= 1.0 :

    # 블렌딩 하는 이미지 크기는 같아야한다고 한다.

    img1 = cv.imread('dal (1).jpg', cv.IMREAD_COLOR)
    img2 = cv.imread('dal (2).jpg', cv.IMREAD_COLOR)

    dst = cv.addWeighted(img1, alpha, img2, beta, 0)

    print('alpha={0}, beta={1}'.format(alpha, beta))

    cv.namedWindow('dst')
    cv.imshow('dst', dst)
    cv.waitKey(50)

    alpha = round(alpha + 0.1, 1)
    beta = round(beta - 0.1, 1)

cv.destroyAllWindows()