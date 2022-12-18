# from tkinter import *
from tkinter import ttk
import tkinter
root = tkinter.Tk()

frame1 = ttk.Frame(root, padding=10)
frame1.grid()

ttk.Label(frame1, text='Hello world!').grid(column=0, row=0)
ttk.Button(frame1, text='Quit',command=root.destroy).grid(column=1, row=0)


root.mainloop()