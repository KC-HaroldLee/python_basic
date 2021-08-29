import os

# mkdir(path[, mode]])
# 폴더를 만든다.

name = '\\testfolder'
print(os.getcwd()+name)
bool1 = os.path.exists(os.getcwd()+name)
print(bool1)
if bool1 == False :
    print('없으니 만든다.')
    os.mkdir(os.getcwd()+name)
else :
    print('이미 있습니다.')


print(os.listdir('.'))

# mkdirs(path[, mode]])
# 폴더를 재귀적으로 만든다.