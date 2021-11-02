import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

from tkinter import messagebox as msg
from tkinter.constants import COMMAND

win = tk.Tk()   

win.title("Python GUI")  

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both")

mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')

def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())

name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')


action = ttk.Button(mighty, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)



scrol_w  = 30
scrol_h  =  3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, sticky='WE', columnspan=3)                    




mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)


chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)                     


def checkCallback(*ignoredArgs):
    
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 


chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   



colors = ["Blue", "Gold", "Red"]   




def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=colors[0])  
    elif radSel == 1: win.configure(background=colors[1])  
    elif radSel == 2: win.configure(background=colors[2])


radVar = tk.IntVar()


radVar.set(99)                                 
 

for col in range(3):                             
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=6, sticky=tk.W)             


buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=7)        
 

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)


def _quit():
    win.quit()
    win.destroy()
    exit() 
    

menu_bar = Menu(win)
win.config(menu=menu_bar)


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)


# 메시지 박스 만들기

def _help_msgBox ():
    msg.showinfo(title='쇼 info', message='!info! : 인포입니다.') # 하나 하나 기다려준다... 착하구나...
    msg.showerror(title='쇼 error', message='!error! : 에러 일까요?.')
    msg.showwarning(title='쇼 warn', message='!warn"ing"! : 경고입니다.')
    msg.askyesno(title='messagebox.askyesno()', message='거참 내부 모듈이름 간단하면서도 멋 없네 그렇지 않아요?')
    msg.askokcancel(title='messagebox.askokcancel()', message='이거 하면 콘솔에 나온다고 하네?')
    msg.askretrycancel(title='messagebox.askretrycancel()', message='뭘 리트라이 할 수 있을까?')
    msg.askyesnocancel(title='messagebox.askyesnocancel()', message='이건 좀 많군요 하지만 분기점은 몰겠지만')
    msg.askquestion(title='messagebox.askquestion()', message='뭘 물어보는 걸까요? 아무튼 이것들은 각각 반환 값이 있다는 것을 이용 할 수 있겠습니다.')
    print(msg.showinfo(title='쇼 info', message='좋아 지금부터 테스트를 해보죠. 콘솔을 띄우고 확인을 눌러봅시다.'))
    print(msg.showerror(title='쇼 error', message='!error! : 에러는 어떤가요?'))
    print(msg.showwarning(title='쇼 warn', message='!warn"ing"! : 경고는 어때요?.'))
    print(msg.askyesno(title='messagebox.askyesno()', message='걱정마세요 지금부터는 버튼 개수 많큼 띄울 겁니다(0)'))
    print(msg.askyesno(title='messagebox.askyesno()', message='걱정마세요 지금부터는 버튼 개수 많큼 띄울 겁니다(1)'))
    print(msg.askokcancel(title='messagebox.askokcancel()', message='재미있기는 한가요?(0)'))
    print(msg.askokcancel(title='messagebox.askokcancel()', message='재미있기는 한가요?(1)'))
    print(msg.askokcancel(title='messagebox.askokcancel()', message='재미있기는 한가요?(2)'))
    print(msg.askretrycancel(title='messagebox.askretrycancel()', message='뭐.. 아직까진 리트라이가 의미가 없죠(0)'))
    print(msg.askretrycancel(title='messagebox.askretrycancel()', message='뭐.. 아직까진 리트라이가 의미가 없죠(1)'))
    print(msg.askyesnocancel(title='messagebox.askyesnocancel()', message='혼잣말을 많이 하는 내가 참 편하군 (0)'))
    print(msg.askyesnocancel(title='messagebox.askyesnocancel()', message='혼잣말을 많이 하는 내가 참 편하군 (1)'))
    print(msg.askyesnocancel(title='messagebox.askyesnocancel()', message='혼잣말을 많이 하는 내가 참 편하군 (2)'))
    print(msg.askquestion(title='messagebox.askquestion()', message='뭘 물어보는 걸까요? 아무튼 이것들은 각각 반환 값이 있다는 것을 이용 할 수 있겠습니다.'))
    print(msg.askquestion(title='messagebox.askquestion()', message='뭘 물어보는 걸까요? 아무튼 이것들은 각각 반환 값이 있다는 것을 이용 할 수 있겠습니다.'))
    print(msg.askquestion(title='messagebox.askquestion()', message='뭘 물어보는 걸까요? 아무튼 이것들은 각각 반환 값이 있다는 것을 이용 할 수 있겠습니다.'))

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_help_msgBox)
menu_bar.add_cascade(label="Help", menu=help_menu)


name_entered.focus()      



win.mainloop()