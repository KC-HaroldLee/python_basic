import numpy as np
arr1 = np.arange(10).reshape(2, 5)

detach1 = np.split(arr1, 2, axis = 0)
detach2 = np.split(arr1, [2 ,3], axis = 1)

print(detach1) # [array([[0, 1, 2, 3, 4]]), array([[5, 6, 7, 8, 9]])]
print(detach2) 
# [array([[0, 1],
#        [5, 6]]), array([[2],
#        [7]]), array([[3, 4],
#        [8, 9]])]

count = 0
for i in detach2 :
    print(count, '번째', i)
    count = count+1

# 0 번째 [[0 1]
#  [5 6]]
# 1 번째 [[2]
#  [7]]
# 2 번째 [[3 4]
#  [8 9]]

# [array([[0, 1],[5, 6]]), array([[2],[7]]), array([[3, 4],[8, 9]])]