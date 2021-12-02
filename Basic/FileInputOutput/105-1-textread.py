import FilePathTools
filePath = FilePathTools.fileFolder+'/test.txt'
f1 = open(filePath, 'r')

import os
print('파일이 존재', os.path.exists(filePath))
print('파일크기', os.path.getsize(filePath))

print('파일 내용 읽기(1) \n',f1.read())
print('파일 내용 읽기(2) \n',f1.read())

print('어디까지 읽었나', f1.tell())
print('10번째로 돌아갑니다.', f1.seek(10))
print('파일 내용 읽기(3) \n',f1.read())

f1.close() # 잊지말자