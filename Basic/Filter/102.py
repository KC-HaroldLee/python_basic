L =[10,25,30]

def GetBiggerThan20(i):
    return i > 20

IterL =filter(GetBiggerThan20, L)
for i in IterL:
    print("Item: {0}".format(i))
