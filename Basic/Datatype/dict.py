d1 = dict(apple = "red", banana="yellow", orange="orange")
# print(d1)
# print(d1["banana"])

for 키, 밸류 in d1.items():
    print(키, 밸류)

for i in d1.values():
    print(i)

for i in d1.keys():
    print(i)

for i in d1.items():
    print(i)


d2 = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
print(d2)
print(d2["banana"])

d2["orange"] = "hwang"
print(d2)
