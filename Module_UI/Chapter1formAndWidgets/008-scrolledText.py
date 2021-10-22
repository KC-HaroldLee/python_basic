import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

### 색상을 저장한 전역변수
COLOR1 ="Blue"
COLOR2 ="Gold"
COLOR3 ="Red"

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


#########################
#  체크박스 만들기
#########################
chVarDis = tk.IntVar()
chVarUn = tk.IntVar()
chVarEn = tk.IntVar()

# chVarDis
check1 = tk.Checkbutton(win1, text = 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 4, sticky = tk.W)

# chVarUn
check2 = tk.Checkbutton(win1, text = 'UnChecked', variable = chVarUn)
check2.deselect()
check2.grid(column = 1, row = 4, sticky = tk.W)

# chVarEn
check3 = tk.Checkbutton(win1, text = 'Enabled', variable= chVarEn)
check3.select()
check3.grid(column = 2, row = 4, sticky = tk.W)


#########################
#  라디오 버튼 만들기
#########################

def radio_callback() :
    radioSelect = radioVar.get()
    print('radio_callback() 호출')
    print('radioSelect : ', radioSelect)
    if radioSelect == 1 :
        win1.configure(background = COLOR1)
    elif radioSelect == 2 :
        win1.configure(background = COLOR2)
    elif radioSelect == 3 :
        win1.configure(background = COLOR3)


radioVar = tk.IntVar()

radio1 = tk.Radiobutton(win1, text = 'Color1', variable = radioVar, value = 1, command = radio_callback)
radio1.grid(column = 0, row = 5, sticky=tk.W, columnspan = 3)
radio2 = tk.Radiobutton(win1, text = 'Color2', variable = radioVar, value = 2, command = radio_callback)
radio2.grid(column = 1, row = 5, sticky=tk.W, columnspan = 3)
radio3 = tk.Radiobutton(win1, text = 'Color3', variable = radioVar, value = 3, command = radio_callback)
radio3.grid(column = 2, row = 5, sticky=tk.W, columnspan = 3)

#########################
#  스크롤 텍스트 위젯
#########################

# from tkinter import scrolledtext

scroll_w = 30
scroll_h = 3

# scroll = scrolledtext.ScrolledText(win1, width = scroll_w, height = scroll_h, wrap = tk.WORD)
scroll = scrolledtext.ScrolledText(win1, width = scroll_w, height = scroll_h, wrap = tk.CHAR) # tk.CHAR도 있다. 근데 차이는 모르겠다.
scroll.grid(column = 1, row=6, sticky = tk.E) # E가 안먹혀

name_typed.focus()
 
win1.mainloop()