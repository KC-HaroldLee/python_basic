def Fibonacci():
    # a = 0
    # b = 1
    a, b = 0, 1
    while 1:
        yield a
        # a = b
        # b = a+b
        a, b =b, a+b

for i, ret in enumerate(Fibonacci()):
    if i < 20: print(i, ret)
    else: break
