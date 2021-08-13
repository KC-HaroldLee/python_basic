def test (*args):
    # return(type(args))
    i=0
    items = list(args)
    print(type(items))
    # for item in items:
    while i<len(items):
        print(items[i])
        i = i + 1

test('안녕','하하',123,True)
