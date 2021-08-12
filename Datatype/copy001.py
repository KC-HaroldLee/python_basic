a = [1, 2, 3]
b = a
print(a)
print(b)

a[0] = 99
print(id(a))
print(id(b))
