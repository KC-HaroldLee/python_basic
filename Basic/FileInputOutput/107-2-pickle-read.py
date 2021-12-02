import FilePathTools
colors2 = []
print('colors2 = ',colors2)
f1 = open(FilePathTools.fileFolder+'/colors.list', 'rb')

import pickle
colors2 = pickle.load(f1)
print('colors2 = ',colors2)
f1.close()