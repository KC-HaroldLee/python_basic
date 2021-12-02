#split()
#구분자로 string을 분리해 list로 출력

import re
str1 = 'hello hello hello how low'
regex = '[aeiou]'

print(re.split(regex, str1)) # ['h', 'll', ' h', 'll', ' h', 'll', ' h', 'w l', 'w']