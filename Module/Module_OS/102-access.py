import os
print(os.access('.', os.F_OK)) # True (존재)
print(os.access('C:\\', os.W_OK)) # True (쓰기 가능)
print(os.access('C:\\', os.W_OK & os.F_OK)) # and
print(os.access('C:\\', os.W_OK | os.F_OK)) # and

# F_OK 존재 여부 
# R_OK 읽기 여부
# W_OK 쓰기 여부
# X_OK 실행 여부