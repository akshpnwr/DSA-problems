# from tkinter import *
# from tkinter import ttk
# import tkinter
# root = tkinter.Tk()

# frame1 = ttk.Frame(root, padding=10)
# frame1.grid()

# ttk.Label(frame1, text='Hello world!').grid(column=0, row=0)
# ttk.Button(frame1, text='Quit',command=root.destroy).grid(column=1, row=0)


# root.mainloop()
# from tkinter import *
# master = Tk()
# var1 = IntVar()
# Checkbutton(master, 
#             text='male', 
#             variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, 
#             text='female', 
#             variable=var2).grid(row=1, sticky=W)
# mainloop()

# canvas = tk.Canvas(win, width=200,height=100, bg='white')
# button = tk.Button(win,bg='red', activebackground='black', activeforeground='white', text='stop',command=win.destroy)

# v1= tk.IntVar()
# v2= tk.IntVar()

# tk.Label(win, text='Name').grid(row=0)
# tk.Label(win,text='age').grid(row=1)

# tk.Entry(win).grid(row=0,column=1)
# tk.Entry(win).grid(row=1,column=1)

# tk.Button(win,text='stop',command=win.destroy).grid(row=2,column=2)
# canvas.create_text(20,50, text='Hi fucy',fill='red')
# tk.Checkbutton(win,text='Male',variable=v1).grid(row=0)
# tk.Checkbutton(win,text='female',variable=v2).grid(row=1)

# canvas.pack()
# button.pack()
# from tkinter import *
# root = Tk()
# frame = Frame(root)
# frame.pack()
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
# redbutton = Button(frame, text = 'Red', fg ='red')
# redbutton.pack( side = BOTTOM)
# greenbutton = Button(frame, text = 'Green', fg='green')
# greenbutton.pack( side = LEFT )
# bluebutton = Button(frame, text ='Blue', fg ='blue')
# bluebutton.pack( side = BOTTOM )
# blackbutton = Button(bottomframe, text ='Black', fg ='black')
# blackbutton.pack( side = BOTTOM)
# root.mainloop()



# frame = tk.Frame(win)
# frame.pack()

# bFrame = tk.Frame(win)
# bFrame.pack(side='bottom')

# redButton = tk.Button(frame,fg='red',text='red')
# redButton.pack(side='bottom')

# blueBtn = tk.Button(frame,fg='blue',text='blue')
# blueBtn.pack(side='right')

# greenBtn = tk.Button(frame,fg='green',text='green')
# greenBtn.pack(side='left')

# blackBtn = tk.Button(bFrame,fg='black',text='black')
# blackBtn.pack(side='bottom')

# import tkinter as tk

# win = tk.Tk()

# win.title('Akash')

# tk.Label(win,text='This a lable').pack()

# l = tk.Listbox(win);
# l.insert(1,'a')
# l.insert(2,'b')

# l.pack()


# win.mainloop()

# def addNumber():
    # res = int(e1.get())+int(e2.get())
    # txt.set(res)

# win = tk.Tk()
# txt = tk.StringVar()

# tk.Label(win,text='Enter 1st num').grid(row=0)
# tk.Label(win,text='Enter 2nd num').grid(row=1)
# e1 = tk.Entry(win)
# e1.grid(row=0,column=1)
# e2 = tk.Entry(win)
# e2.grid(row=1,column=1)

# tk.Label(win,text='Result').grid(row=2)
# tk.Label(win,text='',textvariable=txt).grid(row=2,column=2)

# tk.Button(win,text='Calculate',command=addNumber).grid(row=3,column=2)

# import tkinter as tk

# win = tk.Tk()

# m = tk.Menu(win)
# win.config(menu=m)
# filemenu = tk.Menu(m)

# m.add_cascade(label='file',menu=filemenu)

# filemenu.add_command(label='new')
# filemenu.add_command(label='open...')
# filemenu.add_command(label='exit',command=win.quit)
# win.mainloop()

# from tkinter import * 
# root = Tk()
# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')
# root.mainloop()

##################
### Question 1 ###
##################

# from tkinter import *

# def greet():
#     nm = e1.get()
#     msg.set('Hi there! {}'.format(nm))

# win = Tk()
# msg = StringVar()

# Label(win,text='name').grid(row=0)
# Label(win,text='age').grid(row=1)

# e1 = Entry(win)
# e2 = Entry(win)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# Button(text='Greetings',command=greet).grid(row=2)
# Label(win,text='',textvariable=msg).grid(row=3)
# Button(text='quit',command=win.destroy,fg='white',bg='red').grid(row=4)

# win.mainloop()

##################
### Question 2 ###
##################

from tkinter import *

def getf():
    res = float(e1.get())*(1 + float(e2.get())*float(e3.get()))/100
    fa.set(res)

win = Tk()
fa = StringVar()

Label(win,text='Principal amount').grid(row=0)
Label(win,text='Rate').grid(row=1)
Label(win,text='Time').grid(row=2)

e1 = Entry(win)
e2 = Entry(win)
e3 = Entry(win)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

Label(win,text='final amount').grid(row=3)
Label(win,text='',textvariable=fa).grid(row=3,column=2)

Button(win,text='calculate',command=getf).grid(row=4)

win.mainloop()