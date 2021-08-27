# Match객체를 엇다 쓸까
# match(), search()의 수행결과로 생성된다

import re
telChecker = re.compile('(\d{2,3})-(\d{3,4})-(\d{4})')

tel1 = '010-1234-5678'
m1 = re.match(telChecker, tel1) 
print(m1) # <re.Match object; span=(0, 13), match='010-1234-5678'>

# group() - str형태 (인덱스의 숫자가...)
print(m1.group()) # 010-1234-5678
print(m1.group(0)) # 010-1234-5678
print(m1.group(1)) # 010
print(m1.group(2)) # 1234
print(m1.group(3)) # 5678
print(m1.group(1, 3)) # ('010', '5678')


# groups() - 이건 tuple
print(m1.groups()) # ('010', '1234', '5678')

# groupdict() - dictionary
print(m1.groupdict()) # {} ...흠

# start([group]) cf. end([group])
print(m1.start()) # 0
print(m1.start(1)) # 0 각 문자열 시작 위치다
print(m1.start(2)) # 4
print(m1.start(3)) # 9
# print(m1.start(4)) # IndexError: no such group

# 그 외 이용할만한 반환값들
print(m1.pos) # 0
print(m1.endpos) # 13
print(m1.lastindex) # 3
print(m1.lastgroup) # None
print(m1.string) # 010-1234-5678



