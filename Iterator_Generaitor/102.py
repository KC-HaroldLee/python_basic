s = 'abc'
it = iter(s)
print(it)

i = 0
while i < len(s):
    print(next(it))
    i = i + 1
