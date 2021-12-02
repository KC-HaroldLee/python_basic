# compile(pattern [,flag])
# 정규표현식 객체를 반환!

import re
regex = '[aeiou]'
print(re.compile(regex)) # re.compile('[aeiou]')
print(type(re.compile(regex))) # <class 're.Pattern'>

