# 모듈 만들기
from functools import * # reduce를 가지고 있는 functools이다.

def intersect(*args) :
    "교집합"
    return reduce(__intersectSC, args)

def __intersectSC(list1, list2) :
    setList = []
    for x in list1:
        if x in list2 :
            setList.append(x)
    return setList

def union(*args) :
    "합집합"
    setList = []
    for item in args :
        for x in item :
            if x not in setList :
                setList.append(x)
    return setList

def difference(*args) :
    "차집합"
    setList = []
    intersectSet = intersect(*args)
    unionSet = union(*args)
    for x in unionSet :
        if x not in intersectSet :
            setList.append(x)
    return setList
       