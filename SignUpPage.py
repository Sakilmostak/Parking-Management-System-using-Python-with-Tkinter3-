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

root2 =tk.Tk()
root2.geometry("700x800")
root2.resizable(False, False)
root2.title("Sign Up")

root2.columnconfigure(0, weight=1)
root2.rowconfigure(0, weight=1)

def run():
    os.system('LpuPMSLoginPage.py')

titleIcon = PhotoImage(file="lpu3.png")
root2.iconphoto(False, titleIcon)

bg = PhotoImage(file="lpu2.png")
toshow = Label(root2, image=bg)
toshow.place(x=0, y=0)

style = ttk.Style(root2)
style.theme_use("clam")

font.nametofont("TkDefaultFont").configure(size=12)

frame = ttk.Frame(root2)
frame.grid(padx=100, pady=100, sticky="NSEW")

userlabel = ttk.Label(frame, text="Name:")
userinput = ttk.Entry(frame, width=30)

reglabel = ttk.Label(frame, text="Registration No.:")
reginput = ttk.Entry(frame, width=30)

hostlabel = ttk.Label(frame, text="Hostel/Block:")
hostinput = ttk.Entry(frame, width=30)

genderlabel = ttk.Label(frame, text="Gender:")
genderselect = tk.StringVar()
male = ttk.Radiobutton(frame, text="Male", variable=genderselect, value="m")
female = ttk.Radiobutton(frame, text="Female", variable=genderselect, value="f")

phonelabel = ttk.Label(frame, text="Moblie No.")
phoneinput = ttk.Entry(frame, width=30)

emaillabel = ttk.Label(frame, text="Email:")
emailinput = ttk.Entry(frame, width=30)

signbutton = ttk.Button(frame, text="Sign In")
returnbutton = ttk.Button(frame, text="Return Back", command=lambda: [root2.destroy(), run()])

# Griding

userlabel.grid(row=0, column=0, sticky="W")
userinput.grid(row=0, column=1, sticky="EW")
userinput.focus()

reglabel.grid(row=1, column=0, stick="W")
reginput.grid(row=1, column=1, sticky="EW")

hostlabel.grid(row=2, column=0, sticky="W")
hostinput.grid(row=2, column=1, sticky="EW")

genderlabel.grid(row=3, column=0, sticky="W")
male.grid(row=4, column=0, sticky="EW")
female.grid(row=4, column=1, sticky="EW")

phonelabel.grid(row=5, column=0, sticky="W")
phoneinput.grid(row=5, column=1, sticky="EW")

emaillabel.grid(row=6, column=0, sticky="W")
emailinput.grid(row=6, column=1, sticky="EW")

signbutton.grid(row=7, column=0, columnspan=2, sticky="EW")
returnbutton.grid(row=8, column=0, columnspan=2, sticky="EW")

for things in frame.winfo_children():
    things.grid_configure(padx=15, pady=15)

root2.mainloop()

