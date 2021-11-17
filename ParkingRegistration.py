import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root4 =tk.Tk()
root4.geometry("500x400")
root4.resizable(False, False)
root4.title("Parking Registration")

titleIcon = PhotoImage(file="lpu3.png")
root4.iconphoto(False, titleIcon)

bg = PhotoImage(file="parking.png")
toshow = Label(root4, image=bg)
toshow.place(x=0, y=0)

style = ttk.Style(root4)
style.theme_use("clam")

font.nametofont("TkDefaultFont").configure(size=12)

blockno = tk.IntVar(value=1)
cost = tk.StringVar()
confirm = tk.StringVar()

def showcost():
    bvalue = blockno.get()
    if bvalue>=1 and bvalue<=10:
        cost.set("Rs. 20")
    elif bvalue>=11 and bvalue<=20:
        cost.set("Rs. 25")
    elif bvalue>=21 and bvalue<=30:
        cost.set("Rs. 30")

def showconfirm():
    confirm.set("Parking Slot has been Registered")

reglabel = Label(root4, text="Registration No.:", bg="yellow")
regbutton = Entry(root4)

blocklabel = Label(root4, text="Block:", bg="yellow")
blockdropdown = Spinbox(root4, from_=1, to=32, textvariable=blockno, wrap=False, command=showcost)

costlabel = Label(root4, text="Cost:", bg="yellow")
parkcost = Label(root4, textvariable=cost)

setbutton = Button(root4, text="Book Slot", bg="green", command=showconfirm)
setlabel = Label(root4, textvariable=confirm)

reglabel.grid(row=0, column=0, sticky="NSEW", padx=(100,10), pady=(60,10))
regbutton.grid(row=0, column=1, sticky="NSEW", padx=(10,100), pady=(60,10))

blocklabel.grid(row=1, column=0, sticky="NSEW", padx=(100,10), pady=(0,10))
blockdropdown.grid(row=1, column=1, sticky="NSEW", padx=(10,100), pady=(0,10))

costlabel.grid(row=2, column=0, sticky="NSEW", padx=(100,10), pady=(0,10))
parkcost.grid(row=2, column=1, sticky="NSEW", padx=(10,100), pady=(0,10))

setbutton.grid(row=3, column=0, sticky="NSEW", columnspan=2, padx=(100,100), pady=(0,10))
setlabel.grid(row=4, column=0, sticky="NSEW", columnspan=2, padx=(100,100), pady=(0,10))

root4.mainloop()
