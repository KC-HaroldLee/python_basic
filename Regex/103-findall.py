# findall()

import re
str1 = 'hello hello hello how low'
regex = '[aeiou]'

print(re.findall(regex, str1)) # ['e', 'o', 'e', 'o', 'e', 'o', 'o', 'o']