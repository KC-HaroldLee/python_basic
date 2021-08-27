# sub(pattern, repl, string[, count])
# subn(pattern, repl, string[, count]) - 튜플로 반환

import re
str1 = 'hello hello hello how low'
regex = '[aeiou]'

print(re.sub(regex, 'V', str1)) # hVllV hVllV hVllV hVw lVw
print(re.subn(regex, 'V', str1)) # ('hVllV hVllV hVllV hVw lVw', 8)