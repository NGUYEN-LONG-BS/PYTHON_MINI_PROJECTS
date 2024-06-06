from tkinter import *
from tkinter import font
from define import *

from app import App

window = Tk()

app = App(window)

font_title  = font.Font(family="Stencil Std", size= 44, weight=font.BOLD)
font_text   = font.Font(family="Terminal", size= 20)

# Label pack() place() grid()
label_python = Label( window, text="Python", font=font_title, bg=COLOR_RED, fg=COLOR_YELLOW,  padx=20, pady=10)
label_python.pack(side=TOP, fill=None, expand=True, anchor=CENTER)

label_tkinter = Label( window, text="Tkinter", font=font_title, bg=COLOR_RED, fg=COLOR_YELLOW,  padx=20, pady=10)
label_tkinter.pack(side=BOTTOM, anchor=SE)

window.mainloop()


