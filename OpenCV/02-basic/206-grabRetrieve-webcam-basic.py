import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)
# cv.namedWindow('cam')

print(webcam) # <VideoCapture 00000211858E7910>
print(type(webcam)) # <class 'cv2.VideoCapture'>
print(webcam.grab()) # True
print(type(webcam.grab())) # <class 'bool'>

cv.namedWindow('result1')w
# cv.namedWindow('result2')

# while(True) :
if webcam.grab():
    flag, frame = webcam.retrieve()
    if flag :
        print('!그랩성공! flag : {0}'.format(flag))
        cv.imshow('result1', frame)
else :
    print('?그랩실패?')
    # break

cv.waitKey(0)
cv.destroyAllWindows()
        

# webcam.realse()
# cv.destroyAllWindows()