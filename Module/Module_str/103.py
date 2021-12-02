# find(keyword, [start, [end]])
# 첫번째 인덱스만 확인한다.

g = 'NIRVANA'
print(g.find('N')) # 0
print(g.find('NI')) # 0
print(g.find('A')) # 4
print(g.find('A', 4)) # 4
print(g.find('A', 5)) # 6
print(g.find('Z')) # -1

# index(keyword, [start, [end]])
# (-1)은 결국 '끝'까지라는것을 의미 End of 머시기

print(g.index('A', 0 , -1)) # 4
try :
    print(g.index('Z')) # ValueError: substring not found
except ValueError : 
    print('그 글씨는 없다네')
    pass


# isalnum()
# 알파벳과 숫자로 구성되어 있는가?(공백도 안됨)

h = 'SR71 - 1985'
i = 'SR71 1985'
j = 'SR711985'
print(h.isalnum()) # False
print(i.isalnum()) # False
print(j.isalnum()) # True


# isalpha()
# 알파벳만

k = 'kklastchnpd'
l = 'kk4ever'
print(k.isalpha()) # True
print(l.isalpha()) # False


# islower(), isupper()
print(k.islower()) # True
print(k.isupper()) # False


# isspace()
m = '     '
n = '\t'
o = '\n'
p = '' # 공백이 없는 거니까

print(m.isspace()) # True
print(n.isspace()) # True
print(o.isspace()) # True
print(p.isspace()) # False

q = '안녕하세요? 저는 이석현입니다'
if(q.isspace()==False) :
    print('공백을 제거합니다', q)
    q = q.replace(' ', '') # 공백 제거하는 메소드는 많음
    print('변경후 = ', q)

# istitle()
# ?$?!? 타이틀 스타일 이라고!?

r = 'Nirvana is Best'
s = 'Nirvana Is Best'
t = 'NIRVANA IS BEST'

print(r.istitle()) # False
print(s.istitle()) # True
print(t.istitle()) # False