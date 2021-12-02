class NegativeDisionError(Exception) : 
    def __init__(self, value):
        self.value = value
    
def PositiveDivide(a, b) :
    if(b < 0) :
        raise NegativeDisionError(b)
    result = a / b
    return '{0} / {1} = {2}'.format(str(a),str(b),result)

try :
    ret = PositiveDivide(10, 2)
    print(ret)
except NegativeDisionError as e :
    print('!에러! 두번째 인자는 양수이어야해요', e.value)

except ZeroDivisionError as e :
    e.value = ret.args[1]
    print('0으로 나누지 못해요. 피제수는', e.value) #e.value 작동 안함


# except : #그외의 경우
#     print('에... 아무튼 에러입니다.')
else :
    print('계산 잘되었죠?')