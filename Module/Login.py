members = ['nirvana','greenday','goldfinger','offspring']

def checkId(_id):
    for member in members:
        if _id == member:
            return True
    return False
