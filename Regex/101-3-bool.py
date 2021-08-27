import re
regex = '[0-9]th'
str1 = '4th'
str2 = '    4th'

print(bool(re.match(regex, str2))) # False
print(bool(re.search(regex, str2))) # True