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
action.configure(state='disabled') # 이렇게 비활성화

name_typed.focus()

win1.mainloop()