import numpy as np
from PIL import Image
import cv2

img = Image.open('cccc.tiff')
img_arr = np.array(img, dtype=np.uint8)
print(img_arr.shape)

img_rgb = img.convert("RGB")
img_rgb_arr = np.array(img_rgb, dtype=np.uint8)
print(img_rgb_arr.shape)
print(type(img_rgb_arr))
cv2.namedWindow('viewer-1')
cv2.imshow('viewer-1', img_rgb_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()