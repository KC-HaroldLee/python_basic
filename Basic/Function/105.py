def intersect(prelist, postlist):
    retList = [] # 일단 빈 list를 만든다.
    for x in prelist :
        if x in postlist and not x in retList :
            retList.append(x)
    return retList

list1 = "NIRVANA"
list2 = "NEWFOUNDGLORY"

print(intersect(list1, list2)) # return ['N', 'R']
print(intersect(list1, ['N', 'I', 'V'])) # return ['N', 'I', 'V']

