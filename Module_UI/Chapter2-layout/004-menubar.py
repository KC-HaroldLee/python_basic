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

#########################
#  메뉴바 만들기
#########################

from tkinter import Menu

menu_bar = Menu(win1) # 그치 여기 붙어야지
# menu_bar = Menu(mighty) # 이건 실험
win1.config(menu = menu_bar) # config랑 configure랑 뭔 차이죠?


file_menu = Menu(menu_bar)
file_menu.add_command(label='New')
file_menu.add_command(label='Reset')
file_menu.add_command(label='Exit')
print(str(file_menu.add_command.argv))

menu_bar.add_cascade(label='File', menu=file_menu)


#########################
#  기본 GUI 만들기
#########################
def click_me() :
    action.configure(text='Hello ' + name.get() + ' in ' + country.get())

ttk.Label(mighty, text='type your name').grid(column=0, row=0, sticky = tk.W) 
ttk.Label(mighty, text='choose a country').grid(column=1, row=0, sticky = tk.W)

name = tk.StringVar()
name_typed = ttk.Entry(mighty, width=12, textvariable=name)
name_typed.grid(column=0, row=1, sticky = tk.W)

country = tk.StringVar()
country_selected = ttk.Combobox(mighty, width=20, textvariable=country, state='readonly')
country_selected['values'] = ('KR', 'US', 'AU', 'JP', 'FR')
country_selected.grid(column=1, row=1)
country_selected.current(0)

action = ttk.Button(mighty, text='클릭 미', command=click_me)
action.grid(column=2, row=1)


#########################
#  체크박스 만들기
#########################

chVarDis = tk.IntVar()
chVarUn = tk.IntVar()
chVarEn = tk.IntVar()

# chVarDis
check1 = tk.Checkbutton(mighty, text = 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 4, sticky = tk.W)

# chVarUn
check2 = tk.Checkbutton(mighty, text = 'UnChecked', variable = chVarUn)
check2.deselect()
check2.grid(column = 1, row = 4, sticky = tk.W)

# chVarEn
check3 = tk.Checkbutton(mighty, text = 'Enabled', variable= chVarEn)
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
        mighty.configure(background = colors[0])
    elif radioSelect == 1 :
        mighty.configure(background = colors[1])
    elif radioSelect == 2 :
        mighty.configure(background = colors[2])


radioVar = tk.IntVar()
radioVar.set(99)

for col in range(3) :
    print(col)
    currentRadio = tk.Radiobutton(mighty, text = colors[col], variable = radioVar, value = col, command = radio_callback)
    currentRadio.grid(column = col, row = 5, sticky = tk.W)

#########################
#  스크롤 텍스트 위젯
#########################

scroll_w = 40
scroll_h = 3

scroll = scrolledtext.ScrolledText(mighty, width=scroll_w, height=scroll_h, wrap=tk.WORD)
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