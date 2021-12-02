import numpy as np

a = np.array([1,2,3,4])

for i in range(a.size) :
    print(a[i])

    
for i in a.flat :
    print(i)

b = np.array([[1,2],[3,4]])
# for i in range(b.size) : 
    # print(b[i]) # IndexError:
for i in b.flat :
    print(i)




