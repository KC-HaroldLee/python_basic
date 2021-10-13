import tkinter as tk
from tkinter import ttk # 뭔가 더 있다.

win1 = tk.Tk() # 나름 생성하는군
win1.title('title-bar-hahahahaha') # 타이툴 붙이고
win1.resizable(width=True, height=False) # 크기 조정 방지 
# ttk.Label(win1, text='Label-1').grid(column=0, row=0)

a_label = ttk.Label(win1, text='A Lable')
a_label.grid(column=0, row=0)

def click_me() :
    action.configure(text='클릭해주셨군요')
    a_label.configure(foreground='red')
    a_label.configure(text='A red Label')
    

action = ttk.Button(win1, text='클릭 미', command=click_me) # 인자는 어디?
action.grid(column=1, row=0)


win1.mainloop() # 약간 메인 함수 느낌 # 루프는 콜백 느낌이지만 그렇지는 않은 듯 하다.