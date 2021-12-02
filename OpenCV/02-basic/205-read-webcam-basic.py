import cv2 as cv

def listOfCap ():
    index = 0
    arr = []
    while True:
        cap = cv.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

print('listOfCap : {0}'.format(listOfCap()))

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)
cv.namedWindow('cam')

while(True) :
    ret, frame = webcam.read()
    if ret == True :
        cv.imshow('cam', frame)
        if cv.waitKey(33) == ord('q'):
            break
    else :
        break
        

webcam.realse()
cv.destroyAllWindows()