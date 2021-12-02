import cv2 as cv
pointList=[]

startPoint = (-99999999,-999999999)

def mouse_event_on(event, x, y, flags, param) :
    global radius
    global colorList
    global colorIdx
    global startPoint
    global magRange

    if event == cv.EVENT_RBUTTONDOWN :
        pass
        del pointList[len(pointList)-1]
        print('[del] pointList : ', pointList)

    if event == cv.EVENT_LBUTTONDOWN : 
        cv.circle(param, (x, y), outerRadius, outerColor, -1)
        cv.circle(param, (x, y), innerRadius, innerColor, -1)
        cv.imshow('draw', src)
        pointList.append((x, y))
        print('[add] pointList : ', pointList)

        if len(pointList) > 1 :
            for pointIdx in range(len(pointList)) :
                print('pointIdx :' , pointIdx)
                if pointIdx == 0 :
                    pass
                else : 
                    print('draw line {} to {} | {} to {})'.format(pointIdx-1, pointIdx, pointList[pointIdx-1], pointList[pointIdx]))
                    cv.line(src, pointList[pointIdx-1], pointList[pointIdx], outerColor, 6)
                    cv.line(src, pointList[pointIdx-1], pointList[pointIdx], innerColor, 2)
                    cv.imshow('draw', src)
        elif len(pointList) == 1 :
            startPoint = pointList[0]
            print('[set]startPoint : ', startPoint) 

    if len(pointList) > 1 :
        cv.line(src, pointList[len(pointList)-1], (x, y), outerColor, 6)
        cv.line(src, pointList[len(pointList)-1], (x, y), ingColor, 2)
        cv.imshow('draw', src)

    if len(pointList) > 2 : 
        if abs(startPoint[0] - x) < magRange and (startPoint[1] - y) < magRange :
            cv.circle(param, (startPoint[0], startPoint[1]), int(innerRadius*2), innerColor, -1)
            cv.imshow('draw', src)
        else :
            cv.circle(param, (startPoint[0], startPoint[1]), outerRadius, outerColor, -1)
            cv.circle(param, (startPoint[0], startPoint[1]), innerRadius, innerColor, -1)
            cv.imshow('draw', src)

    if len(pointList) > 3 : 
        if abs(pointList[0][0] - pointList[len(pointList)-1][0]) < magRange and (pointList[0][1] - pointList[len(pointList)-1][1]) < magRange :
            cv.setMouseCallback('draw', mouse_event_off, src)
            del pointList[len(pointList)-1]
            print('최종 pointList :', pointList)
    
def mouse_event_off(event, x, y, flags, param) :
    pass

# 그리기 설정들
innerRadius = 4
innerColor = (255,255,255)
outerRadius = 12
outerColor = (0,0,0)
ingColor = (0,0,255)

magRange = 10

src = cv.imread('OpenCV/98-polygon/image/20210922000096_1.jpg')

cv.imshow('draw', src)

while True :
    key = cv.waitKey(1)
    if key == ord('q') : # 종료
        print('창 종료')
        cv.destroyAllWindows()

    if key == ord('w') :
        print('draw 시작')
        cv.setMouseCallback('draw', mouse_event_on, src)

    if key == ord('e') :
        print('draw 종료')
        cv.setMouseCallback('draw', mouse_event_off, src)
        