import cv2 as cv
import numpy as np
import os

from numpy.core.fromnumeric import reshape


# 근사치에 있는 것들을 검지
limit = 5 # 좌표 거리
def notInList (newObject) :
    global limit
    for detectedObject in detectedObjectList :
        a = detectedObject[0] - newObject[0]
        b = detectedObject[1] - newObject[1]
        if np.sqrt(a*a + b*b) < limit :
            return False
    return True

detectedObjectList = []

os.chdir('14-templateMatching\\images')
img_rgb = cv.imread('test.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

img_template = cv.imread('template.jpg', cv.IMREAD_GRAYSCALE)
w, h = img_template.shape[:2]

res = cv.matchTemplate(img_gray, img_template, cv.TM_CCOEFF_NORMED)

# 임계값 0.9보다 크고
# 기존에 템플릿 검출 리스트에 포함된 좌표의 거리가 5이상이어야(위 def)
# 새로운 좌표로 리스트에 추가한다.
count = 0 
for x in range(res.shape[1]) :
    for y in range(res.shape[0]) :
        if res[y, x] > 0.9 and notInList((x, y)) :
            detectedObjectList.append((x, y))
            # cv.rectangle(img_rgb, (x, y), (x+w, y+h), [0,0,255], -1)
            cv.rectangle(img_rgb, (x, y), (x+w, y+h), [0,0,255], 1)
            count = count + 1

print('count : ', count)
cv.imshow('img_rgb', img_rgb)
cv.waitKey(0)