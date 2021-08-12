import copy
a = [1, 2, 3]
b = copy.deepcopy(a)

a[0] = 99
print(id(a))
print(id(b))
print(a)
print(b)
