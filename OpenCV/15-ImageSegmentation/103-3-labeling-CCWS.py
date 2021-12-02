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

print(type(nlabels)) # <class 'int'>
print('nlabels: \n', nlabels) # 10

print(type(labels)) # <class 'numpy.ndarray'>
print('labels : \n', labels) 
for i in labels :
    # for j in i :
    #     print(labels[i][j])
    print('--------------')
    print(labels[i])


print(type(stats)) # <class 'numpy.ndarray'>
print('stats : \n', stats)
# [[     0      0    500    500  10410]
#  [     1      1    498    498 223675]
#  [    63     59     85     87   2032]
#  [   237     88     69     69   2086]
#  [   326    169     89     89   2003]
#  [   146    194     85     84   2016]
#  [    61    275     68     67   1887]
#  [   244    274     90     90   2029]
#  [   364    370     90     89   2018]
#  [   183    378     83     72   1844]]

print(type(centroids)) # <class 'numpy.ndarray'>
print('centroids : \n', centroids)
#  [[244.83967339 260.44947166]
#  [250.06848329 248.07113893]
#  [104.34301181 102.09350394]
#  [270.33413231 121.93384468]
#  [368.92361458 212.78931603]
#  [187.5952381  234.56051587]
#  [ 92.35983042 305.95760466]
#  [289.         318.44553967]
#  [408.34638256 414.05946482]
#  [224.70498915 410.23318872]]