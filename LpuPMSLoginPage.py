import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root = tk.Tk()

root.title("LPU Parking Management System")
root.geometry("700x400")
root.resizable(False, False)

titleIcon = PhotoImage(file="lpu3.png")
root.iconphoto(False, titleIcon)

bg = PhotoImage(file="lpu.png")
toshow = Label(root, image=bg)
toshow.place(x=0, y=0)

def run1():
    os.system('SignInPage.py')

def run2():
    os.system('SignUpPage.py')

logbut = tk.Button(root, text="Login", bg="green", fg="white", command=lambda: [root.destroy(), run1()])
logbut.pack(expand=True, ipadx=40, ipady=20)

sigbut = tk.Button(root, text="Sign Up", bg="blue", fg="white", command=lambda: [root.destroy(), run2()])
sigbut.pack(expand=True, ipadx=40, ipady=20)

root.mainloop()