import re
regex = '[0-9]th'
str1 = '4th'
str2 = 'aaa'
print(re.search(regex, str1)) # <re.Match object; span=(0, 3), match='4th'>
print(re.search(regex, str2)) # None