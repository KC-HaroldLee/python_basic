import FilePath
f1 = open(FilePath.fileFolder+'/music.mp3', 'w')
print(f1)
f1.write(open(FilePath.fileFolder+'/music.mp3', 'w'))