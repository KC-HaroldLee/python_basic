def Raise1() :
    print('hello1')
    raise TypeError
    print('hello2')
def Raise2(a) :
    print('입력한 것은 {0}'.format(a))
    raise ZeroDivisionError(a)

# Raise1()
Raise2('hello')