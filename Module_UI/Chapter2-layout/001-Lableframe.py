import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win1 = tk.Tk()
win1.title('text_input_test') 
win1.resizable(width=True, height=False)

def click_me() :
    action.configure(text='Hello ' + name.get() + ' in ' + country.get())

ttk.Label(win1, text='type your name').grid(column=0, row=0, sticky = tk.W) 
ttk.Label(win1, text='choose a country').grid(column=1, row=0, sticky = tk.W)

name = tk.StringVar()
name_typed = ttk.Entry(win1, width=12, textvariable=name)
name_typed.grid(column=0, row=1, sticky = tk.W)

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
    #  반복문으로 위젯 추가
    #########################

colors = ['Blue', 'Gold', 'Red']

def radio_callback() :
    radioSelect = radioVar.get()
    print('radio_callback() 호출')
    print('radioSelect : ', radioSelect)
    if radioSelect == 0 :
        win1.configure(background = colors[0])
    elif radioSelect == 1 :
        win1.configure(background = colors[1])
    elif radioSelect == 2 :
        win1.configure(background = colors[2])


radioVar = tk.IntVar()
radioVar.set(99)

for col in range(3) :
    print(col)
    currentRadio = tk.Radiobutton(win1, text = colors[col], variable = radioVar, value = col, command = radio_callback)
    currentRadio.grid(column = col, row = 5, sticky = tk.W)

#########################
#  스크롤 텍스트 위젯
#########################

scroll_w = 40 # 너무 적게 설정했어서...
scroll_h = 3

# scroll = scrolledtext.ScrolledText(win1, width = scroll_w, height = scroll_h, wrap = tk.WORD)
# scroll.grid(column = 0, columnspan = 3)
scroll = scrolledtext.ScrolledText(win1, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scroll.grid(column=0, row = 6, columnspan = 3)

#########################
#  레이아웃 만들기
#########################

buttons_frame = ttk.LabelFrame(win1, text = '  new lable!!  ')
buttons_frame.grid(column = 0, row = 7, columnspan = 2, sticky = tk.W)
# button_frame.grid(column = 1, row = 7) # 음
ttk.Label(buttons_frame, text = 'label_1 in frame').grid(column = 0, row = 0) # 뭐여 바로 지정하네
ttk.Label(buttons_frame, text = 'label_2 in frame').grid(column = 1, row = 0) # 뭐여 바로 지정하네
ttk.Label(buttons_frame, text = 'label_3 in frame').grid(column = 2, row = 0) # 뭐여 바로 지정하네


name_typed.focus()
 
win1.mainloop()