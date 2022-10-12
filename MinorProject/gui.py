import time
from tkinter import CENTER, W, Tk, Button, Entry, StringVar, Grid

root = Tk()
root.geometry('700x450')
root.config(bg="#24F0E3")

timee = StringVar(root)

def fun1():
    timee.set(10)

timee.set(12)
entry1  = Entry(root, textvariable = timee, font=('Georgia 60'), width=2, justify=CENTER)
entry1.place(relx=0.2, rely=0.2)

b1 = Button(root, text='Click me', command=fun1).place(relx=0.2, rely=0.5)
root.mainloop()
