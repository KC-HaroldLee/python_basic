import sys

try :
    1 / 0
except :
    exc_class, val, tb_ob = sys.exc_info()

    print(exc_class) # <class 'ZeroDivisionError'>
    print(val) # division by zero
    print(tb_ob) # <traceback object at 0x0000026936AFE7C0>

    print(dir(tb_ob)) # ['tb_frame', 'tb_lasti', 'tb_lineno', 'tb_next']
    print(tb_ob.tb_lineno) # 4