import tkinter as tk
from tkinter import ttk

win1 = tk.Tk()
win1.title('text_input_test') 
win1.resizable(width=True, height=False)

# 바로 만들 수 있다. 그리고 뒤에 뭔갈 더 설정 할 수 있다.
# a_label = ttk.Label(win1, text='A Lable')
ttk.Label(win1, text='type your name').grid(column=0,row=0) 

# 변수를 먼저 설정해주고
# 인스턴스서 참고 할 수 있게 인자에 설정하여
# 변수를 할당해준다.

name = tk.StringVar()

name_typed = ttk.Entry(win1, width=12, textvariable=name)
name_typed.grid(column=0, row=1)

def click_me() :
    action.configure(text='Hello ' + name.get())


action = ttk.Button(win1, text='클릭 미', command=click_me) # 인자는 어디?
action.grid(column=1, row=1)

# 초기변수는 비어있는가? ~ 네 '' 입니다
str1 = ''
name2 = tk.StringVar()
int1 = tk.IntVar() # 이런것도 있다네
# print(name) # PY_VAR0
print(bool(str1==name2.get())) # True

win1.mainloop()