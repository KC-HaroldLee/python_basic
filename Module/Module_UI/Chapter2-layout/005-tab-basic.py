import tkinter as tk
from tkinter import ttk

win1 =tk.Tk()
win1.title('python window with tab')
tabControl = ttk.Notebook(win1)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='TAB1')
tabControl.add(tab2, text='TAB2')

tabControl.pack(expand=1, fill='both')

win1.mainloop()