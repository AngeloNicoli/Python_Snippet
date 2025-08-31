# Importing tkinter module
from tkinter import * 
from tkinter.ttk import *
import time
import random

# creating Tk window
master = Tk()

# setting geometry of tk window
master.geometry("200x200")

# button widget
b1 = Button(master, text = "Click me !")
b1.place(relx = 1, x =-2, y = 2, anchor = NE)

# label widget
l = Label(master, text = "I'm a Label")
l.place(anchor = NW)


def prova():
    a = random.randint(3, 9);
    b2 = Button(master, text = "GFG")
    b2.place(relx = 0.1+a/10, rely = 0.5, anchor = CENTER)
    print("Ciao")
    master.after(2000,prova)


master.after(2000,prova)

b4 = Button(master, text = "GF")
b4.place(x = 90,rely = 0.4, anchor = CENTER)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()