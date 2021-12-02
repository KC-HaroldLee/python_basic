def abc():
    data = "abc"
    for char in data:
        # return char
        yield char

print(abc)
print(abc())

it = iter(abc())
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
