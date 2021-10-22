import tkinter as tk
from tkinter import ttk

win1 = tk.Tk()
win1.title('text_input_test') 
win1.resizable(width=True, height=False)

def click_me() :
    action.configure(text='Hello ' + name.get() + ' in ' + country.get())

ttk.Label(win1, text='type your name').grid(column=0,row=0) 
ttk.Label(win1, text='choose a country').grid(column=0, row=1)

name = tk.StringVar()
name_typed = ttk.Entry(win1, width=12, textvariable=name)
name_typed.grid(column=0, row=1)

country = tk.StringVar()
country_selected = ttk.Combobox(win1, width=20, textvariable=country, state='readonly')
country_selected['values'] = ('KR', 'US', 'AU', 'JP', 'FR')
country_selected.grid(column=1, row=1)
country_selected.current(0)

action = ttk.Button(win1, text='클릭 미', command=click_me)
action.grid(column=2, row=1)

# 체크 박스들
# 일단 만드는데 왜 Int일까
chVarDis = tk.IntVar()
chVarUn = tk.IntVar()
chVarEn = tk.IntVar()



name_typed.focus()

win1.mainloop()