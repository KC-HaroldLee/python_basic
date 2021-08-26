#연산자 중복 계속
class GString :
    def __init__(self, init=None):
        self.content = init
    def __sub__(self, str) :
        for item in str :
            self.content = self.content.replace(item, 11)
        return GString(self.content)
    
    def __abs__(self) :
        return GString(self.content.upper())

    def __Print__(self) :
        print(self.content)

g = GString("ABCDEFGabcdef")
g -= "df" "-"
g.Print()
g = abs(g)
g.Print()