import numpy as np

arr_origin = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
                    [[101,102,103],[104,105,106],[107,108,109],[110,111,112]]])
print(arr_origin)
# print(arr_origin.ndim) # 3

# print(arr_origin[0])
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# print(arr_origin[0][0])
# [1 2 3]

# print(arr_origin[0][0][0])
# 1

iNo,jNo,kNo = 0, 0, 0
for i in arr_origin :
    for j in i :
        for k in j :
            # print('arr_origin[{0}][{1}][{2}] : '
            print('{0}{1}{2} : ' # 쉬운버전
            .format(iNo, jNo, kNo), k)
            kNo = kNo + 1
        kNo = 0
        jNo = jNo + 1
    jNo = 0
    iNo = iNo + 1


# [[[  1   2   3]
#   [  4   5   6]
#   [  7   8   9]
#   [ 10  11  12]]

#  [[101 102 103]
#   [104 105 106]
#   [107 108 109]
#   [110 111 112]]]


reshapedArrC = np.reshape(arr_origin, (2, -1), order='C')
print(reshapedArrC)
# [[  1   2   3   4   5   6   7   8   9  10  11  12]
#  [101 102 103 104 105 106 107 108 109 110 111 112]]

reshapedArrF = np.reshape(arr_origin, (2, -1), order='F')
print(reshapedArrF)
# [[  1   4   7  10   2   5   8  11   3   6   9  12]
#  [101 104 107 110 102 105 108 111 103 106 109 112]]