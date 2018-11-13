from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")


def helloCallBack():
    msg = messagebox.showinfo("Hello Python", "Hello World")


B = Button(top, text="Hello", command=helloCallBack,bg='#000000', fg='#ffffff')
B.place(x=5, y=5)
Button(top, text='RESET', command=helloCallBack, font='Arial -20 bold', relief='flat', bg='blue', fg='white', width=10, height=2).pack()
top.mainloop()
