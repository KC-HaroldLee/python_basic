#연산자 중복 정의
class GString :
    def __init__(self, init=None) : # 생성자라는데... 왜 None일까
        self.content = init # 벌써 None?
    
    def __sub__ (self, str) :
        for item in str :
            self.content = self.content.replace(item,'')
        return GString(self.content)
    
    def Remove(self, str) :
        return self.__sub__(str)


g = GString("ABCDEFabcdefg")
print(g + "apple")