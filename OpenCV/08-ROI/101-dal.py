import cv2 as cv
import os

os.chdir("08-ROI\\videos")
video = cv.VideoCapture('dal.mp4')

while True :

    ret, img_frame = video.read()
    # img_frame = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)
    ret, img_frame = cv.threshold(img_frame, 127, 255, cv.THRESH_BINARY)
    cv.imshow('video', img_frame)
    key = cv.waitKey(25)

    if key == 30 :
        break