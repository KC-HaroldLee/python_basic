def __init__ (self, inputTuple=tuple) :
    self.inputTuple = inputTuple

def ridOuterDimTuple (inputTuple=tuple) :
    listTmp = list(inputTuple)
    del(listTmp[0])
    return (tuple(listTmp))

def ridInnerDimTuple (inputTuple=tuple) :
    listTmp = list(inputTuple)
    del(listTmp[len(listTmp)-1])
    return (tuple(listTmp))