# isdecimal()
# 10진수로 구성되어 있는지
u = '2580'
v = '\u0669' # ' '
w = '\u00bc' # ¼
print(u.isdecimal()) # True
print(v.isdecimal()) # True (의외군)
print(w.isdecimal()) # False


# isnumeric()
# 숫자로 구성되어 있는지
x = '123'
y = '\u00bc'
z = '\u00bc'

print(x.isnumeric()) # True
print(y.isdecimal()) # False
print(z.isnumeric()) # True

# isidenttifier()
# 식별자 생략

# isprintable()
# print 가능한지

aa = 'test'
ab = '\u0014'
ac = ' '
ad = ''
print(aa.isprintable()) # True
print(ab.isprintable()) # False
print(ac.isprintable()) # True
print(ad.isprintable()) # True

print(aa)
print(ab) # 아무것도 안 나옴(진짜 없음)
print(ac) # 아무것도 안 나옴(근데 있는거임)
print(ad) # 아무것도 안 나옴('')

# join() ㅋㅋ
ae = '.'
af = '아시겠어요?'
print(ae.join(af)) # '아.시.겠.어.요.?'

#lower(), upper()

#lstrip([chars])
# 문자열의 왼쪽을 잘라낸다.
ag = '\t python'
print(ag.lstrip()) # 'python'

ah = '<<<python is powerful>>>'
print(ah.lstrip('<')) # 'python is powerful>>>'

#rstrip
print(ah.rstrip('>')) # '<<<python is powerful'

# maketrans()
# 모르겠어서 생략

# partition(seperator)
# 세 조각으로 쪼갠다
ai = '나는 나비'
print(ai.partition('는')) # ('나', '는', ' 나비')
print(type(ai.partition('는')))  # <class 'tuple'>

# replace(old, new, [count])
aj = 'QQQQQQQQQQQQQQQQQQQ'
print(aj.replace('Q', 'I', 10)) # IIIIIIIIIIQQQQQQQQQ

# 반대시리즈

# rfind()
# rindex()
# rpartition()
# rsplit
# rstrip 등등

# split(seperator, [maxsplit])
# 문자열을 seperator로 분리한다. 
ak = 'apple and banana and orange and papaya'
print(ak.split()) # ['apple', 'and', 'banana', 'and', 'orange', 'and', 'papaya']
print(ak.split('and')) # ['apple ', ' banana ', ' orange ', ' papaya']

# splitlines([keep])
al = 'python\nis\npowerful'
print(al.splitlines()) # ['python', 'is', 'powerful'] (이게 기본이여?)
print(al.splitlines(True)) # ['python\n', 'is\n', 'powerful']
print(al.splitlines(False)) # ['python', 'is', 'powerful']

# strip([chars])
# 흠 인자 모양이 특이하다
# 그냥 싫은거 다 자를수 있다...ㅋㅋㅋ
am = 'kkk안녕하세요yyy'
print(am.strip('k')) # 안녕하세요yyy
print(am.strip('ky')) # 안녕하세요
print(am.strip('y')) # kkk안녕하세요
print(am.strip('ky요')) # 안녕하세

# swapcase()
# lower를 upper로, upper를 lower로
an = 'Aa'
print(an.swapcase())

#title()
#타이틀 왜이리 좋아해..
ao = 'smells like teen spirit'
print(ao.title()) # Smells Like Teen Spirit