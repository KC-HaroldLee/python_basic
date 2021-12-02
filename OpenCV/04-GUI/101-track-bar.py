import cv2 as cv
import os

# 트랙바가 조정될 때마다 실행되는 콜백함수라고 한다.
# 이곳에 트랙바로 조정할 OpenCV함수를 넣을 수도 있다고 하는데
def trackbar_for_callback(x) :
    print('트랙바 조정 중')
    print('low = {0}, high ={1}'.format(cv.getTrackbarPos('low thershold', 'Canny'), cv.getTrackbarPos('high thershold', 'Canny')))
    pass

# namedWindow를 한 번 더 사용하여 트랙바를 '붙일'윈도우를 생성한다고 한다.
cv.namedWindow('Canny') # Canny

# 트랙바를 생성한다.
# 이름이 정직하지만, 옵션은 많다.
a = cv.createTrackbar('low thershold', 'Canny', 0, 1000, trackbar_for_callback)
b = cv.createTrackbar('high thershold', 'Canny', 0, 1000, trackbar_for_callback)
# 0 - 트랙바 명칭, 1 - 해당 윈도우(Canny), 2 - 최솟값, 3 - 최대값, 콜백함수 이름
# <class 'NoneType'> ???


# 트랙바의 초기값을 설정해준다.
# 약자가...아니라 position이구나
cv.setTrackbarPos('low thershold', 'Canny', 50)
cv.setTrackbarPos('high thershold', 'Canny', 50)
# 0 - 트랙바 명칭, 1 - 해당 윈도우(Canny), 2 - 값

# 이미지를 불러오자
os.chdir('04-GUI\\images')
img1 = cv.imread('mangpo-s.jpg', cv.IMREAD_GRAYSCALE)

while(1) :
    # 현재 트랙바 위치를 가져온다?
    low = cv.getTrackbarPos('low thershold', 'Canny')
    high = cv.getTrackbarPos('high thershold', 'Canny')
    # 0 - 트랙바 명칭, 1 - 해당 윈도우(Canny)


    # 트랙바에서 가져온 두 값을 Canny함수의 파라미터를 조정한다.

    img_Canny = cv.Canny(img1, low, high)

    cv.imshow('Canny', img_Canny)
    if cv.waitKey(1) & 0xFF==27:
        break

cv.destroyAllWindows()