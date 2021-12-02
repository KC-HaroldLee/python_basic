import sys
print('argv 사이즈 : ', len(sys.argv))

for i , arg in enumerate(sys.argv) :
    print ('i = {0}, arg = {1}'.format(i, arg))