import tkinter as tk
from tkinter import ttk

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

# 라디오 버튼을 위한 콜백 함수 / 체크와 라디오의 차이점을 생각해보면 콜백이 필요한 게 맞는 거 같다.
# 음 함수 이름은... 안해도 되나 mainloop() 때문에?
# 아니 만든다...
def radio_callback() :
    radioSelect = radioVar.get() # 여기....
    print('radio_callback() 호출')
    print('radioSelect : ', radioSelect)
    if radioSelect == 1 :
        win1.configure(background = COLOR1)
    elif radioSelect == 2 :
        win1.configure(background = COLOR2)
    elif radioSelect == 3 :
        win1.configure(background = COLOR3)


radioVar = tk.IntVar()
# radioSelect = radioVar.get() 이것 콜백 함수에 넣어야 했다.

radioVar_A = tk.IntVar()

radio1 = tk.Radiobutton(win1, text = 'Color1', variable = radioVar, value = 1, command = radio_callback) # ()안쓰고 함수 명만 쓴다.
radio1.grid(column = 0, row = 5, sticky=tk.W, columnspan = 3)
radio2 = tk.Radiobutton(win1, text = 'Color2', variable = radioVar, value = 2, command = radio_callback)
radio2.grid(column = 1, row = 5, sticky=tk.W, columnspan = 3)
radio3 = tk.Radiobutton(win1, text = 'Color3', variable = radioVar, value = 3, command = radio_callback)
# radio3 = tk.Radiobutton(win1, text = 'Color3', variable = radioVar_A, value = 3, command = radio_callback) # variable이 같은 애들끼리 묶인다.
radio3.grid(column = 2, row = 5, sticky=tk.W, columnspan = 3)

name_typed.focus()
 
win1.mainloop()