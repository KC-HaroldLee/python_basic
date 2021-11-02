import tkinter as tk
from tkinter import ttk

win1 =tk.Tk()
win1.title('python window with tab')
tabControl = ttk.Notebook(win1)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

# 각자 부모가 된다
tabControl.add(tab1, text='TAB1')
mighty1 = ttk.Labelframe(tab1, text='아 지나ㅉ 졸리다')
mighty1.grid(column=0, row=0, padx=8, pady=4)
a_label = ttk.Label(mighty1, text='뭐...')
a_label.grid(column=0, row=0 , padx=4, pady=4)

# 각자 부모가 된다
tabControl.add(tab2, text='TAB2')

tabControl.pack(expand=1, fill='both')

win1.mainloop()