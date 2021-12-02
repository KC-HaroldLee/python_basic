import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win1 = tk.Tk()
win1.title('text_input_test') 
win1.resizable(width=True, height=False)

#########################
#  외부 프레임 만들기
#########################
mighty = ttk.LabelFrame(win1, text='mighty Frame')
mighty.grid(column = 0, row = 0, padx = 8, pady = 4)

def click_me() :
    action.configure(text='Hello ' + name.get() + ' in ' + country.get())

ttk.Label(mighty, text='type your name').grid(column=0, row=0, sticky = tk.W)  # 부모 프레임 변경 win1 -> mighty
ttk.Label(mighty, text='choose a country').grid(column=1, row=0, sticky = tk.W) # 부모 프레임 변경 win1 -> mighty

name = tk.StringVar()
name_typed = ttk.Entry(mighty, width=12, textvariable=name) # 부모 프레임 변경 win1 -> mighty
name_typed.grid(column=0, row=1, sticky = tk.W)

country = tk.StringVar()
country_selected = ttk.Combobox(mighty, width=20, textvariable=country, state='readonly') # 부모 프레임 변경 win1 -> mighty
country_selected['values'] = ('KR', 'US', 'AU', 'JP', 'FR')
country_selected.grid(column=1, row=1)
country_selected.current(0)

action = ttk.Button(mighty, text='클릭 미', command=click_me) # 부모 프레임 변경 win1 -> mighty
action.grid(column=2, row=1)


#########################
#  체크박스 만들기
#########################

chVarDis = tk.IntVar()
chVarUn = tk.IntVar()
chVarEn = tk.IntVar()

# chVarDis
check1 = tk.Checkbutton(mighty, text = 'Disabled', variable = chVarDis, state = 'disabled') # 부모 프레임 변경 win1 -> mighty
check1.select()
check1.grid(column = 0, row = 4, sticky = tk.W)

# chVarUn
check2 = tk.Checkbutton(mighty, text = 'UnChecked', variable = chVarUn) # 부모 프레임 변경 win1 -> mighty
check2.deselect()
check2.grid(column = 1, row = 4, sticky = tk.W)

# chVarEn
check3 = tk.Checkbutton(mighty, text = 'Enabled', variable= chVarEn) # 부모 프레임 변경 win1 -> mighty
check3.select()
check3.grid(column = 2, row = 4, sticky = tk.W)


#########################
#  라디오 버튼 만들기
#########################
    #  반복문으로 위젯 추가
    #########################

colors = ['Blue', 'Gold', 'Red']

def radio_callback() :
    radioSelect = radioVar.get()
    print('radio_callback() 호출')
    print('radioSelect : ', radioSelect)
    if radioSelect == 0 :
        mighty.configure(background = colors[0]) # 부모 프레임 변경 win1 -> mighty
    elif radioSelect == 1 :
        mighty.configure(background = colors[1]) # 부모 프레임 변경 win1 -> mighty
    elif radioSelect == 2 :
        mighty.configure(background = colors[2]) # 부모 프레임 변경 win1 -> mighty


radioVar = tk.IntVar()
radioVar.set(99)

for col in range(3) :
    print(col)
    currentRadio = tk.Radiobutton(mighty, text = colors[col], variable = radioVar, value = col, command = radio_callback) # 부모 프레임 변경 win1 -> mighty
    currentRadio.grid(column = col, row = 5, sticky = tk.W)

#########################
#  스크롤 텍스트 위젯
#########################

scroll_w = 40
scroll_h = 3

scroll = scrolledtext.ScrolledText(mighty, width=scroll_w, height=scroll_h, wrap=tk.WORD) # 부모 프레임 변경 win1 -> mighty
scroll.grid(column=0, row = 6, columnspan = 3)

#########################
#  레이아웃 만들기
#########################

buttons_frame = ttk.LabelFrame(mighty, text = '  new lable!!  ')
buttons_frame.grid(column = 0, row = 7, columnspan = 2, sticky = tk.W)

ttk.Label(buttons_frame, text = 'label_1 ').grid(column = 0, row = 0)
ttk.Label(buttons_frame, text = 'label_2 ').grid(column = 1, row = 0)
ttk.Label(buttons_frame, text = 'label_3 ').grid(column = 2, row = 0)

name_typed.focus()
 
mighty.mainloop()