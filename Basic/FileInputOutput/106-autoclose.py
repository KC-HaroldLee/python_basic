import FilePathTools
with open(FilePathTools.fileFolder+'/test.txt') as f1 :
    print(f1.readlines())
    print(f1.closed)

print(f1.closed)