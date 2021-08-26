#예외를 발생시키는데 쓰인다고?
# assert <조건식>, <관련데이터>

def nirvana(x):
    print('type of x = ', type(x))
    assert type(x) == int, 'int이어야합니다'
    return x * 10

n1 = nirvana(1)
print(n1)
n2 = nirvana(int('5'))
print(n2)
n3 = nirvana('가')
print(n3)