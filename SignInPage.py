import sys
import os
import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root1 =tk.Tk()
root1.geometry("700x500")
root1.resizable(False, False)
root1.title("Login Page")

root1.columnconfigure(0, weight=1)
root1.rowconfigure(0, weight=1)

titleIcon = PhotoImage(file="lpu3.png")
root1.iconphoto(False, titleIcon)

bg = PhotoImage(file="lpu2.png")
toshow = Label(root1, image=bg)
toshow.place(x=0, y=0)

style = ttk.Style(root1)
style.theme_use("clam")

font.nametofont("TkDefaultFont").configure(size=12)

def run():
    os.system('ParkingRegistration.py')


frame = ttk.Frame(root1)
frame.grid(padx=140, pady=120, sticky="NSEW")

username = tk.StringVar()
password = tk.StringVar()
ershow = tk.StringVar()

def checkIdentity(*args):
    firstpara = username.get()
    secondpara = password.get()

    if firstpara == "sakil" and secondpara == "sastapassword":
        root1.destroy()
        run()
    elif firstpara == "" and secondpara == "":
        ershow.set("Empty. Please enter the details!")
    else:
        ershow.set("Wrong Input. Try again!!")


userlabel = ttk.Label(frame, text="User-name:")
userinput = ttk.Entry(frame, width=30, textvariable=username)
passwordlabel = ttk.Label(frame, text="Password:")
passwordinput = ttk.Entry(frame, width=30, textvariable=password)
errordisplay = ttk.Label(frame, textvariable=ershow)
signbutton = ttk.Button(frame, text="Sign In", command=checkIdentity)

userlabel.grid(row=0, column=0, sticky="W")
userinput.grid(row=0, column=1, sticky="EW")
userinput.focus()

passwordlabel.grid(row=1, column=0, sticky="W")
passwordinput.grid(row=1, column=1, sticky="EW")

errordisplay.grid(row=2, column=0, columnspan=2, sticky="EW")
signbutton.grid(row=3, column=0, columnspan=2, sticky="EW")

for things in frame.winfo_children():
    things.grid_configure(padx=15, pady=15)

root1.mainloop()
