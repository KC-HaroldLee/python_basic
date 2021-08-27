import FilePath
f1 = open(FilePath.fileFolder+'/music.mp3', 'rb')
print(f1)
print(f1.read())

f1.close()