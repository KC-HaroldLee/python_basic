import simpleset
# print(dir(simpleset ,listC)) # 제대로 import되었는지 확인

listA = [1,2,3,4] 
listB = [2,3,4,5,6,7]
listC = ['A', 7,8,9]

print(simpleset.union(listA, listB))
print(simpleset.intersect(listA, listB))
print(simpleset.difference(listA, listB))

print(simpleset.union(listA, listB ,listC))
print(simpleset.intersect(listA, listB ,listC))
print(simpleset.difference(listA, listB ,listC))
