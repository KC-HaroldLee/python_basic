import numpy as np

tuple1 = (2,3,4,5)

# # 뒤 차원 지우기
# list1 = list(tuple1)  # [2, 3, 4, 5]
# list1.__delitem__(len(list1)-1) # [2, 3, 4]
# print(tuple(list1)) # (2, 3, 4)

# # 앞 차원 지우기
# list2 = list(tuple1) # [2, 3, 4, 5]
# list2.__delitem__(0) # [3, 4, 5]
# print(tuple(list2)) # (3, 4, 5)

import dimTools as dt

tuple2 =(5,6,7,8)
print(type(tuple2))
print(dt.ridInnerDimTuple(tuple2)) # (5, 6, 7)
print(dt.ridOuterDimTuple(tuple2)) # (6, 7, 8)