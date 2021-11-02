import tkinter as tk
from tkinter import ttk

win1 = tk.Tk()
win1.title('text_input_test') 
win1.resizable(width=True, height=False)

ttk.Label(win1, text='type your name').grid(column=0,row=0) 

name = tk.StringVar()
name_typed = ttk.Entry(win1, width=12, textvariable=name)
name_typed.grid(column=0, row=1)

def click_me() :
    action.configure(text='Hello ' + name.get())


action = ttk.Button(win1, text='클릭 미', command=click_me)
action.grid(column=1, row=1)

name_typed.focus() # 바로 포커스 # 아 마우스커서가 아니라 텍스트 입력 커서가 간다고...

win1.mainloop()