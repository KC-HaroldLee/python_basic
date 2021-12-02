import tkinter as tk

root = tk.Tk()
root.withdraw() # '관심없는 디버그창 종료'
from tkinter import messagebox as msg
msg.showinfo(title='뭐여', message='Python GUI created using tkinter:\nThe year is 2019')

