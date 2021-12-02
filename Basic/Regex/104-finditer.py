# finditer()
# 이터레이터로 반환

import re
str1 = 'hello hello hello how low'
regex = '[aeiou]'

it = re.finditer(regex, str1) 
print(type(re.finditer(regex, str1))) # <class 'callable_iterator'> 

print(it) # <callable_iterator object at 0x0000018A54D2D040>

print(next(it)) # <re.Match object; span=(1, 2), match='e'>
print(next(it)) # <re.Match object; span=(4, 5), match='o'>
print(next(it)) # <re.Match object; span=(7, 8), match='e'>
print(next(it)) # <re.Match object; span=(10, 11), match='o'>
print(next(it)) # <re.Match object; span=(13, 14), match='e'>