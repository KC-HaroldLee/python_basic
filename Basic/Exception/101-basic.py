try :
    #<예외 발생가능성이 있는 문장>
    pass
except LookupError : #<예외종류1> 
    #<예외 처리문장1>
    pass
except TypeError : #<예외종류2>
    #<예외 처리문장2>
    pass
except ZeroDivisionError as a : #<예외종류3> as <인자>
    pass

else :
    #예외가 발생하지 않은 경우
    pass
finally :
    # 아무튼 마지막에 실행
    pass