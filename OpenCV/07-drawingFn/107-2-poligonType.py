import cv2 as cv
import numpy as np

img = np.zeros((640, 640, 3), np.uint8)

r = (0, 0, 255)
g = (0, 255, 0)
y = (0, 255, 255)

thickness = 2

# 오각형
pts = np.array([[315,50],[570,240],[475,550],[150,550],[50,240]], np.int32)
pts = pts.reshape((-1,1,2)) #?
cv.polylines(img, [pts], False, r, thickness)

print(type(pts)) # <class 'numpy.ndarray'>

# 대괄호가 두개나 된다.
# 심지어 쉼표도 사라짐
print(pts[0]) # [[315  50]]
print(pts[1]) # [[570 240]]
print(pts[2]) # [[475 550]] 

print(type(pts[0])) # <class 'numpy.ndarray'>""

# 대괄호 하나를 빼내었지만
# 타입은 같다
print(pts[0][0]) # [315  50]
print(type(pts[0][0])) # <class 'numpy.ndarray'>

# 3중이다.
# 타입은 numpy.int32다.
print(pts[0][0][0]) # 315
print(pts[0][0][1]) # 50
print(type(pts[0][0][0])) # <class 'numpy.int32'>

a = type(pts[0][0][0])
# print(a + 1) # TypeError: unsupported operand type(s) for +: 'type' and 'int'
print(int(a) + 1) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'type'



