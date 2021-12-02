# 리뷰
import cv2
import os

os.chdir("02-basic\\images") # 언젠가 경로제어를 할 수 있겠지...

# imread()
img1 = cv2.imread('20210624_175217.jpg', cv2.IMREAD_COLOR)
# 인자 0 - 파일이름
# 인자 1 - 옵션
# 'IMREAD_COLOR'인 경우 컬러 포맷으로 영상을 읽겠다는 의미

print(type(img1)) # <class 'numpy.ndarray'>
# 타입은 '넘파이 배열'이라고 한다. 이를 print하면...
# print(img1) # 너무 길어서 주석으로 처리


# 만약 이미지가 없는 경우
img2 = cv2.imread('not.jpg')
print(type(img2)) # <class 'NoneType'>

# 음 뭐랄까 객체를 만드는 느낌
# 윈도우를 만든다. 
cv2.namedWindow('viewer', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('viewer', img1)

# 여기까지만 만들면 출력되고 바로 사라진다.

# waitkey(time-ms)
# ms단위로 지정한 시간만큼 대기한다.
# 키보드 입력이 있을 때까지 대기한다.
cv2.waitKey(0)

# 사용이 끝난 후 윈도우를 종료해준다.
cv2.destroyAllWindows()