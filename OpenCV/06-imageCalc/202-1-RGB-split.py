import cv2 as cv
import os 

os.chdir('06-imageCalc\\images')

src = cv.imread('dal (1).jpg', cv.IMREAD_REDUCED_COLOR_2)
# src_addAlpha = cv.cvtColor(src, cv.COLOR_BGR2RGBA)
src_addAlpha = cv.cvtColor(src, cv.COLOR_RGB2RGBA)

cv.imshow('src_addAlpha', src_addAlpha) 
cv.waitKey(0)

mv = cv.split(src) # 채널별로 분리된다.
print(type(mv)) # <class 'list'>
print(len(mv)) # 3

mv_addAlpha = cv.split(src_addAlpha) # 채널별로 분리된다.
print(type(mv_addAlpha)) # <class 'list'>
print(len(mv_addAlpha)) # 4

cv.imshow('mv_addAlpha[0]', mv_addAlpha[0]) 
cv.imshow('mv_addAlpha[1]', mv_addAlpha[1]) 
cv.imshow('mv_addAlpha[2]', mv_addAlpha[2]) 
cv.imshow('mv_addAlpha[3]', mv_addAlpha[3]) 
cv.waitKey(0)