import FilePathTools
f1 = open(FilePathTools.fileFolder+'/music.mp3', 'w')
print(f1)
f1.write(open(FilePathTools.fileFolder+'/music.mp3', 'w'))