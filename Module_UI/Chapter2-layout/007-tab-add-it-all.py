## 다시 기억을 더듬으며 작성한다.

from ast import copy_location
import tkinter as tk
from tkinter import ttk

#########################
## 대빵인 Tk
#########################

win1 = tk.Tk()
win1.title('Py Gui')


#########################
## 탭 만들기
#########################

tabControl = ttk.Notebook(win1)

tab1 = ttk.Frame(tabControl) # ~에 속한다?
tabControl.add(tab1, text='탭1') #에 넣는다. (왜 동시에 하지 않을까)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='탭2')

# 다 만들면 팩을 한다.
tabControl.pack(expand=1, fill='both') # 보이게 한다.


#########################
## 레이블 프레임 만들기(마이티)
#########################

mighty1 = ttk.LabelFrame(tab1, text='1st mighty')
mighty1.grid(column=0, row=0, padx=8, pady=4) # 패드 안넣으면 진짜 몬생김

# 바로 만들어 보기
ttk.Label(mighty1, text='이름을 입력해라').grid(column=0, row=0)
# a_label = ttk.Label(mighty1, text='이름을 입력하세요')
# a_label.grid(column=0, row=0, sticky='W')

# name = tk.StringVar() # 자바스럽게 생각하자
# name_entered = ttk.Entry(mighty1, width= 15, textvariable=name)
name_entered = ttk.Entry(mighty1, width= 15, textvariable=tk.StringVar())
name_entered.grid(column=0, row=1, sticky='W')

# action1과 연결 된 함수 만들기
def click_me() :
    # action1.configure(text='Hello ' + name.get(), width=500)
    action1.configure(text='Hello ' + name_entered.get() + ' ' + number_chosen.get()) # 이거도 된다
    # action1.configure(text='Hello ' + name.get())

action1 = ttk.Button(mighty1, text='Click Me!', width=12, command=click_me)
action1.grid(column=2, row=1)

# 바로 만들어 보기
ttk.Label(mighty1, text='숫자를 선택해라').grid(column=1, row=0)
# b_label = ttk.Label(mighty1, text='숫자를 선택하세요')
# b_label.grid(column=1, row=0)

# number = tk.StringVar()
# number_chosen = ttk.Combobox(mighty1, width=15, textvariable=number)
number_chosen = ttk.Combobox(mighty1, width=15, textvariable=tk.StringVar())
number_chosen['values'] = (1,2,4,42,100) #
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty1, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty1, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty1, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)           

# GUI Callback function 
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 



win1.mainloop()
