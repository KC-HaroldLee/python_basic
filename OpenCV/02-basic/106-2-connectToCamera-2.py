import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

print(type(cap))
cap.isOpened()