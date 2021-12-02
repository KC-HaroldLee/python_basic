import cv2 as cv
import os

os.chdir('15-Image segmentation\\images')
img_color = cv.imread("test.jpg", cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY) 
img_edge = cv.Canny(img_gray, 50, 150)
img_edge = cv.bitwise_not(img_edge)
cv.imshow("result", img_edge )
cv.waitKey(0) 

contours = cv.findContours(img_edge.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_edge, contours[0], -1, (0, 0, 0), 1)
cv.imshow("result", img_edge )
cv.waitKey(0) 


nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(img_edge)

for i in range(nlabels):

    # 배경을 제외 시킨다.
    if i < 1:
        continue

    # 구역을 뽑아낸다.
    area = stats[i, cv.CC_STAT_AREA]

    # 도심을 뽑아낸다.
    center_x = int(centroids[i, 0])
    center_y = int(centroids[i, 1]) 

    # 외각 사각형의 꼭지점을 구한다.
    left = stats[i, cv.CC_STAT_LEFT]
    top = stats[i, cv.CC_STAT_TOP]
    width = stats[i, cv.CC_STAT_WIDTH]
    height = stats[i, cv.CC_STAT_HEIGHT]


 
    if area > 50: 
        cv.rectangle(img_color, (left, top), (left + width, top + height), 
                (0, 0, 255), 1)

        cv.circle(img_color, (center_x, center_y), 5, (255, 0, 0), 1)
 
        cv.putText(img_color, str(i), (left + 20, top + 20), 
                cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)


cv.imshow("result", img_color)
cv.waitKey(0)