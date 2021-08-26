# 세가지 도움이 되는 인자
# sep 구분자
# end 끝라인
# file 출력

import sys
print("welcome to", "python", sep="~", end="(end of print)")
print("welcome to", "python", sep="~", end="(end of print)", file=sys.stderr)
