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
    currentRadio = tk.Radiobutton(win1, text = colors[col], variable = radioVar, value = col, command = radio_callback)
    currentRadio.grid(column = col, row = 5, sticky = tk.W)

#########################
#  스크롤 텍스트 위젯
#########################

scroll_w = 40
scroll_h = 3

scroll = scrolledtext.ScrolledText(win1, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scroll.grid(column=0, row = 6, columnspan = 3)

#########################
#  레이아웃 만들기
#########################
    #  패딩 설정
    #########################
        #  반복문으로 패딩 설정
        #########################

buttons_frame = ttk.LabelFrame(win1, text = '  new lable ')
buttons_frame.grid(column = 0, row = 7, columnspan = 2, sticky = tk.W, padx=20, pady=20) # y라서 위 아래 모두 적용...
ttk.Label(buttons_frame, text = 'label_1 ').grid(column = 0, row = 0)
ttk.Label(buttons_frame, text = 'label_2 ').grid(column = 0, row = 1)
ttk.Label(buttons_frame, text = 'label_3 ').grid(column = 0, row = 2)

for child in buttons_frame.winfo_children() :
    print('작업중', child.cget('text')) # cget을 많은 곳에 활용할 수 있을 거 같다.
    child.grid_configure(padx = 30, pady = 4)
    # 근데 사실 하나만 해도 다 적용된다... column을 공유하니까

name_typed.focus()
 
win1.mainloop()

# <class 'tkinter.ttk.Label'> -dir
# ['_Misc__winfo_getint', '_Misc__winfo_parseitem', '__class__', '__delattr__', 
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bind', '_configure', 
# '_displayof', '_do', '_getboolean', '_getconfigure', '_getconfigure1', '_getdoubles', '_getints', 
# '_grid_configure', '_gridconvvalue', '_last_child_ids', '_name', '_nametowidget', '_noarg_', 
# '_options', '_register', '_report_exception', '_root', '_setup', '_subst_format', '_subst_format_str', 
# '_substitute', '_tclCommands', '_w', '_windowingsystem', 'after', 'after_cancel', 'after_idle', 'anchor', 
# 'bbox', 'bell', 'bind', 'bind_all', 'bind_class', 'bindtags', 'cget', 'children', 'clipboard_append', 
# 'clipboard_clear', 'clipboard_get', 'columnconfigure', 'config', 'configure', 'deletecommand', 'destroy', 
# 'event_add', 'event_delete', 'event_generate', 'event_info', 'focus', 'focus_displayof', 'focus_force', 
# 'focus_get', 'focus_lastfor', 'focus_set', 'forget', 'getboolean', 'getdouble', 'getint', 'getvar', 
# 'grab_current', 'grab_release', 'grab_set', 'grab_set_global', 'grab_status', 'grid', 'grid_anchor', 
# 'grid_bbox', 'grid_columnconfigure', 'grid_configure', 'grid_forget', 'grid_info', 'grid_location', 
# 'grid_propagate', 'grid_remove', 'grid_rowconfigure', 'grid_size', 'grid_slaves', 'identify', 
# 'image_names', 'image_types', 'info', 'instate', 'keys', 'lift', 'location', 'lower', 'mainloop', 
# 'master', 'nametowidget', 'option_add', 'option_clear', 'option_get', 'option_readfile', 'pack', 
# 'pack_configure', 'pack_forget', 'pack_info', 'pack_propagate', 'pack_slaves', 'place', 'place_configure', 
# 'place_forget', 'place_info', 'place_slaves', 'propagate', 'quit', 'register', 'rowconfigure', 'selection_clear', 
# 'selection_get', 'selection_handle', 'selection_own', 'selection_own_get', 'send', 'setvar', 'size', 'slaves', 
# 'state', 'tk', 'tk_bisque', 'tk_focusFollowsMouse', 'tk_focusNext', 'tk_focusPrev', 'tk_setPalette', 'tk_strictMotif', 
# 'tkraise', 'unbind', 'unbind_all', 'unbind_class', 'update', 'update_idletasks', 'wait_variable', 'wait_visibility', 
# 'wait_window', 'waitvar', 'widgetName', 'winfo_atom', 'winfo_atomname', 'winfo_cells', 'winfo_children', 'winfo_class', 
# 'winfo_colormapfull', 'winfo_containing', 'winfo_depth', 'winfo_exists', 'winfo_fpixels', 'winfo_geometry', 'winfo_height', 
# 'winfo_id', 'winfo_interps', 'winfo_ismapped', 'winfo_manager', 'winfo_name', 'winfo_parent', 'winfo_pathname', 'winfo_pixels', 
# 'winfo_pointerx', 'winfo_pointerxy', 'winfo_pointery', 'winfo_reqheight', 'winfo_reqwidth', 'winfo_rgb', 'winfo_rootx', 
# 'winfo_rooty', 'winfo_screen', 'winfo_screencells', 'winfo_screendepth', 'winfo_screenheight', 'winfo_screenmmheight', 
# 'winfo_screenmmwidth', 'winfo_screenvisual', 'winfo_screenwidth', 'winfo_server', 'winfo_toplevel', 'winfo_viewable', 
# 'winfo_visual', 'winfo_visualid', 'winfo_visualsavailable', 'winfo_vrootheight', 'winfo_vrootwidth', 'winfo_vrootx', 
# 'winfo_vrooty', 'winfo_width', 'winfo_x', 'winfo_y']