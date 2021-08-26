import FilePath
f = open(FilePath.fileFolderPath+'test.txt', 'w') #음 문자열 형태로... 그렇군
print(f) # open의 정보를 알려준다.
print(f.write('hello hello\nhow low')) # 글자수를 반환한다.

print('close 전', f.closed)
f.close()
print('close 후', f.closed)