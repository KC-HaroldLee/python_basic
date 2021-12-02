import FilePathTools
filePath = FilePathTools.fileFolder+'/test.txt'
f1 = open(filePath, 'r')

f1.readline()
print(f1.readline())

f1.seek(0)
print(f1.readlines())
print(type(f1.readlines()))

f1.close() # 잊지말자