L =[10,25,30]
def GetBiggerThan20(i):
    return i > 20

NewL = list(filter(GetBiggerThan20, L))
print(NewL)
