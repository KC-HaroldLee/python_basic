import FilePathTools
colors = ['red', 'orange', 'yellow']
f1 = open(FilePathTools.fileFolder+'/colors.list', 'wb')

import pickle
pickle.dump(colors, f1)
f1.close()