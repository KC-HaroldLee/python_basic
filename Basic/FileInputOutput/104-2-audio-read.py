import FilePathTools
f1 = open(FilePathTools.fileFolder+'/music.mp3', 'rb')
print(f1)
print(f1.read())

f1.close()